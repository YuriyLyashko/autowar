from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

from tutor_py_files import wrappers
from browser import open_browser
from authentication_info import ADMIN_LOGIN, ADMIN_PASS, SOC_AUTH_INFO, SOC_NET_LINKS


def wipe(SOCIAL, SERVER, ID):
    '''open chrome'''
    driver = open_browser()

    '''go to admin panel'''
    driver.get(SOC_NET_LINKS['ADM'])

    '''login'''
    driver.find_element_by_id('YumUserLogin_username').send_keys(ADMIN_LOGIN)
    driver.find_element_by_id('YumUserLogin_password').send_keys(ADMIN_PASS)
    driver.find_element_by_name('yt0').click()

    '''select social network'''
    select = Select(driver.find_element_by_name('social'))
    select.select_by_value(SERVER)

    '''click to Пользователи'''
    driver.find_element_by_link_text('Пользователи').click()

    '''find user'''
    driver.find_element_by_id('Filter__id.match').send_keys(SOCIAL + ID)
    driver.find_element_by_id('Filter_aka.match').click()

    '''click to user ID'''
    try:
        full_ID = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, SOCIAL + ID)))
        full_ID.click()
        '''click to button К списку'''
        tabs = driver.find_element_by_class_name('tabs')
        tabs.find_element_by_class_name('button').click()

        '''click to button Удалить'''
        driver.find_element_by_class_name('remove').click()

        '''accept deleting'''
        time.sleep(2)
        alert = driver.switch_to_alert()
        alert.accept()

        time.sleep(3)
        driver.quit()
    except Exception:
        driver.quit()
        # pass




if __name__ == '__main__':
    SOCIAL = 'FB'  # 'VK', 'FB'
    SERVER = 'FB'  # 'DM', 'FB'
    ID = SOC_AUTH_INFO[SOCIAL]['ID']
    wipe(SOCIAL, SERVER, ID)