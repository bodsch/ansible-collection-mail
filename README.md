# Ansible Collection - bodsch.mail

A collection of Ansible roles to manage mail services.


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-mail/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-collection-mail)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-collection-mail)][releases]

[ci]: https://github.com/bodsch/ansible-collection-mail/actions
[issues]: https://github.com/bodsch/ansible-collection-mail/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-collection-mail/releases


## supported operating systems

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-collection-mail/tags)!

---

## Roles

| Role                                                        | Build State | Description |
|:----------------------------------------------------------- | :---- | :---- |
| [bodsch.mail.postfix](./roles/postfix/README.md)         | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-mail/postfix.yml?branch=main)][postfix]       | Ansible role to install and configure `postfix`. |
| [bodsch.mail.dovecot](./roles/dovecot/README.md)         | [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-mail/dovecot.yml?branch=main)][dovecot]       | Ansible role to install and configure `dovecot`. |


[postfix]: https://github.com/bodsch/ansible-collection-mail/actions/workflows/postfix.yml
[dovecot]: https://github.com/bodsch/ansible-collection-mail/actions/workflows/dovecot.yml
