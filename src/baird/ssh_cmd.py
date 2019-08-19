"""Build SSH command"""


class SSHCmd:
    """Create SSH command line from arguments"""
    def __init__(self, args):
        self.args = args
        self.ssh_cmd = 'ssh'

    def bastion_login(self):
        """
        Return bastion_login string
        """
        if self.args.bastion_login:
            self.ssh_cmd = self.ssh_cmd + ' -l ' + self.args.bastion_login

    def bastion_id(self):
        """
        Return bastion_id string
        """
        if self.args.bastion_id:
            self.ssh_cmd = self.ssh_cmd + ' -i ' + self.args.bastion_id

    def bastion(self):
        """
        Return bastion server string
        """
        if self.args.bastion:
            self.ssh_cmd = self.ssh_cmd + ' ' + self.args.bastion + ' -At ssh '

    def login(self):
        """
        Return login name string
        """
        if self.args.login:
            self.ssh_cmd = self.ssh_cmd + ' -l ' + self.args.login

    def identityfile(self):
        """
        Return identityfile string
        """
        if self.args.identityfile:
            self.ssh_cmd = self.ssh_cmd + ' -i ' + self.args.identityfile

    def return_ssh_cmd(self):
        """
        Return full ssh_cmd
        """
        self.bastion_login()
        self.bastion_id()
        self.bastion()
        self.login()
        self.identityfile()
        return self.ssh_cmd
