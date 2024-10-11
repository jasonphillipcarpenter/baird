## BAIRD

Baird is a system administration tool for simultaneous management of
multiple instances through SSH. Baird utilises
[tmux](https://tmux.github.io/) to create individual panes per instance
and facilitate synchronised input.

Baird is named after the puppeteer, Bil
[Baird](https://en.wikipedia.org/wiki/Bil_Baird)

# Preparing the Development

1. Ensure `pip` and `pipenv` are installed.
2. Clone repository: `git clone git@gitlab.com:boweevil/baird`
3. `cd` into the repository.
4. Fetch development dependencies `make install`
5. Activate virtualenv: `pipenv shell`

# Installation

- Install using pip

```shell
pip install -e .
```

# Usage

```bash
baird [-h] [-t <TITLE>] [-l <LOGIN>] [-i <IDENTITY FILE>]
      [-b <BASTION SERVER>] [-bl <BASTION LOGIN>] [-bi <BASTION ID>]
      <SERVER LIST> [<SERVER LIST> ...]
```

- Connect with user and key:

```bash
baird -l user1 -i ~/.ssh/key server1 server2 server3
```

- Using only a list of servers:

```bash
baird server1 server2 server3 server4 server5
```

- Bash globbing:

```bash
baird server{01..05}
```

- Using a bastion server:

```bash
baird --title 'Production' --bastion bastion01 --bastion-login bastionuser --bastion-id ~/.ssh/bastionkey --login serveruser --identityfile ~/.ssh/serverkey server{1..3}
```

# Running Tests

```bash
make test
```
