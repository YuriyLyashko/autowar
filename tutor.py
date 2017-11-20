import os, pyautogui
import time, datetime

from open_chrome import open_chrome
from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS
from tutor_py_files import wrappers

SOCIAL = 'FB'

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

def open_browser():
    '''open chrome'''
    driver = open_chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver

def go_to_social_network(driver):
    '''go to social network'''
    driver.get(SOC_NET_LINKS[SOCIAL])

def login(driver):
    '''login'''
    driver.find_element_by_id('email').send_keys(SOC_AUTH_INFO[SOCIAL]['LOGIN'])
    driver.find_element_by_id('pass').send_keys(SOC_AUTH_INFO[SOCIAL]['PASS'])
    driver.find_element_by_id('loginbutton').click()

def get_screen_resolution_size():
    '''get screen resolution size'''
    width_screen, height_screen = pyautogui.size()
    print('width_screen', width_screen)
    print('height_screen', height_screen)
    return width_screen, height_screen

def find_games_top_menu():
    '''find game's top menu'''
    top_menu_location = find_flashing_image('top_menu.png')
    left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = top_menu_location
    return left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu

def scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu):
    print('scroll_to_see_top_menu')
    driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 100))

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


@wrappers.print_time
def choose_nation(REGIONS_ON_WINDOW):
    '''1.choose nation'''
    time.sleep(30)
    pyautogui.moveTo(pyautogui.center(REGIONS_ON_WINDOW['center_mid']), duration=1)
    button_choose_nation = find_flashing_image('button_choose_nation.png',
                                               region=REGIONS_ON_WINDOW['center_down'],
                                               grayscale=True
                                               )
    if button_choose_nation:
        '''1.1 scroll nation right'''
        button_right_arrow_to_choose_nation = find_image('right_arrow_to_choose_nation.png',
                                                         region=REGIONS_ON_WINDOW['right_mid'],
                                                         grayscale=True
                                                         )
        print('button_right_arrow_to_choose_nation', button_right_arrow_to_choose_nation, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
        if button_right_arrow_to_choose_nation:
            for i in range(10):
                time.sleep(2)
                usa_nation = find_image('USA_nation.png',
                                        region=REGIONS_ON_WINDOW['center_down'],
                                        grayscale=True
                                        )
                print('usa_nation', usa_nation, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
                if usa_nation:
                    click_to_center(button_choose_nation)
                    break
                click_to_center(button_right_arrow_to_choose_nation)

        '''1.2 scroll nation left'''
        time.sleep(5)
        button_left_arrow_to_choose_nation = find_image('left_arrow_to_choose_nation.png',
                                                        region=REGIONS_ON_WINDOW['left_mid'],
                                                        grayscale=True
                                                        )
        print('button_left_arrow_to_choose_nation', button_left_arrow_to_choose_nation, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
        if button_left_arrow_to_choose_nation:
            for i in range(10):
                time.sleep(5)
                usa_nation = find_image('USA_nation.png',
                                        region=REGIONS_ON_WINDOW['center_down'],
                                        grayscale=True
                                        )
                print('usa_nation', usa_nation, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
                if usa_nation:
                    click_to_center(button_choose_nation)
                    break
                click_to_center(button_left_arrow_to_choose_nation)

@wrappers.print_time
def first_battle(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN):
    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_full_screen_game'''
    find_flashing_image_and_click('button_full_screen_game.png',
                                  region=REGIONS_ON_WINDOW['right_down'],
                                  grayscale=True
                                  )

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_to_battle'''
    find_flashing_image_and_click('button_to_battle.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_up'],
                                  grayscale=True
                                  )

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_bomb'''
    find_flashing_image_and_click('button_art_bomb.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                  grayscale=True
                                  )

    '''click to area_art_bomb'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=100,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )
    # pyautogui.moveTo(x=AREA_ART_BOMB_COORD['x'], y=AREA_ART_BOMB_COORD['y'], duration=1)
    # pyautogui.click()

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    find_flashing_image_and_click('button_continue.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_down'],
                                  grayscale=True
                                  )

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )



    time.sleep(5)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    find_flashing_image_and_click('button_continue.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_1(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    '''quest №1 "пекарь"'''
    '''find quest_1_icon'''
    find_flashing_image_and_click('quest_1_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    '''find quest_1_2_icon'''
    find_flashing_image_and_click('quest_1_2_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(3)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_2(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №2 "точи пилу"'''
    '''find quest_2_1_icon'''
    find_flashing_image_and_click('quest_2_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    '''find button_store'''
    find_flashing_image_and_click('button_store.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_buy'''
    find_flashing_image_and_click('button_buy.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''click to area build sawmill'''
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=40,
                                  righter_on=10,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    # pyautogui.moveTo(x=AREA_BUILD_SAWMILL_COORD['x'], y=AREA_BUILD_SAWMILL_COORD['y'], duration=1)
    # pyautogui.click()

    time.sleep(3)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_3(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №3 "первые стволы"'''
    '''find quest_3_1_icon'''
    find_flashing_image_and_click('quest_3_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )
    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find building_garrison_icon'''
    find_flashing_image_and_click('building_garrison_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_hire_squad'''
    find_flashing_image_and_click('button_hire_squad.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )
    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)

    # '''find button_speed_up'''
    # find_flashing_image_and_click('button_speed_up.png',
    #                               region=REGIONS_ON_FULL_SCREEN['center_down'],
    #                               grayscale=True
    #                               )

    # time.sleep(2)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_4(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №4 "оборона Клинберга"'''
    '''find quest_4_1_icon'''
    # find_flashing_image_and_click('help_arrow_left.png',
    #                               lefter_on=80,
    #                               region=REGIONS_ON_FULL_SCREEN['left_mid'],
    #                               grayscale=True
    #                               )
    find_flashing_image_and_click('quest_4_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )
    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_campaign'''
    find_flashing_image_and_click('button_campaign.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    find_flashing_image_and_click('campaign_baptism_of_fire .png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(3)
    '''find battle_available'''
    find_flashing_image_and_click('battle_available.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_begin_green'''
    find_flashing_image_and_click('button_begin_green.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(15)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    find_flashing_image_and_click('button_linear_infantry.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(2)
    for i in range(2):
        '''find help_arrow_down'''
        find_flashing_image_and_click('help_arrow_down.png',
                                      lower_on=80,
                                      region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                      grayscale=True
                                      )
        time.sleep(1)

    '''click to button_to_battle'''
    find_flashing_image_and_click('button_to_battle.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_up'],
                                  grayscale=True
                                  )


    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    if find_flashing_image('help_arrow_right.png',
                           region=REGIONS_ON_FULL_SCREEN['right_mid'],
                           grayscale=True
                           ):
        print('way 1')
        '''find button_helth'''
        find_flashing_image_and_click('button_helth.png',
                                      region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                      grayscale=True
                                      )
        time.sleep(1)
        '''click to area_helth'''
        '''find help_arrow_down'''
        find_flashing_image_and_click('help_arrow_down.png',
                                      lower_on=100,
                                      region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                      grayscale=True
                                      )

        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        find_flashing_image_and_click('button_continue.png',
                                      region=REGIONS_ON_FULL_SCREEN['left_down'],
                                      grayscale=True
                                      )
    else:
        print('way 2')
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        find_flashing_image_and_click('button_continue.png',
                                      region=REGIONS_ON_FULL_SCREEN['left_down'],
                                      grayscale=True
                                      )
        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''find button_helth'''
        button_helth = find_flashing_image('button_helth.png',
                                           region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                           grayscale=True)
        if button_helth:
            print('way 2.1')
            click_to_center(button_helth)
            time.sleep(1)
            '''click to area_helth'''
            '''find help_arrow_down'''
            find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=100,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )
        else:
            print('way 2.2')
            help_arrow_right = find_flashing_image('help_arrow_right.png',
                                                   region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                                   grayscale=True
                                                   )
            if help_arrow_right:
                print('way 2.2.1')
                click_to_center(help_arrow_right, righter_on=50)

                time.sleep(1)
                '''click to area_helth'''
                '''find help_arrow_down'''
                find_flashing_image_and_click('help_arrow_down.png',
                                              lower_on=100,
                                              region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                              grayscale=True
                                              )

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    print('''click to quest_4_7_icon''')
    quest_4_7_icon = find_flashing_image('quest_4_7_icon.png',
                                         region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                         grayscale=True)
    if quest_4_7_icon:
        print('quest_4_7_icon is finded')
        click_to_center(quest_4_7_icon)
    else:
        print('quest_4_7_icon is NOT finded')
        find_flashing_image_and_click('help_arrow_down.png',
                                      lower_on=70,
                                      region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                      grayscale=True
                                      )



    # find_flashing_image_and_click('quest_4_7_icon.png',
    #                               region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
    #                               grayscale=True
    #                               )

    time.sleep(2)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )


    time.sleep(15)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(10)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_5(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №5 "Расчистка местности"'''
    '''find quest_5_1_icon'''
    find_flashing_image_and_click('quest_5_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_open'''
    find_flashing_image_and_click('button_open.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_6(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №6 "Укрепрайон"'''
    '''find quest_6_1_icon'''
    find_flashing_image_and_click('quest_6_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_defense'''
    find_flashing_image_and_click('button_defense.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(4)
    '''find quest_6_2_icon'''
    find_flashing_image_and_click('quest_6_2_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_store'''
    find_flashing_image_and_click('button_store.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_buy'''
    find_flashing_image_and_click('button_buy.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    find_flashing_image_and_click('button_continue.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(50)
    pyautogui.moveTo(5, 5, 1)
    '''click to quest_6_3_icon'''
    find_flashing_image_and_click('quest_6_3_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_down'],
                                  grayscale=True
                                  )

    time.sleep(20)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )


    # time.sleep(2)
    # pyautogui.moveTo(5, 5, 1)
    # '''click to button_continue'''
    # find_flashing_image_and_click('button_continue.png',
    #                               region=REGIONS_ON_FULL_SCREEN['center_mid'],
    #                               grayscale=True
    #                               )

@wrappers.print_time
def quest_7(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №7 "Заварушка в лесу"'''
    '''find quest_7_1_icon'''
    find_flashing_image_and_click('quest_7_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_campaign'''
    find_flashing_image_and_click('button_campaign.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    find_flashing_image_and_click('campaign_baptism_of_fire .png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(3)
    '''find battle_available'''
    find_flashing_image_and_click('battle_available.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_begin_green'''
    find_flashing_image_and_click('button_begin_green.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    find_flashing_image_and_click('button_linear_infantry.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )
    time.sleep(1)

    '''click to button_to_battle'''
    find_flashing_image_and_click('button_to_battle.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_up'],
                                  grayscale=True
                                  )

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_strike'''
    find_flashing_image_and_click('button_art_strike.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                  grayscale=True
                                  )


    time.sleep(2)
    '''click to button_art_strike'''
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=85,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(5)
    '''find button_melee'''
    find_flashing_image_and_click('button_melee.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find quest_7_5_icon'''
    quest_7_5_icon = find_flashing_image('quest_7_5_icon.png',
                                         region=REGIONS_ON_FULL_SCREEN['right_down'],
                                         grayscale=True)
    if quest_7_5_icon:
        click_to_center(quest_7_5_icon)
    else:
        find_flashing_image_and_click('quest_7_5_icon.png',
                                      region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                      grayscale=True
                                      )

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    find_flashing_image_and_click('button_linear_infantry.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(5)
    '''find button_volley'''
    find_flashing_image_and_click('button_volley.png',
                                  region=REGIONS_ON_FULL_SCREEN['right_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find quest_7_5_icon'''
    quest_7_5_icon = find_flashing_image('quest_7_5_icon.png',
                                         region=REGIONS_ON_FULL_SCREEN['center_down'],
                                         grayscale=True)
    if quest_7_5_icon:
        click_to_center(quest_7_5_icon)
    else:
        find_flashing_image_and_click('quest_7_5_icon.png',
                                      region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                      grayscale=True
                                      )

    time.sleep(25)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(10)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_8(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №8 "Заряжай"'''
    '''find quest_8_1_icon'''
    find_flashing_image_and_click('quest_8_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find building_garrison_icon'''
    find_flashing_image_and_click('building_garrison_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_hire_squad'''
    find_flashing_image_and_click('button_hire_squad.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)

    # '''find button_speed_up'''
    # find_flashing_image_and_click('button_speed_up.png',
    #                               region=REGIONS_ON_FULL_SCREEN['center_down'],
    #                               grayscale=True
    #                               )

    # time.sleep(2)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_9(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №9 "Добровольцы"'''
    '''find quest_9_1_icon'''
    find_flashing_image_and_click('quest_9_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_store'''
    find_flashing_image_and_click('button_store.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_buy'''
    find_flashing_image_and_click('button_buy.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_down'],
                                  grayscale=True
                                  )

    '''click to area build home'''
    '''find help_arrow_down'''
    find_flashing_image_and_click('help_arrow_down.png',
                                  lower_on=80,
                                  righter_on=10,
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_10(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №10 "Рабочее пространство"'''
    '''find quest_10_1_icon'''
    find_flashing_image_and_click('quest_10_1_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find button_start_mission'''
    find_flashing_image_and_click('button_start_mission.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(1)
    '''find quest_10_2_icon'''
    find_flashing_image_and_click('quest_10_2_icon.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''find button_upgrade'''
    find_flashing_image_and_click('button_upgrade.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )

    time.sleep(2)
    '''click to button_ok'''
    find_flashing_image_and_click('button_ok.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_down'],
                                  grayscale=True
                                  )






# pyautogui.screenshot('full_scteen.png')
# pyautogui.screenshot('left_mid.png', region=REGIONS_ON_WINDOW['left_mid'])
# pyautogui.screenshot('center_mid.png', region=REGIONS_ON_WINDOW['center_mid'])
# pyautogui.screenshot('right_mid.png', region=REGIONS_ON_WINDOW['right_mid'])
# pyautogui.screenshot('center_down.png', region=REGIONS_ON_WINDOW['center_down'])
# pyautogui.screenshot('right_down.png', region=REGIONS_ON_WINDOW['right_down'])
# pyautogui.screenshot('center_up.png', region=REGIONS_ON_FULL_SCREEN['center_up'])
# pyautogui.screenshot('right_mid.png', region=REGIONS_ON_FULL_SCREEN['right_mid'])
# pyautogui.screenshot('left_down.png', region=REGIONS_ON_FULL_SCREEN['left_down'])
# pyautogui.screenshot('center_down.png', region=REGIONS_ON_FULL_SCREEN['center_down'])
# pyautogui.screenshot('center_mid.png', region=REGIONS_ON_FULL_SCREEN['center_mid'])
# pyautogui.alert('end')
# driver.quit()