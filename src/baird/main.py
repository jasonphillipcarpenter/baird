"""Connect to multiple servers using tmux"""
import subprocess
import textwrap
import argparse
import libtmux
from baird.cli import Cli
from baird.ssh_cmd import SSHCmd
from baird.tmux_session import TmuxSession
from baird.tmux_window import TmuxWindow
from baird.connections import Connections


def main():
    """Connect to multiple servers using tmux"""
    parser = Cli(
        argparse,
        textwrap
    )
    args = parser.return_parser()
    ssh_cmd = SSHCmd(
        args
    ).return_ssh_cmd()
    tmux_session = TmuxSession(
        subprocess,
        libtmux.Server(),
        libtmux.exc,
        args
    ).get_session()
    tmux_window = TmuxWindow(
        tmux_session,
        args
    ).return_new_window()
    Connections(
        tmux_window,
        ssh_cmd,
        args
    ).create_connections()


if __name__ == "__main__":
    main()
