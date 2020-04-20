"""Create a new TMUX window"""


class TmuxWindow:
    """Define a TMUX window"""

    def __init__(self, session, args):
        self.session = session
        self.args = args

    def return_new_window(self):
        """
        Return new TMUX window

        :returns: TMUX window
        """
        return self.session.new_window(attach=True, window_name=self.args.title)
