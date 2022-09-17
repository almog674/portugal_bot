"""
Name: pages.py
Author: Almog Maimon
Purpose: Functions which tells us how to behave in each page.
Date: 14/09/2022
"""
import time

from constants import ElementsIDs
from web_scapper import AgamdamentosBot
from selenium import webdriver


def handle_welcome_page(bot: AgamdamentosBot):
    """Handles the welcome page, continue to scheduling."""
    bot.click_on_element(ElementsIDs.COOKIES_DISABLE_BUTTON)
    time.sleep(2)
    bot.click_on_element(ElementsIDs.CLOSE_POPUP_BUTTON)
    bot.click_on_element(ElementsIDs.SCHEDULE_BUTTON)
