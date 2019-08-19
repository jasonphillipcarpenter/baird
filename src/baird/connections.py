"""Create TMUX panes running SSH connection strings"""


class Connections:
    """Define SSH connections"""
    def __init__(self, window, ssh_cmd, args):
        self.window = window
        self.ssh_cmd = ssh_cmd
        self.args = args

    def create_connections(self):
        """
        Create the connections
        """
        first = 0
        for server in self.args.servers:
            server_cmd = self.ssh_cmd + ' ' + server
            print()
            print(server_cmd)
            if first == 0:
                pane = self.window.panes[0]
                pane.select_pane()
                pane.send_keys(server_cmd)
                pane = None
            else:
                pane = self.window.split_window(attach=False)
                self.window.select_layout('tiled')
                pane.select_pane()
                pane.send_keys(server_cmd)
                pane = None

            first = 1

        self.window.set_window_option('synchronize-panes', 'on')
