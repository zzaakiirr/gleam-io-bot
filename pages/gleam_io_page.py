import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


TWITTER_LOGIN_CSS_SELECTOR = "a.twitter-background.popup-window"
FOLLOW_ON_TWITTER_CSS_SELECTOR = 'a.enter-link.twitter_follow-border'
TWITTER_FOLLOW_BTN_CSS_SELECTOR = 'div.entry_details span.twitter-label'

BSC_ADDRESS_INPUT_NAME = 'bsc_address'
TG_USERNAME_INPUT_NAME = 'tg_username'
# AGREE_TO_TERMS = 'i_have_read_the_terms_and_conditions'

TASK_COMPLETED_LINK_SELECTOR = "a[ng-click='saveEntryDetails(entry_method)']"


class GleamIoPage(BasePage):

    # MARK: - Init

    def __init__(self, browser):
        super().__init__(browser)

        # FIXME: Doesn't work
        self.wait_until_found(By.CSS_SELECTOR, TWITTER_LOGIN_CSS_SELECTOR)

    # MARK: - Public methods

    def open_twitter_login_page(self):
        links = self.__twitter_login_links()

        self.browser.action_on_first_interactable(links, action_name='click')

    def submit_details(self, user_info):
        bsc_address_input = self.__bsc_address_input()
        tg_username_input = self.__tg_username_input()

        bsc_address_input.send_keys(user_info['bsc_address'])
        tg_username_input.send_keys(user_info['tg_username'])

    def click_follow_on_twitter_task(self):
        links = self.__twitter_follow_links()
        self.browser.action_on_first_interactable(links, action_name='click')

        self.__wait_until_follow_btn_appeared()

        follow_btns = self.__follow_btns()
        self.browser.action_on_first_interactable(
            follow_btns,
            action_name='click'
        )

    def mark_task_as_completed(self):
        self.browser.switch_to_window(0)

        task_completed_links = self.__check_if_task_completed_links()
        self.browser.action_on_first_interactable(
            task_completed_links,
            action_name='click'
        )

        time.sleep(3) # FIXME

    # MARK: - Private methods

    def __wait_until_login_completed(self):
        self.wait_until_found(By.NAME, BSC_ADDRESS_INPUT_NAME)

    def __wait_until_follow_btn_appeared(self):
        self.wait_until_found(By.CSS_SELECTOR, TWITTER_FOLLOW_BTN_CSS_SELECTOR)

    def __twitter_login_links(self):
        return self.browser \
                   .driver \
                   .find_elements_by_css_selector(TWITTER_LOGIN_CSS_SELECTOR)

    def __twitter_follow_links(self):
        return self.browser \
                   .driver \
                   .find_elements_by_css_selector(FOLLOW_ON_TWITTER_CSS_SELECTOR)

    def __bsc_address_input(self):
        return self.browser \
                   .driver \
                   .find_element_by_name(BSC_ADDRESS_INPUT_NAME)

    def __tg_username_input(self):
        return self.browser \
                   .driver \
                   .find_element_by_name(TG_USERNAME_INPUT_NAME)

    def __follow_btns(self):
        return self.browser \
                   .driver \
                   .find_elements_by_css_selector(TWITTER_FOLLOW_BTN_CSS_SELECTOR)

    def __check_if_task_completed_links(self):
        return self.browser \
           .driver \
           .find_elements_by_css_selector(TASK_COMPLETED_LINK_SELECTOR)
