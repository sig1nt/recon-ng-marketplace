Welcome to the Recon-ng Marketplace! The official module repository for the Recon-ng Framework.

For guidance on contributing to or developing modules, see the [Development Guide](https://github.com/lanmaster53/recon-ng/wiki/Development-Guide) in the official [Recon-ng wiki](https://github.com/lanmaster53/recon-ng/wiki).

**This repository is not intended for independent use.** The Recon-ng Marketplace is used from within the Recon-ng Framework. To download and use Recon-ng, visit the [official Recon-ng Framework repository](https://github.com/lanmaster53/recon-ng).

# Dev Branch

# What is this?

This branch is synthesized from all of my personal patches to the various plugins, as well as PRs/patch sets that I like on the official `recon-ng-marketplace` repo that haven't been picked up. This repo should always base off of the master branch, and as a result will be rebased frequently as I pull patches out of it when they get merged into the main repo (hopefully).

## How to use this

Switch marketplaces is actually a relatively easy task. To do so, change the url
at `recon/core/base.py:51` to:

```
https://raw.githubusercontent.com/sig1nt/recon-ng-marketplace/dev/
```

## List of PRs that I've pulled in

* lanmaster53#201
* lanmaster53#200
* lanmaster53#199
* lanmaster53#197
* lanmaster53#196
* lanmaster53#195
* lanmaster53#186
* lanmaster53#110 (with modification)
