import pyautogui, time, datetime, os
from open_chrome import open_chrome


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

def find_image_and_click(image_name, **kwargs):
    image = find_image(image_name, **kwargs)
    if not image: pyautogui.alert("{} doesn't find".format(image_name))
    print(image_name, image, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
    if image:
        click_to_center(image)

def find_flashing_image_and_click(image_name,
                                  higher_on=0, lower_on=0, righter_on=0, lefter_on=0,
                                  **kwargs):
    image = find_flashing_image(image_name, **kwargs)
    if not image: pyautogui.alert("{} doesn't find".format(image_name))
    print(image_name, image, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
    if image:
        click_to_center(image, higher_on=higher_on, lower_on=lower_on, righter_on=righter_on, lefter_on=lefter_on)

def set_full_screen(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN):
    pyautogui.moveTo(5, 5, 1)
    time.sleep(2)
    '''click to button_full_screen_game_top'''
    find_image_and_click('button_full_screen_game_top.png',
                         region=REGIONS_ON_WINDOW['center_up'],
                         grayscale=True
                         )
    time.sleep(2)

def scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu):
    print('scroll_to_see_top_menu')
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 100))




def open_browser():
    '''open chrome'''
    driver = open_chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def go_to_social_network(driver, soc_network):
    '''go to social network'''
    driver.get(soc_network)

def login(driver, login, password):
    '''login'''
    driver.find_element_by_id('email').send_keys(login)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()

def get_screen_resolution_size():
    '''get screen resolution size'''
    width_screen, height_screen = pyautogui.size()
    print('width_screen', width_screen)
    print('height_screen', height_screen)
    return width_screen, height_screen

def scroll_down(driver, left_coord_top_menu, top_coord_top_menu):
    '''scroll down'''
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu))

def click_to_game_area(width_top_menu, left_coord_top_menu, top_coord_top_menu, height_screen):
    '''click to game area'''
    time.sleep(2)
    pyautogui.click(x=width_top_menu - left_coord_top_menu, y=top_coord_top_menu + height_screen / 2)

def accept_flash_running():
    '''accept flash running'''
    time.sleep(0.5)
    button_accept_flash_running = find_flashing_image('accept_flash_running.png')
    if button_accept_flash_running:
        click_to_center(button_accept_flash_running)
