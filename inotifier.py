class INotifier:
    """
    A basic interface for notify a user about events.
    """

    def notify(self, message: str):
        """
        notify the user with a message.
        :param message: The message we want to send.
        """
        raise NotImplementedError("YOu must inherit from this class to use this method.")
