"""Setup TMUX session"""


class TmuxSession:
    """Define TMUX session"""
    def __init__(self, subprocess, tmux, args):
        self.subprocess = subprocess
        self.tmux = tmux
        self.args = args
        self.tmux_server = tmux.Server()

    def get_current_session_id(self):
        """
        Check for current TMUX session

        :returns: Current session ID
        """
        current_session = self.subprocess.run([
            'tmux',
            'display-message',
            '-p',
            '"#{session_id}"'
        ], stdout=self.subprocess.PIPE)
        current_session_id = current_session.stdout.decode().replace(
            '"', '').rstrip()
        return self.tmux_server.get_by_id(current_session_id)

    def get_new_session_id(self):
        """
        Create new TMUX session

        :returns: New session ID
        """
        return self.tmux_server.new_session(
            attach=True, session_name=self.args.title, session_id='$0')

    def get_session(self):
        """
        Get TMUX session to be used

        :returns: session ID
        """
        try:
            session = self.get_current_session_id()
        except self.tmux.exc.LibTmuxException:
            session = self.get_new_session_id()
        return session
