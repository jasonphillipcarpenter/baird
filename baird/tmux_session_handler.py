"""Setup TMUX session"""


class TmuxSessionHandler:
    """Define TMUX session"""

    def __init__(self, subprocess, tmux_server, tmux_exception, args):
        self.subprocess = subprocess
        self.tmux_server = tmux_server
        self.tmux_exception = tmux_exception
        self.args = args
        self.session_is_new = False

    def get_current_session_id(self):
        """
        Check for current TMUX session

        :returns: Current session ID
        """
        current_session = self.subprocess.run(
            ["tmux", "display-message", "-p", '"#{session_id}"'],
            stdout=self.subprocess.PIPE,
        )
        if not current_session.stdout:
            raise self.tmux_exception.LibTmuxException("No current TMUX session found")
        current_session_id = current_session.stdout.decode().replace('"', "").rstrip()
        return self.tmux_server.get_by_id(current_session_id)

    def get_new_session_id(self):
        """
        Create new TMUX session

        :returns: New session ID
        """
        self.session_is_new = True
        return self.tmux_server.new_session(
            attach=False, session_name=self.args.title, session_id="$0"
        )

    def get_session(self):
        """
        Get TMUX session to be used

        :returns: session ID
        """
        try:
            session = self.get_current_session_id()
        except self.tmux_exception.LibTmuxException:
            session = self.get_new_session_id()
        return session

    def attach_session(self, session):
        """
        Attach to TMUX session

        :param session: TMUX session ID
        """
        self.subprocess.run(["tmux", "attach-session", "-t", session.get("session_id")])
