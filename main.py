from browser import Browser
from pages.gleam_io_page import GleamIoPage
from pages.twitter_login_page import TwitterLoginPage
from pages.twitter_page import TwitterPage


# REFERAL_LINK = 'https://wn.nr/7G3qdE'
REFERAL_LINK = 'https://gleam.io/zzxy5/fanaply-new-years-giveaway'
ACCOUNTS_FILE_PATH = 'accounts.txt'


def complete_twitter_task(user_info):
    try:
        browser = Browser()
        browser.start()

        browser.get_url(REFERAL_LINK)
        gleam_io_page = GleamIoPage(browser)

        gleam_io_page.open_twitter_login_page()

        twitter_login_page = TwitterLoginPage(browser)
        twitter_login_page.submit_credentials(user_info)

        # gleam_io_page.submit_details(user_info)

        gleam_io_page.click_follow_on_twitter_task()

        twitter_page = TwitterPage(browser)
        twitter_page.click_follow()

        gleam_io_page.mark_task_as_completed()

        browser.stop()
    except Exception as e: # TODO: Add specific exception
        browser.stop()
        print(e)

if __name__ == '__main__':
    with open(ACCOUNTS_FILE_PATH, 'r') as file:
        for line in file:
            login, password, phone_number, bsc_address, tg_username = line.split(',')

            complete_twitter_task({
                'login': login,
                'password': password,
                'phone_number': phone_number,
                'bsc_address': bsc_address,
                'tg_username': tg_username,
            })
