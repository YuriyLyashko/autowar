import pyautogui, time, datetime, logging

import browser
from tutor_py_files import wrappers



@wrappers.print_time
def choose_nation(REGIONS_ON_WINDOW):
    logging.info('''1.choose nation''')
    time.sleep(30)
    pyautogui.moveTo(pyautogui.center(REGIONS_ON_WINDOW['center_mid']), duration=1)
    button_choose_nation = browser.find_flashing_image('button_choose_nation.png',
                                                       region=REGIONS_ON_WINDOW['center_down'],
                                                       grayscale=True
                                                       )
    if button_choose_nation:
        logging.info('''1.1 scroll nation right''')
        button_right_arrow_to_choose_nation = browser.find_image('right_arrow_to_choose_nation.png',
                                                                 region=REGIONS_ON_WINDOW['right_mid'],
                                                                 grayscale=True
                                                                 )
        logging.info('button_right_arrow_to_choose_nation {}'.format(button_right_arrow_to_choose_nation))
        if button_right_arrow_to_choose_nation:
            for i in range(10):
                time.sleep(2)
                usa_nation = browser.find_image('USA_nation.png',
                                                region=REGIONS_ON_WINDOW['center_down'],
                                                grayscale=True
                                                )
                logging.info('usa_nation {}'.format(usa_nation))
                if usa_nation:
                    browser.click_to_center(button_choose_nation)
                    break
                browser.click_to_center(button_right_arrow_to_choose_nation)

        logging.info('''1.2 scroll nation left''')
        time.sleep(5)
        button_left_arrow_to_choose_nation = browser.find_image('left_arrow_to_choose_nation.png',
                                                                region=REGIONS_ON_WINDOW['left_mid'],
                                                                grayscale=True
                                                                )
        logging.info('button_left_arrow_to_choose_nation {}'.format(button_left_arrow_to_choose_nation))
        if button_left_arrow_to_choose_nation:
            for i in range(10):
                time.sleep(5)
                usa_nation = browser.find_image('USA_nation.png',
                                                region=REGIONS_ON_WINDOW['center_down'],
                                                grayscale=True
                                                )
                logging.info('usa_nation {}'.format(usa_nation))
                if usa_nation:
                    browser.click_to_center(button_choose_nation)
                    break
                browser.click_to_center(button_left_arrow_to_choose_nation)

