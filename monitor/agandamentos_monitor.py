"""
Name: agandamentos_monitor.py
Author: Almog Maimon
Purpose: Monitor the available dates in agandamentos and notify when needed.
Date: 17/09/2022
"""
import time

from constants import SECONDS_IN_MINUTE, FOUND_MESSAGE
from notifier.whatsapp_notifier import WhatsappNotifier
from web_bot.pages import handle_pages
from web_bot.web_scapper import AgamdamentosBot


class AgandamentosMonitor:
    def __init__(self, web_bot: AgamdamentosBot, notifier: WhatsappNotifier, time_to_wait: int):
        self.web_bot = web_bot
        self.notifier = notifier
        self.time_to_wait = time_to_wait

    def monitor(self):
        while True:
            handle_pages(self.web_bot)
            if self.web_bot.check_if_available():
                self.notifier.notify_everyone(FOUND_MESSAGE)

            time.sleep(self.time_to_wait * SECONDS_IN_MINUTE)
