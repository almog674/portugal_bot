from typing import List

import pywhatkit

from inotifier import INotifier

PHONE_NUMBER = "+972542141100"
NOTHING_MESSAGE = "Just a test of the bot"
FOUND_MESSAGE = "THe bot found something!"


class WhatsappNotifier(INotifier):
    def __init__(self, number_groups: dict):
        self.number_groups = number_groups

    def add_number_group(self, numbers_to_add: List[str], group_name: str):
        """
        Adds a group we want to notify to the number groups.

        :param numbers_to_add: List of the numbers we want the groups to contain.
        :param group_name: The name of the group.
        """
        # TODO - Add a validation.
        self.number_groups[group_name] = numbers_to_add

    def add_number_to_group(self, number_to_add: str, group_name: str):
        """
        Adds a number to existing group.

        :param number_to_add: The number of the user.
        :param group_name: The name of the group the user wants to join.
        """
        pass

    def notify(self, message: str, groups_to_notify: List[str]):
        """
        Notify one group or more with a message
        :param message: The message we want to send in whatsapp.
        :param groups_to_notify: All teh groups we want to notify.
        """
        for group in groups_to_notify:
            for user in group:
                pywhatkit.sendwhatmsg_instantly(user, NOTHING_MESSAGE)
