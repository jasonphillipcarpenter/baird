# Baird

![alt text](assets/Baird3-icon-192x192.png "Baird")

Baird is a system administration tool for simultaneous management of
multiple instances through SSH. Baird utilises
[tmux](https://tmux.github.io/) to create individual panes per instance
and facilitate synchronised input.

![Demo](assets/demo.gif)

Baird is named after the puppeteer, Bil
[Baird](https://en.wikipedia.org/wiki/Bil_Baird)

## Preparing the Development

1. Ensure [pip] and [poetry] are installed.
2. Clone repository: `git clone git@gitlab.com:jasoncarpenter/baird`
3. `cd` into the repository directory.
4. Fetch development dependencies `make install_pkgs`

## Installation

- Install using pip

```shell
make install
```

## Usage

```shell
baird [-h] [-v] [-t <TITLE>] [-l <LOGIN>] [-i <IDENTITY FILE>] [-b <BASTION SERVER>] [-bl <BASTION LOGIN>] [-bi <BASTION ID>]
      <SERVER LIST> [<SERVER LIST> ...]
```

- Connect with user and key:

```shell
baird -l user1 -i ~/.ssh/key server1 server2 server3
```

- Using only a list of servers:

```shell
baird server1 server2 server3 server4 server5
```

- Using Bash globbing, we can pass a shorthand list of servers to Baird:

```bash
baird server{01..05}
```

- Using a bastion server:

```bash
baird --title 'Production' --bastion bastion01 --bastion-login bastionuser --bastion-id ~/.ssh/bastionkey --login serveruser --identityfile ~/.ssh/serverkey server{1..3}
```

## Running Tests

```shell
make test
```

[poetry]: https://python-poetry.org/
[pip]: https://pip.pypa.io/en/stable/
