import time

from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


RESOURCE_NAME = 'gleam.io'
USERNAME_OR_EMAIL_FIELD_ID = 'username_or_email'
PASSWORD_FIELD_ID = 'password'
PHONE_NUMBER_INPUT_ID = 'challenge_response'


class TwitterLoginPage(BasePage):

    # MARK: - Init

    def __init__(self, browser):
        super().__init__(browser)

        self.browser.switch_to_window(-1)
        self.wait_until_found(By.ID, USERNAME_OR_EMAIL_FIELD_ID)

    # MARK: - Public methods

    def submit_credentials(self, credentials):
        username_field = self.__username_field()
        password_field = self.__password_field()

        username_field.send_keys(credentials['login'])
        password_field.send_keys(credentials['password'])

        password_field.send_keys(Keys.RETURN)

        if not self.browser.wait_until_current_window_closed():
            self.__submit_phone_number(credentials['phone_number'])

        time.sleep(3) # FIXME
        self.browser.switch_to_window(0)

    # MARK: - Private methods

    def __submit_phone_number(self, phone_number):
        phone_number_field = self.__phone_number_field()

        phone_number_field.send_keys(phone_number)
        phone_number_field.send_keys(Keys.RETURN)

    def __username_field(self):
        return self.browser \
                   .driver \
                   .find_element_by_id(USERNAME_OR_EMAIL_FIELD_ID)

    def __password_field(self):
        return self.browser \
                   .driver \
                   .find_element_by_id(PASSWORD_FIELD_ID)

    def __phone_number_field(self):
        try:
            return self.browser \
                       .driver \
                       .find_element_by_id(PHONE_NUMBER_INPUT_ID)
        except exceptions.NoSuchElementException:
            return None
