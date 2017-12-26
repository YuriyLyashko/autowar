import re, time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from tutor_py_files import wrappers
from browser import open_browser
from authentication_info import ADMIN_LOGIN, ADMIN_PASS, SOC_NET_LINKS, SOC_AUTH_INFO


def load_max_lvl_dump(SOCIAL, SERVER, ID):
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
    select.select_by_value('DM')

    '''move mouse to dropdown menu'''
    dropdown = driver.find_element_by_id('yw1')
    first = dropdown.find_element_by_class_name('first')
    ActionChains(driver).move_to_element(first).perform()

    '''click to Дамп'''
    driver.find_element_by_link_text('Дамп').click()

    '''fill user field 1'''
    driver.find_element_by_class_name('inputtext').send_keys(SOCIAL + ID)

    '''select social network to get dump'''
    select = Select(driver.find_element_by_name('MDump[social]'))
    select.select_by_value(SERVER)

    '''click to button load list'''
    driver.find_element_by_link_text('load list').click()

    '''choose dump file'''
    select = Select(driver.find_element_by_id('s_dump'))
    '''find a max level dump'''
    max_level_dump = max([int(re.findall(r'\d+', o.text[-5:])[0]) for o in select.options])
    '''choose max level dump'''
    select.select_by_visible_text('{}{}_{}_{}'.format(SOCIAL, ID, str(max_level_dump), SERVER))

    '''click to Target checkbox'''
    driver.find_element_by_name('MDump[t_accept]').click()

    '''fill user field 2'''
    driver.find_element_by_name('MDump[t_user]').send_keys(SOCIAL + ID)

    '''select social network to put dump'''
    select = Select(driver.find_element_by_name('MDump[t_social]'))
    select.select_by_value(SERVER)

    '''click to button Load dump'''
    driver.find_element_by_link_text('Load dump').click()

    '''accept loading'''
    alert = driver.switch_to_alert()
    alert.accept()

    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    SOCIAL = 'FB' # 'VK','RBK'
    SERVER = 'FB' # 'DM', 'FB'
    ID = SOC_AUTH_INFO[SOCIAL]['ID']
    load_max_lvl_dump(SOCIAL, SERVER, ID)