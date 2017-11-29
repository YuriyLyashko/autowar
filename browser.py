import pyautogui, time, datetime, os, logging
from open_chrome import open_chrome
from tutor_py_files.wrappers import else_click_to_help_arrow, print_time

pyautogui.FAILSAFE = False





def find_image(image_name, **kwargs):
    for i in range(10):
        coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\tutor\\samples\\', image_name), **kwargs)
        if coord:
            return coord
    return None

def find_flashing_image(image_name, **kwargs):
    for i in range(1000):
        coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\tutor\\samples\\', image_name), **kwargs)
        if coord:
            return coord
    return None

def click_to_center(button, higher_on=0, lower_on=0, righter_on=0, lefter_on=0):
    x, y = pyautogui.center(button)
    pyautogui.moveTo(x=x+righter_on-lefter_on, y=y+lower_on-higher_on, duration=0.5)
    pyautogui.click()


@else_click_to_help_arrow
@print_time
def find_image_and_click(image_name, **kwargs):
    image = find_image(image_name, **kwargs)
    if not image:
        logging.error("{} doesn't find".format(image_name))
        pyautogui.alert("{} doesn't find".format(image_name))
    logging.INFO('{} {}'.format(image_name, image))
    if image:
        click_to_center(image)
        return True
    return False

def find_flashing_image_and_click(image_name,
                                  higher_on=0, lower_on=0, righter_on=0, lefter_on=0,
                                  **kwargs):
    logging.info('find_flashing_image_and_click')
    image = find_flashing_image(image_name, **kwargs)
    if not image:
        logging.error("{} doesn't find".format(image_name))
        pyautogui.alert("{} doesn't find".format(image_name))
    logging.info('{} {}'.format(image_name, image))
    if image:
        click_to_center(image, higher_on=higher_on, lower_on=lower_on, righter_on=righter_on, lefter_on=lefter_on)

def set_full_screen(REGIONS_ON_WINDOW):
    logging.info('set_full_screen')
    pyautogui.moveTo(5, 5, 1)
    time.sleep(2)
    logging.info('''click to button_full_screen_game_top''')
    find_image_and_click('quest_menu__button_full_screen_game_top.png',
                         region=REGIONS_ON_WINDOW['center_up'],
                         grayscale=True
                         )
    time.sleep(2)

def scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu):
    logging.info('scroll_to_see_top_menu')
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 100))




def open_browser():
    logging.info('''open chrome''')
    driver = open_chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def go_to_social_network(driver, soc_network):
    logging.info('''go to social network''')
    driver.get(soc_network)

def login(driver, login, password):
    logging.info('''login''')
    driver.find_element_by_id('email').send_keys(login)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

def get_screen_resolution_size():
    logging.info('''get screen resolution size''')
    width_screen, height_screen = pyautogui.size()
    logging.info('width_screen {}'.format(width_screen))
    logging.info('height_screen {}'.format(height_screen))
    return width_screen, height_screen

def scroll_down(driver, left_coord_top_menu, top_coord_top_menu):
    logging.info('''scroll down''')
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu))

def click_to_game_area(width_top_menu, left_coord_top_menu, top_coord_top_menu, height_screen):
    logging.info('''click to game area''')
    time.sleep(2)
    pyautogui.click(x=width_top_menu - left_coord_top_menu, y=top_coord_top_menu + height_screen / 2)

def accept_flash_running():
    logging.info('''accept flash running''')
    time.sleep(0.5)
    button_accept_flash_running = find_flashing_image('accept_flash_running.png')
    if button_accept_flash_running:
        click_to_center(button_accept_flash_running)
