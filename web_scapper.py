import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from constants import ElementsIDs, CONSOLE_PLACE, ORDER_CATEGORY


class AgamdamentosBot(webdriver.Chrome):
    def __init__(self):
        options = webdriver.ChromeOptions()
        super(AgamdamentosBot, self).__init__(options=options)

    def click_on_element(self, element_id: str):
        button = self.find_element_by_id(element_id)
        button.click()

    def select_tel_aviv(self):
        open_dropdown_button = self.find_element_by_css_selector(f'div[id*="{ElementsIDs.SELECT_PLACE_BUTTON}"]')
        open_dropdown_button.click()

        self.select_dropdown_option(ElementsIDs.PLACE_DROPDOWN, CONSOLE_PLACE)

    def fill_order_type_form(self):
        """Fills the form responsible for the type of ordering."""
        type_drop_down_button = self.find_element_by_css_selector(f'div[id*="{ElementsIDs.SELECT_ORDER_CATEGORY}"]')
        type_drop_down_button.click()

        self.select_dropdown_option(ElementsIDs.CATEGORY_DROPDOWN, ORDER_CATEGORY)
        go_next_button = self.find_element_by_css_selector(f'button[id*="{ElementsIDs.TYPE_FORM_BUTTON}"]')
        go_next_button.click()

    def submit_checking(self):
        """Clicks on the submit button to check if there are available turns."""
        self.find_element_by_css_selector(f'span[id*="ui-chkbox-icon"]').click()
        self.find_element_by_css_selector(f'button[id*={ElementsIDs.SUBMIT_BUTTON}]').click()

    def select_dropdown_option(self, dropdown_id: str, selected_option: str):
        """
        Selects an option automatically.


        :param dropdown_id: The id of dropdown itself.
        :param selected_option: The option which we want to select.
        """
        drop_down = self.find_element_by_css_selector(f'div[id*="{dropdown_id}"]')
        drop_down_children = drop_down.find_elements_by_css_selector("*")

        for child_element in drop_down_children:
            print(child_element.text)
            if selected_option in child_element.text:
                print(f"Clicked!")
                child_element.click()

    def write_in_input(self, field_id: str, text: str):
        """
        Write text in an input field.

        :param field_id: The id of the field element
        :param text: The text we want to write in the input.
        """

        input_field = self.find_element_by_css_selector(f'input[id*="{field_id}"]')
        input_field.send_keys(text)

    def open_web_page(self, url: str):
        """
        Opens a web page with chrome.
        :param url: The url of the page.
        """
        self.get(url)
        self.maximize_window()

    def wait_for_page(self, time_to_wait: int = 10):
        """
        Wait for the loading of a page.
        :param time_to_wait: The time in seconds we want to wait.
        """
        self.implicitly_wait(time_to_wait)
