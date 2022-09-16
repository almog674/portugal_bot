from typing import List, Set

import pywhatkit
import json
from inotifier import INotifier


class WhatsappNotifier(INotifier):
    def __init__(self, number_groups: dict):
        self.number_groups = number_groups

    def get_all_groups(self) -> str:
        """Returns all the groups in json format."""
        return json.dumps(self.number_groups)

    def add_number_group(self, numbers_to_add: Set[str], group_name: str):
        """
        Adds a group we want to notify to the number groups.

        :param numbers_to_add: Set of the numbers we want the groups to contain.
        :param group_name: The name of the group.
        """
        if self.is_group_exists(group_name):
            print(f"The group {group_name} already exists.")
            return

        self.number_groups[group_name] = numbers_to_add

    def add_number_to_group(self, number_to_add: str, group_name: str):
        """
        Adds a number to existing group.

        :param number_to_add: The number of the user.
        :param group_name: The name of the group the user wants to join.
        """
        if not self.is_group_exists(group_name):
            print(f"The group {group_name} does not exists.")

        self.number_groups[group_name].add(number_to_add)

    def remove_number_from_group(self, number_to_remove: str, group_name: str):
        """
        Removes a number from existing group.

        :param number_to_remove: The number of the user.
        :param group_name: The name of the group the user wants to exit.
        """
        if not self.is_group_exists(group_name):
            print(f"The group {group_name} does not exists.")

        self.number_groups[group_name].remove(number_to_remove)

    def is_group_exists(self, group_name: str) -> bool:
        """Checks if a group exists."""
        return self.number_groups.get(group_name)

    def notify(self, message: str, groups_to_notify: List[str]):
        """
        Notify one group or more with a message

        :param message: The message we want to send in whatsapp.
        :param groups_to_notify: All the groups we want to notify.
        """
        for group in groups_to_notify:
            if group in list(self.number_groups.keys()):
                for user in self.number_groups[group]:
                    print(user)
                    pywhatkit.sendwhatmsg_instantly(user, message, tab_close=True
                                                    )