@wrappers.print_time
def first_battle(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN):
    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_full_screen_game'''
    browser.find_flashing_image_and_click('button_full_screen_game.png',
                                          region=REGIONS_ON_WINDOW['right_down'],
                                          grayscale=True
                                          )

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_to_battle'''
    browser.find_flashing_image_and_click('button_to_battle.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_up'],
                                          grayscale=True
                                          )

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_bomb'''
    browser.find_flashing_image_and_click('button_art_bomb.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                          grayscale=True
                                          )

    '''click to area_art_bomb'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=100,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )
    # pyautogui.moveTo(x=AREA_ART_BOMB_COORD['x'], y=AREA_ART_BOMB_COORD['y'], duration=1)
    # pyautogui.click()

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.find_flashing_image_and_click('button_continue.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_down'],
                                          grayscale=True
                                          )

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )



    time.sleep(5)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.find_flashing_image_and_click('button_continue.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_1(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    '''quest №1 "пекарь"'''
    '''find quest_1_icon'''
    browser.find_flashing_image_and_click('quest_1_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    '''find quest_1_2_icon'''
    browser.find_flashing_image_and_click('quest_1_2_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(3)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_2(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №2 "точи пилу"'''
    '''find quest_2_1_icon'''
    browser.find_flashing_image_and_click('quest_2_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    '''find button_store'''
    browser.find_flashing_image_and_click('button_store.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_buy'''
    browser.find_flashing_image_and_click('button_buy.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''click to area build sawmill'''
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=40,
                                          righter_on=10,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    # pyautogui.moveTo(x=AREA_BUILD_SAWMILL_COORD['x'], y=AREA_BUILD_SAWMILL_COORD['y'], duration=1)
    # pyautogui.click()

    time.sleep(3)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_3(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №3 "первые стволы"'''
    '''find quest_3_1_icon'''
    browser.find_flashing_image_and_click('quest_3_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )
    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find building_garrison_icon'''
    browser.find_flashing_image_and_click('building_garrison_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_hire_squad'''
    browser.find_flashing_image_and_click('button_hire_squad.png',
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
    browser.find_flashing_image_and_click('button_ok.png',
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
    browser.find_flashing_image_and_click('quest_4_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )
    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_campaign'''
    browser.find_flashing_image_and_click('button_campaign.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    browser.find_flashing_image_and_click('campaign_baptism_of_fire .png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(3)
    '''find battle_available'''
    browser.find_flashing_image_and_click('battle_available.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_begin_green'''
    browser.find_flashing_image_and_click('button_begin_green.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(15)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.find_flashing_image_and_click('button_linear_infantry.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(2)
    for i in range(2):
        '''find help_arrow_down'''
        browser.find_flashing_image_and_click('help_arrow_down.png',
                                              lower_on=80,
                                              region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                              grayscale=True
                                              )
        time.sleep(1)

    '''click to button_to_battle'''
    browser.find_flashing_image_and_click('button_to_battle.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_up'],
                                          grayscale=True
                                          )


    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    if browser.find_flashing_image('help_arrow_right.png',
                                   region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                   grayscale=True
                                   ):
        logging.info('way 1')
        '''find button_helth'''
        browser.find_flashing_image_and_click('button_helth.png',
                                              region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                              grayscale=True
                                              )
        time.sleep(1)
        '''click to area_helth'''
        '''find help_arrow_down'''
        browser.find_flashing_image_and_click('help_arrow_down.png',
                                              lower_on=100,
                                              region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                              grayscale=True
                                              )

        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        browser.find_flashing_image_and_click('button_continue.png',
                                              region=REGIONS_ON_FULL_SCREEN['left_down'],
                                              grayscale=True
                                              )
    else:
        logging.info('way 2')
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        browser.find_flashing_image_and_click('button_continue.png',
                                              region=REGIONS_ON_FULL_SCREEN['left_down'],
                                              grayscale=True
                                              )
        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''find button_helth'''
        button_helth = browser.find_flashing_image('button_helth.png',
                                                   region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                                   grayscale=True
                                                   )
        if button_helth:
            logging.info('way 2.1')
            browser.click_to_center(button_helth)
            time.sleep(1)
            '''click to area_helth'''
            '''find help_arrow_down'''
            browser.find_flashing_image_and_click('help_arrow_down.png',
                                                  lower_on=100,
                                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                                  grayscale=True
                                                  )
        else:
            logging.info('way 2.2')
            help_arrow_right = browser.find_flashing_image('help_arrow_right.png',
                                                           region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                                           grayscale=True
                                                           )
            if help_arrow_right:
                logging.info('way 2.2.1')
                browser.click_to_center(help_arrow_right, righter_on=50)

                time.sleep(1)
                help_arrow_down = browser.find_flashing_image('help_arrow_down.png',
                                                              region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                                              grayscale=True
                                                              )
                if help_arrow_down:
                    logging.info('way 2.2.1.1')
                    '''click to area_helth'''
                    '''find help_arrow_down'''
                    browser.click_to_center(help_arrow_down, lower_on=100)
                else:
                    logging.info('area_helth help_arrow_down is NOT finded')

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to quest_4_7_icon'''
    quest_4_7_icon = browser.find_flashing_image('quest_4_7_icon.png',
                                                 region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                                 grayscale=True
                                                 )
    if quest_4_7_icon:
        logging.info('quest_4_7_icon is finded')
        browser.click_to_center(quest_4_7_icon)
        time.sleep(2)
        '''find help_arrow_down'''
        browser.find_flashing_image_and_click('help_arrow_down.png',
                                              lower_on=80,
                                              region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                              grayscale=True
                                              )
    else:
        logging.info('quest_4_7_icon is NOT finded')
        help_arrow_down = browser.find_flashing_image('help_arrow_down.png',
                                                      region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                                      grayscale=True
                                                      )
        if help_arrow_down:
            browser.click_to_center(help_arrow_down, lower_on=70)
            time.sleep(2)
            '''find help_arrow_down'''
            browser.find_flashing_image_and_click('help_arrow_down.png',
                                                  lower_on=80,
                                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                                  grayscale=True
                                                  )


    time.sleep(15)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(10)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_5(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №5 "Расчистка местности"'''
    '''find quest_5_1_icon'''
    browser.find_flashing_image_and_click('quest_5_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_open'''
    browser.find_flashing_image_and_click('button_open.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_6(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №6 "Укрепрайон"'''
    '''find quest_6_1_icon'''
    browser.find_flashing_image_and_click('quest_6_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_defense'''
    browser.find_flashing_image_and_click('button_defense.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(4)
    '''find quest_6_2_icon'''
    browser.find_flashing_image_and_click('quest_6_2_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_store'''
    browser.find_flashing_image_and_click('button_store.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_buy'''
    browser.find_flashing_image_and_click('button_buy.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.find_flashing_image_and_click('button_continue.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(50)
    pyautogui.moveTo(5, 5, 1)
    '''click to quest_6_3_icon'''
    browser.find_flashing_image_and_click('quest_6_3_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_down'],
                                          grayscale=True
                                          )

    time.sleep(20)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )


    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.find_flashing_image_and_click('button_continue.png',
                                  region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                  grayscale=True
                                  )

@wrappers.print_time
def quest_7(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №7 "Заварушка в лесу"'''
    '''find quest_7_1_icon'''
    browser.find_flashing_image_and_click('quest_7_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_campaign'''
    browser.find_flashing_image_and_click('button_campaign.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    browser.find_flashing_image_and_click('campaign_baptism_of_fire .png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(3)
    '''find battle_available'''
    browser.find_flashing_image_and_click('battle_available.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_begin_green'''
    browser.find_flashing_image_and_click('button_begin_green.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.find_flashing_image_and_click('button_linear_infantry.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )
    time.sleep(1)

    '''click to button_to_battle'''
    browser.find_flashing_image_and_click('button_to_battle.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_up'],
                                          grayscale=True
                                          )

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_strike'''
    browser.find_flashing_image_and_click('button_art_strike.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                          grayscale=True
                                          )


    time.sleep(2)
    '''click to button_art_strike'''
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=85,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(5)
    '''find button_melee'''
    browser.find_flashing_image_and_click('button_melee.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find quest_7_5_icon'''
    for region in ('left_up', 'center_mid', 'right_down'):
        quest_7_5_icon = browser.find_flashing_image('quest_7_5_icon.png',
                                                     region=REGIONS_ON_FULL_SCREEN[region],
                                                     grayscale=True
                                                     )
        if quest_7_5_icon:
            browser.click_to_center(quest_7_5_icon)
            break



    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.find_flashing_image_and_click('button_linear_infantry.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(5)
    '''find button_volley'''
    browser.find_flashing_image_and_click('button_volley.png',
                                          region=REGIONS_ON_FULL_SCREEN['right_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find quest_7_5_icon'''
    for region in ('center_down', 'center_mid', 'leftt_down'):
        quest_7_5_icon = browser.find_flashing_image('quest_7_5_icon.png',
                                                     region=REGIONS_ON_FULL_SCREEN[region],
                                                     grayscale=True
                                                     )
        if quest_7_5_icon:
            browser.click_to_center(quest_7_5_icon)
            break

    time.sleep(25)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(10)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_8(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №8 "Заряжай"'''
    '''find quest_8_1_icon'''
    browser.find_flashing_image_and_click('quest_8_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find building_garrison_icon'''
    browser.find_flashing_image_and_click('building_garrison_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_hire_squad'''
    browser.find_flashing_image_and_click('button_hire_squad.png',
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
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_9(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №9 "Добровольцы"'''
    '''find quest_9_1_icon'''
    browser.find_flashing_image_and_click('quest_9_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_store'''
    browser.find_flashing_image_and_click('button_store.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down_menu'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_buy'''
    browser.find_flashing_image_and_click('button_buy.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_down'],
                                          grayscale=True
                                          )

    '''click to area build home'''
    '''find help_arrow_down'''
    browser.find_flashing_image_and_click('help_arrow_down.png',
                                          lower_on=80,
                                          righter_on=10,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(10)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

@wrappers.print_time
def quest_10(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №10 "Рабочее пространство"'''
    '''find quest_10_1_icon'''
    browser.find_flashing_image_and_click('quest_10_1_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['left_mid'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find button_start_mission'''
    browser.find_flashing_image_and_click('button_start_mission.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(1)
    '''find quest_10_2_icon'''
    browser.find_flashing_image_and_click('quest_10_2_icon.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''find button_upgrade'''
    browser.find_flashing_image_and_click('button_upgrade.png',
                                          region=REGIONS_ON_FULL_SCREEN['center_down'],
                                          grayscale=True
                                          )

    time.sleep(2)
    '''click to button_ok'''
    browser.find_flashing_image_and_click('button_ok.png',
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