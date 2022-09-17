import time

from constants import ElementsIDs, URL, Credentials
from pages import handle_welcome_page
from web_scapper import AgamdamentosBot
from selenium.webdriver.common.keys import Keys


def main():
    bot = AgamdamentosBot()
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

    print()


if __name__ == '__main__':
    main()
