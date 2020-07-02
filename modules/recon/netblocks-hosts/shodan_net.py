from recon.core.module import BaseModule
import shodan
import time
import re


class Module(BaseModule):

    meta = {
        'name': 'Shodan Network Enumerator',
        'author': 'Mike Siegel and Tim Tomes (@lanmaster53) & Ryan Hays (@_ryanhays)',
        'version': '1.1',
        'description': 'Harvests hosts from the Shodan API by using the \'net\' search operator. Updates the \'hosts\' '
                       'table with the results.',
        'required_keys': ['shodan_api'],
        'query': 'SELECT DISTINCT netblock FROM netblocks WHERE netblock IS NOT NULL',
        'options': (
            ('limit', 1, True, 'limit number of api requests per input source (0 = unlimited)'),
        ),
        'dependencies': ['shodan']
    }

    def module_run(self, netblocks):
        limit = self.options['limit']
        api = shodan.Shodan(self.keys.get('shodan_api'))

        for netblock in netblocks:
            self.heading(netblock, level=0)
            query = f"net:{netblock}"

            try:
                page = 1
                rec_count = 0
                total_results = 1
                while rec_count <= total_results:
                    results = api.search(query, page=page)
                    total_results = results['total']

                    for host in results['matches']:
                        rec_count += 1
                        try:
                            for hostname in host['hostnames']:
                                self.insert_ports(host=hostname, ip_address=host['ip_str'], port=host['port'],
                                                  protocol=host['transport'])
                                self.insert_hosts(host=hostname, ip_address=host['ip_str'])
                        except KeyError:
                            self.insert_ports(ip_address=ipaddr, port=host['port'], protocol=host['transport'])
                            self.insert_host(ip_address=host['ip_str'])

                    page += 1
                    time.sleep(limit)

            except shodan.exception.APIError:
                pass
