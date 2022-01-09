import time

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver import chrome 
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager


class Browser:

    # MARK: - Init

    def __init__(self,
                 driver=webdriver.Chrome,
                 options=chrome.options.Options(),
                 caps=webdriver.DesiredCapabilities().CHROME):
        self.driver = driver
        self.options = options
        self.caps = caps

    # MARK: - Public methods

    def start(self):
        self.__configure()

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=self.options,
            desired_capabilities=self.caps,
        )

    def stop(self):
        if self.driver is None:
            return

        self.driver.quit()
        self.driver = None

    def get_url(self, url):
        self.driver.get(url)

    def switch_to_window(self, position):
        last_window = self.driver.window_handles[position]
        self.driver.switch_to.window(last_window)

    def action_on_first_interactable(self, elements, action_name='click'):
        for element in elements:
            try:
                actions = ActionChains(self.driver).move_to_element(element)
                getattr(actions, action_name)()
                actions.perform()
            except exceptions.ElementNotInteractableException:
                continue
            else:
                return True

        return False

    def wait_until_current_window_closed(self, timeout=3):
        while timeout > 0:
            try:
                # Raises error if window closed
                self.driver.current_window_handle
            except exceptions.NoSuchWindowException:
                # self.switch_to_window(1) # Maybe useless
                return True
            else:
                time.sleep(1)
                timeout -= 1

        return False

    # MARK: - Private methods

    def __configure(self):
        # Prevent selenium detection
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled'
        )

        # Run in silent mode
        # self.options.add_argument('--headless')

        # self.__disable_image_loading()
        self.__disable_full_load_waiting()

    def __disable_image_loading(self):
        prefs = {
            'profile.default_content_settings': { 'images': 2 },
            'profile.managed_default_content_settings': { 'images': 2},
        }
        self.options.experimental_options['prefs'] = prefs

    def __disable_full_load_waiting(self):
        self.caps['pageLoadStrategy'] = 'none'
