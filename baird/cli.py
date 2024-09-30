"""Handle command-line arguments"""


class Cli:
    """Handle command-line arguments"""

    def __init__(self, argument_parser, text_wrapper, toml):
        self.argparse = argument_parser.ArgumentParser(
            formatter_class=argument_parser.RawTextHelpFormatter,
            description=text_wrapper.dedent(
                """\
                Use Tmux to ssh to mutliple targets at once.
                Any configuration in ~/.ssh/config is respected as %(prog)s is
                essentially a wrapper for ssh & tmux.
                    """
            ),
            epilog=text_wrapper.dedent(
                """\
                EXAMPLES:
                    Display help:
                    %(prog)s --help

                    Connect with user and key:
                    %(prog)s -l user1 -i ~/.ssh/key server1 server2 server3

                    Using only a list of servers:
                    %(prog)s server1 server2 server3 server4 server5

                    Bash globbing:
                    %(prog)s server{01..05}

                    Using a bastion server:
                    %(prog)s \\
                        --title 'Production' \\
                        --bastion bastion01 \\
                        --bastion-login bastionuser \\
                        --bastion-id ~/.ssh/bastionkey \\
                        --login serveruser \\
                        --identityfile ~/.ssh/serverkey \\
                        server{1..3}

               """
            ),
        )
        self._pyproject = toml.load("pyproject.toml")

    def get_version(self):
        return self._pyproject["tool"]["poetry"]["version"]

    def add_arguments(self):
        """
        Add arguments for command-line interface
        """
        self.argparse.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"%(prog)s {self.get_version()}",
            help="Show %(prog)s version\n",
        )

        self.argparse.add_argument(
            "-t",
            "--title",
            metavar="<TITLE>",
            default="BAIRD",
            help="Specify the tmux window title. (default: %(default)s)\n",
        )

        self.argparse.add_argument(
            "-l",
            "--login",
            metavar="<LOGIN>",
            help="Specify the username for the connection.\n",
        )

        self.argparse.add_argument(
            "-i",
            "--identityfile",
            metavar="<IDENTITY FILE>",
            help="Specify the SSH key for the connection.\n",
        )

        self.argparse.add_argument(
            "-b",
            "--bastion",
            metavar="<BASTION SERVER>",
            help="Specify bastion server for the connection.\n",
        )

        self.argparse.add_argument(
            "-bl",
            "--bastion-login",
            metavar="<BASTION LOGIN>",
            help="Specify bastion server username for the connection.\n",
        )

        self.argparse.add_argument(
            "-bi",
            "--bastion-id",
            metavar="<BASTION ID>",
            help="Specify bastion server SSH key for the connection.\n",
        )

        self.argparse.add_argument(
            "servers",
            metavar="<SERVER LIST>",
            type=str,
            nargs="*",
            help="REQUIRED: Specify a list of servers to which to connect.\n",
        )

    def return_args(self):
        """
        Return argument_parser

        :returns: parsed arguments
        """
        self.add_arguments()
        return self.argparse.parse_args()

    def return_parser(self):
        """
        Return argument_parser

        :returns: argparse
        """
        self.add_arguments()
        return self.argparse
