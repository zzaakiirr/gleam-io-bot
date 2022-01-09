from selenium.webdriver.common.by import By

from pages.base_page import BasePage


FOLLOW_BTN_CSS_SELECTOR = "div[data-testid='confirmationSheetConfirm']"


class TwitterPage(BasePage):

    # MARK: - Init

    def __init__(self, browser):
        super().__init__(browser)

        self.browser.switch_to_window(-1)
        self.wait_until_found(
            By.CSS_SELECTOR, FOLLOW_BTN_CSS_SELECTOR,
            timeout=10
        )

    # MARK: - Public methods

    def click_follow(self):
        follow_btns = self.__follow_btns()

        self.browser.action_on_first_interactable(
            follow_btns,
            action_name='click'
        )

    # MARK: - Private methods

    def __follow_btns(self):
        return self.browser \
                   .driver \
                   .find_elements_by_css_selector(FOLLOW_BTN_CSS_SELECTOR)
