import pyautogui, time, datetime, os, logging
from multiprocessing import Pool
from selenium import webdriver

from tutor_py_files.directories_settings import screens_dir

pyautogui.FAILSAFE = False

def get_screen(screens_dir):
    for _ in range(1):
        coord = pyautogui.screenshot('{}{}{}'.format(os.getcwd(),
                                                     screens_dir,
                                                     '{}.png'.format(datetime.datetime.now().strftime('%d_%m_%Y__%H_%M_%S')))
                                     )
        time.sleep(5)

def monosearch_10(image_name, samples_dir, **kwargs):
    for i in range(10):
        coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), samples_dir, image_name), **kwargs)
        if coord:
            return coord
    return None

def monosearch_1000(image_name, samples_dir, **kwargs):
    for i in range(1000):
        coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), samples_dir, image_name),
                                         grayscale=True,
                                         **kwargs)
        if coord:
            return coord
    return None

def monosearch(come):
    image_name, samples_dir, region = come
    for i in range(1000):
        coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), samples_dir, image_name),
                                         grayscale=True,
                                         region=region)
        if coord:
            return coord
    return None

def find_all_images(image_name, samples_dir, **kwargs):
    for i in range(10):
        coords = pyautogui.locateAllOnScreen('{}{}{}'.format(os.getcwd(), samples_dir, image_name),
                                             # grayscale=True,
                                             **kwargs)
        if coords:
            return coords
    return None

def monosearch_10_and_click(image_name, samples_dir, **kwargs):
    image = monosearch_10(image_name, samples_dir, **kwargs)
    if not image:
        logging.error("{} doesn't find".format(image_name))
        pyautogui.alert("{} doesn't find".format(image_name))
    logging.info('{} {}'.format(image_name, image))
    if image:
        click_to_center(image)
        return True
    return False

def monosearch_1000_and_click(image_name,
                              higher_on=0, lower_on=0, righter_on=0, lefter_on=0,
                              **kwargs):
    logging.info('monosearch_1000_and_click')
    image = monosearch_1000(image_name, **kwargs)
    if not image:
        logging.error("{} doesn't find".format(image_name))
        get_screen(screens_dir)
        pyautogui.alert("{} doesn't find".format(image_name))
    logging.info('{} {}'.format(image_name, image))
    if image:
        click_to_center(image, higher_on=higher_on, lower_on=lower_on, righter_on=righter_on, lefter_on=lefter_on)

def monoregion_multisearch(image_name, samples_dir, region=None, **kwargs):
    logging.info('{}'.format('monoregion_multisearch'))
    with Pool(os.cpu_count()) as pool:
        for image in pool.imap_unordered(monosearch, [(image_name, samples_dir, region) for _ in range(os.cpu_count())]):
            logging.info('{} {}'.format(image_name, image))
            if image:
                pool.terminate()
                return image
    logging.error("{} doesn't find".format(image_name))
    get_screen(screens_dir)
    pyautogui.alert("{} doesn't find".format(image_name))

def monoregion_multisearch_and_click(image_name,
                                     samples_dir,
                                     region=None,
                                     higher_on=0, lower_on=0, righter_on=0, lefter_on=0,
                                     **kwargs):
    logging.info('{}'.format('monoregion_multisearch_and_click'))
    image = monoregion_multisearch(image_name, samples_dir, region=region, **kwargs)
    click_to_center(image, higher_on=higher_on, lower_on=lower_on, righter_on=righter_on, lefter_on=lefter_on)

def multiregion_monosearch(image_name,
                           samples_dir,
                           regions,
                           **kwargs):
    logging.info('{}'.format('multiregion_monosearch'))
    with Pool(5) as pool:
        for image in pool.imap_unordered(monosearch, ((image_name, samples_dir, regions['left_up']),
                                                      (image_name, samples_dir, regions['left_down']),
                                                      (image_name, samples_dir, regions['center_mid']),
                                                      (image_name, samples_dir, regions['right_up']),
                                                      (image_name, samples_dir, regions['right_down']),
                                                      (image_name), samples_dir, None
                                                      )
                                         ):
            logging.info('{} {}'.format(image_name, image))
            if image:
                return image
    logging.error("{} doesn't find".format(image_name))
    get_screen(screens_dir)
    pyautogui.alert("{} doesn't find".format(image_name))

def multiregion_monosearch_and_click(image_name,
                                     samples_dir,
                                     regions,
                                     higher_on=0, lower_on=0, righter_on=0, lefter_on=0,
                                     **kwargs):
    logging.info('{}'.format('multiregion_monosearch_and_click'))
    image = multiregion_monosearch(image_name, samples_dir, regions, **kwargs)
    click_to_center(image, higher_on=higher_on, lower_on=lower_on, righter_on=righter_on, lefter_on=lefter_on)

def move_mouse_to(button, righter_on=0, lefter_on=0, lower_on=0, higher_on=0):
    x, y = pyautogui.center(button)
    pyautogui.moveTo(x=x + righter_on - lefter_on, y=y + lower_on - higher_on, duration=0.5)

def click_to_center(button, higher_on=0, lower_on=0, righter_on=0, lefter_on=0):
    x, y = pyautogui.center(button)
    pyautogui.moveTo(x=x+righter_on-lefter_on, y=y+lower_on-higher_on, duration=0.5)
    pyautogui.click()

def set_full_screen(samples_dir, REGIONS_ON_WINDOW):
    logging.info('set_full_screen')
    pyautogui.moveTo(5, 5, 1)
    time.sleep(2)
    logging.info('''click to button_full_screen_game_top''')
    monosearch_10_and_click('quest_menu__button_full_screen_game_top.png',
                            samples_dir,
                            region=REGIONS_ON_WINDOW['center_up'],
                            grayscale=True)
    time.sleep(2)

def scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu):
    logging.info('scroll_to_see_top_menu')
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 100))


def open_browser():
    logging.info('''open open_browser''')
    driver = webdriver.Chrome('{}\chromedriver.exe'.format(os.path.dirname(__file__)))
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

def accept_flash_running(region, samples_dir):
    logging.info('''accept flash running''')
    time.sleep(0.5)
    button_accept_flash_running = monosearch_1000('accept_flash_running.png', samples_dir, region=region)
    if button_accept_flash_running:
        click_to_center(button_accept_flash_running)

def change_lanuage(lanuage_image, samples_dir):
    select_language_arrow = monosearch_1000('language_select_arrow.png', samples_dir)
    if select_language_arrow:
        click_to_center(select_language_arrow)
        language = monosearch_1000(lanuage_image, samples_dir)
        if language:
            click_to_center(language)
            return True
        raise ValueError("Language isn't finded")
    raise ValueError("language_select_arrow isn't finded")

def close_all_bonus_windows(samples_dir, driver, height_screen, left_coord_top_menu, top_coord_top_menu):
    '''close all bonus windows'''
    while monosearch_10('button_close_window.png', samples_dir):
        all_buttons_close_window = find_all_images('button_close_window.png', samples_dir)
        for coord in all_buttons_close_window:
            click_to_center(coord)
    scroll_down(driver, 0, height_screen)
    button_thank_you_for_comeback = monosearch_10('button_thank_you_for_comeback.png', samples_dir)
    if button_thank_you_for_comeback:
        click_to_center(button_thank_you_for_comeback)
    button_restore = monosearch_10('button_restore.png', samples_dir)
    if button_restore:
        click_to_center(button_restore)
    scroll_down(driver, left_coord_top_menu, top_coord_top_menu - 100)