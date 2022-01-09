from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_WAIT_TIMEOUT = 5


class BasePage:

    # MARK: - Init

    def __init__(self, browser):
        self.browser = browser

    # MARK: - Public methods

    def wait_until_found(self, *args, **kwargs):
        timeout = kwargs.get('timeout', DEFAULT_WAIT_TIMEOUT)

        try:
            element_present_condition = EC.presence_of_element_located(args)
            WebDriverWait(self.browser.driver, timeout) \
                .until(element_present_condition)
        except exceptions.TimeoutException:
            print('Timeout waiting for element')
