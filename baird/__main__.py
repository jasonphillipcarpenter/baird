"""Connect to multiple servers using tmux"""
import subprocess
import textwrap
import argparse
import libtmux
import toml
from cli import Cli
from ssh_cmd import SSHCmd
from tmux_session import TmuxSession
from tmux_window import TmuxWindow
from connections import Connections


def main():
    """Connect to multiple servers using tmux"""
    parser = Cli(argparse, textwrap, toml)
    args = parser.return_args()
    ssh_cmd = SSHCmd(args).return_ssh_cmd()
    tmux_session = TmuxSession(
        subprocess, libtmux.Server(), libtmux.exc, args
    ).get_session()
    tmux_window = TmuxWindow(tmux_session, args).return_new_window()
    Connections(tmux_window, ssh_cmd, args).create_connections()


if __name__ == "__main__":
    main()
