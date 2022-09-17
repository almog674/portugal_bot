"""
Name: pages.py
Author: Almog Maimon
Purpose: Functions which tells us how to behave in each page.
Date: 14/09/2022
"""
import time

from web_bot.constants import ElementsIDs, Credentials, URL
from web_bot.web_scapper import AgamdamentosBot
from selenium import webdriver


def handle_welcome_page(bot: AgamdamentosBot):
    """Handles the welcome page, continue to scheduling."""
    bot.click_on_element(ElementsIDs.COOKIES_DISABLE_BUTTON)
    time.sleep(2)
    bot.click_on_element(ElementsIDs.CLOSE_POPUP_BUTTON)
    bot.click_on_element(ElementsIDs.SCHEDULE_BUTTON)


def handle_pages(bot: AgamdamentosBot):
    """Handle all the steps needed for checking if there is available turn"""
    bot.open_web_page(URL)

    bot.wait_for_page(10)
    handle_welcome_page(bot)

    bot.wait_for_page()
    bot.write_in_input(ElementsIDs.ID_NUMBER_INPUT, Credentials.ID_NUMBER)
    bot.write_in_input(ElementsIDs.DATE_INPUT, Credentials.BIRTH_DATE)

    bot.find_element_by_css_selector('button[id*="searchIcon"]').click()
    bot.select_tel_aviv()
    bot.fill_order_type_form()
    time.sleep(2)
    bot.submit_checking()

    time.sleep(1000)
    bot.quit()
