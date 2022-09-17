from typing import List


class INotifier:
    """
    A basic interface for notify a user about events.
    """

    def notify(self, message: str, groups_to_notify: List[str]):
        """
        notify the user with a message.
        :param message: The message we want to send.
        :param groups_to_notify: The groups of users we want to notify.
        """
        raise NotImplementedError("YOu must inherit from this class to use this method.")
