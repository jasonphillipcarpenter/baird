"""Build SSH command"""


class SSHCmd:
    """Create SSH command line from arguments"""

    def __init__(self, args):
        self.args = args
        self.ssh_cmd = "ssh"

    def bastion_login(self):
        """
        Return bastion_login string

        :returns: bastion_login
        """
        return f"-l {self.args.bastion_login}"

    def bastion_id(self):
        """
        Return bastion_id string

        :returns: bastion_id
        """
        return f"-i {self.args.bastion_id}"

    def bastion(self):
        """
        Return bastion server string

        :returns: bastion
        """
        return f"{self.args.bastion} -At ssh"

    def login(self):
        """
        Return login name string

        :returns: login
        """
        return f"-l {self.args.login}"

    def identityfile(self):
        """
        Return identityfile string

        :returns: identityfile
        """
        return f"-i {self.args.identityfile}"

    def return_ssh_cmd(self):
        """
        Return full ssh_cmd

        :returns: ssh_cmd
        """
        ssh_cmd = [self.ssh_cmd]
        if self.args.bastion_login:
            ssh_cmd.append(self.bastion_login())
        if self.args.bastion_id:
            ssh_cmd.append(self.bastion_id())
        if self.args.bastion:
            ssh_cmd.append(self.bastion())
        if self.args.login:
            ssh_cmd.append(self.login())
        if self.args.identityfile:
            ssh_cmd.append(self.identityfile())
        return " ".join(ssh_cmd)
