from seleniumbase import Driver
import time
from selenium.webdriver.common.by import By
from seleniumbase import SB
from dotenv import load_dotenv
from xpath import patreon_username_xpath, patreon_password_xpath, continue_button_xpath, continue_button_2_xpath, google_button
from xpath import gmail_username_xpath, next_button_xpath, gmail_passwords_xpath, not_now_button
import os


load_dotenv()

patreon_email = os.getenv('patreon_email')
patreon_password = os.getenv('patreon_password')

domain = "https://www.patreon.com/"
patreon_login_url = domain + 'login'
driver = Driver(uc=True)


def google_auth():
    driver.wait_for_element(google_button)
    driver.click(google_button, by = 'xpath') # клик на вход с помощью гугл

    window_handles = driver.window_handles
    print("Window Handles:", window_handles)
    driver.switch_to.window(window_handles[1])

    driver.type(gmail_username_xpath, patreon_email, timeout = 2)
    driver.click(next_button_xpath)

    driver.type(gmail_passwords_xpath, patreon_password)
    driver.click(next_button_xpath, timeout = 2)
    
    #driver.click(not_now_button, timeout = 3)



def mail_auth():
    driver.type(patreon_username_xpath, patreon_email, by = 'xpath')
    driver.click(continue_button_xpath, by = 'xpath')
    driver.type(patreon_password_xpath, patreon_password, by = 'xpath')
    driver.click(continue_button_2_xpath, by = 'xpath')


def create_post():
    driver.uc_open_with_reconnect(patreon_login_url, 4) # Переходит на сайт патреона
    driver.uc_gui_click_captcha() # Кликает на капчу
    time.sleep(1)

    if '@gmail' in patreon_email:
        google_auth()
    else:
        mail_auth()

    time.sleep(1000)
    driver.get(domain + 'posts/new?postType=text_only')
    time.sleep(10)
    driver.quit()

create_post()

       