import pyautogui, time, logging

import browser
from tutor_py_files import wrappers
from tutor_py_files.directories_settings import *


@wrappers.write_log_and_video(videos_dir)
def choose_nation(REGIONS_ON_WINDOW):
    logging.info('''1.choose nation''')
    time.sleep(30)
    pyautogui.moveTo(pyautogui.center(REGIONS_ON_WINDOW['center_mid']), duration=1)
    button_choose_nation = browser.monosearch_1000('button_choose_nation.png',
                                                   samples_dir,
                                                   region=REGIONS_ON_WINDOW['center_down'])
    if button_choose_nation:
        logging.info('''1.1 scroll nation right''')
        button_right_arrow_to_choose_nation = browser.monosearch_1000('right_arrow_to_choose_nation.png',
                                                                      samples_dir,
                                                                      region=REGIONS_ON_WINDOW['right_mid'])
        logging.info('button_right_arrow_to_choose_nation {}'.format(button_right_arrow_to_choose_nation))
        if button_right_arrow_to_choose_nation:
            for i in range(10):
                time.sleep(2)
                usa_nation = browser.monosearch_10('USA_nation.png',
                                                   samples_dir,
                                                   region=REGIONS_ON_WINDOW['center_down'])
                logging.info('usa_nation {}'.format(usa_nation))
                if usa_nation:
                    browser.click_to_center(button_choose_nation)
                    break
                browser.click_to_center(button_right_arrow_to_choose_nation)

        if not usa_nation:
            logging.info('''1.2 scroll nation left''')
            time.sleep(5)
            button_left_arrow_to_choose_nation = browser.monosearch_1000('left_arrow_to_choose_nation.png',
                                                                         samples_dir,
                                                                         region=REGIONS_ON_WINDOW['left_mid'])
            logging.info('button_left_arrow_to_choose_nation {}'.format(button_left_arrow_to_choose_nation))
            if button_left_arrow_to_choose_nation:
                for i in range(10):
                    time.sleep(5)
                    usa_nation = browser.monosearch_10('USA_nation.png',
                                                       samples_dir,
                                                       region=REGIONS_ON_WINDOW['center_down'])
                    logging.info('usa_nation {}'.format(usa_nation))
                    if usa_nation:
                        browser.click_to_center(button_choose_nation)
                        break
                    browser.click_to_center(button_left_arrow_to_choose_nation)
        if not usa_nation:
            logging.error("usa_nation isn't finded")
            pyautogui.alert("{} doesn't find".format('USA_nation.png'))
    else:
        logging.error("button_choose_nation isn't finded")
        pyautogui.alert("{} doesn't find".format('button_choose_nation.png'))

@wrappers.write_log_and_video(videos_dir)
def first_battle(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN):
    # time.sleep(20)

    pyautogui.moveTo(5, 5, 1)
    if browser.monosearch_1000('button_to_battle.png',
                               samples_dir,
                               region=REGIONS_ON_FULL_SCREEN['center_up']):
        '''click to button_full_screen_game'''
        browser.monoregion_multisearch_and_click('button_full_screen_game.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_WINDOW['right_down'])

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_to_battle'''
    browser.monoregion_multisearch_and_click('button_to_battle.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_up'])

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_bomb'''
    browser.monoregion_multisearch_and_click('button_art_bomb.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_mid'])

    '''click to area_art_bomb'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                             lower_on=100,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.monoregion_multisearch_and_click('button_continue.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down'])

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(5)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.monoregion_multisearch_and_click('button_continue.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

@wrappers.write_log_and_video(videos_dir)
def quest_1(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    '''quest №1 "пекарь"'''
    '''find quest_1_icon'''
    browser.monoregion_multisearch_and_click('quest_1_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    '''find quest_1_2_icon'''
    browser.monoregion_multisearch_and_click('quest_1_2_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(3)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_2(REGIONS_ON_FULL_SCREEN):
    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''quest №2 "точи пилу"'''
    '''find quest_2_1_icon'''
    browser.monoregion_multisearch_and_click('quest_2_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    '''find button_store'''
    browser.monoregion_multisearch_and_click('button_store.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(2)
    '''find button_buy'''
    browser.monoregion_multisearch_and_click('button_buy.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    '''click to area build sawmill'''
    '''find and click help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,
                                             lower_on=40,
                                             righter_on=10,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    button_ok = browser.monosearch_10('button_ok.png', samples_dir, region=REGIONS_ON_FULL_SCREEN['center_down'])
    if not button_ok:
        for _ in range(10):
            browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                     samples_dir,
                                                     lower_on=40,
                                                     righter_on=10,
                                                     region=REGIONS_ON_FULL_SCREEN['center_mid'])
            time.sleep(2)
            button_ok = browser.monosearch_10('button_ok.png', samples_dir,
                                              region=REGIONS_ON_FULL_SCREEN['center_down'])
            if button_ok:
                '''click to button_ok'''
                browser.click_to_center(button_ok)
                break
    else:
        browser.click_to_center(button_ok)

@wrappers.write_log_and_video(videos_dir)
def quest_3(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №3 "первые стволы"'''
    '''find quest_3_1_icon'''
    browser.monoregion_multisearch_and_click('quest_3_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])
    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    '''find building_garrison_icon'''
    browser.monoregion_multisearch_and_click('building_garrison_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(1)
    '''find button_hire_squad'''
    browser.monoregion_multisearch_and_click('button_hire_squad.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])
    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)

    time.sleep(2)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_4(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №4 "оборона Клинберга"'''
    '''find quest_4_1_icon'''
    browser.monoregion_multisearch_and_click('quest_4_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])
    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find button_campaign'''
    browser.monoregion_multisearch_and_click('button_campaign.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_down_menu'])

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    browser.monoregion_multisearch_and_click('campaign_baptism_of_fire .png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(3)
    '''find battle_available'''
    browser.monoregion_multisearch_and_click('battle_available.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down'])

    time.sleep(2)
    '''find button_begin_green'''
    browser.monoregion_multisearch_and_click('button_begin_green.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(15)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.monoregion_multisearch_and_click('button_linear_infantry.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(2)
    for i in range(2):
        '''find help_arrow_down'''
        browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                 samples_dir,

                                              lower_on=80,
                                              region=REGIONS_ON_FULL_SCREEN['center_mid'])
        time.sleep(1)

    '''click to button_to_battle'''
    browser.monoregion_multisearch_and_click('button_to_battle.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_up'])


    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    if browser.monosearch_1000('help_arrow_right.png',
                               samples_dir,
                               region=REGIONS_ON_FULL_SCREEN['right_mid']):
        logging.info('way 1')
        '''find button_helth'''
        browser.monoregion_multisearch_and_click('button_helth.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['right_mid'])
        time.sleep(1)
        '''click to area_helth'''
        '''find help_arrow_down'''
        browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                 samples_dir,
                                                 lower_on=100,
                                                 region=REGIONS_ON_FULL_SCREEN['center_mid'])

        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        browser.monoregion_multisearch_and_click('button_continue.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['left_down'])
    else:
        logging.info('way 2')
        pyautogui.moveTo(5, 5, 1)
        '''click to button_continue'''
        browser.monoregion_multisearch_and_click('button_continue.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['left_down'])
        time.sleep(20)
        pyautogui.moveTo(5, 5, 1)
        '''find button_helth'''
        button_helth = browser.monosearch_1000('button_helth.png',
                                               samples_dir,
                                               region=REGIONS_ON_FULL_SCREEN['right_mid'])
        if button_helth:
            logging.info('way 2.1')
            browser.click_to_center(button_helth)
            time.sleep(1)
            '''click to area_helth'''
            '''find help_arrow_down'''
            browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                     samples_dir,
                                                     lower_on=100,
                                                     region=REGIONS_ON_FULL_SCREEN['center_mid'])
        else:
            logging.info('way 2.2')
            help_arrow_right = browser.monosearch_1000('help_arrow_right.png',
                                                       samples_dir,
                                                       region=REGIONS_ON_FULL_SCREEN['right_mid'])
            if help_arrow_right:
                logging.info('way 2.2.1')
                browser.click_to_center(help_arrow_right, righter_on=50)

                time.sleep(1)
                help_arrow_down = browser.monosearch_1000('help_arrow_down.png',
                                                          samples_dir,
                                                          region=REGIONS_ON_FULL_SCREEN['center_mid'])
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
    quest_4_7_icon = browser.monosearch_1000('quest_4_7_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])
    if quest_4_7_icon:
        logging.info('quest_4_7_icon is finded')
        browser.click_to_center(quest_4_7_icon)
        time.sleep(2)
        '''find help_arrow_down'''
        browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                 samples_dir,
                                                 lower_on=80,
                                                 region=REGIONS_ON_FULL_SCREEN['center_mid'])
    else:
        logging.info('quest_4_7_icon is NOT finded')
        help_arrow_down = browser.monosearch_1000('help_arrow_down.png',
                                                  samples_dir,
                                                  region=REGIONS_ON_FULL_SCREEN['center_down_menu'])
        if help_arrow_down:
            browser.click_to_center(help_arrow_down, lower_on=70)
            time.sleep(2)
            '''find help_arrow_down'''
            browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                                     samples_dir,
                                                     lower_on=80,
                                                     region=REGIONS_ON_FULL_SCREEN['center_mid'])
    time.sleep(15)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])
    time.sleep(10)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_5(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №5 "Расчистка местности"'''
    '''find quest_5_1_icon'''
    browser.monoregion_multisearch_and_click('quest_5_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])
    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])
    time.sleep(2)
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,
                                             lower_on=80,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])
    time.sleep(2)
    '''find button_open'''
    button_open = browser.monoregion_multisearch('button_open.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['center_down'])
    if button_open:
        browser.click_to_center(button_open)
    else:
        browser.monoregion_multisearch_and_click('button_open_bug_quest_5.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_6(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №6 "Укрепрайон"'''
    '''find quest_6_1_icon'''
    browser.monoregion_multisearch_and_click('quest_6_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find button_defense'''
    browser.monoregion_multisearch_and_click('button_defense.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down_menu'])

    time.sleep(4)
    '''find quest_6_2_icon'''
    browser.monoregion_multisearch_and_click('quest_6_2_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(1)
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid']
                                          )

    time.sleep(1)
    '''find button_store'''
    browser.monoregion_multisearch_and_click('button_store.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_down_menu'])

    time.sleep(2)
    '''find button_buy'''
    browser.monoregion_multisearch_and_click('button_buy.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid']
                                          )

    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.monoregion_multisearch_and_click('button_continue.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(50)
    pyautogui.moveTo(5, 5, 1)
    '''click to quest_6_3_icon'''
    browser.monoregion_multisearch_and_click('quest_6_3_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down'])

    time.sleep(20)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])


    time.sleep(2)
    pyautogui.moveTo(5, 5, 1)
    '''click to button_continue'''
    browser.monoregion_multisearch_and_click('button_continue.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

@wrappers.write_log_and_video(videos_dir)
def quest_7(REGIONS_ON_FULL_SCREEN):
    # print(browser.monosearch_1000('10.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['right_up_menu']))

    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №7 "Заварушка в лесу"'''
    '''find quest_7_1_icon'''
    browser.monoregion_multisearch_and_click('quest_7_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(2)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find button_campaign'''
    browser.monoregion_multisearch_and_click('button_campaign.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_down_menu'])

    time.sleep(3)
    '''find campaign_baptism_of_fire'''
    browser.monoregion_multisearch_and_click('campaign_baptism_of_fire .png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(3)
    '''find battle_available'''
    browser.monoregion_multisearch_and_click('battle_available.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    '''find button_begin_green'''
    browser.monoregion_multisearch_and_click('button_begin_green.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(10)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.monoregion_multisearch_and_click('button_linear_infantry.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(2)
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,
                                             lower_on=80,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid']
                                             )

    time.sleep(1)
    '''click to button_to_battle'''
    browser.monoregion_multisearch_and_click('button_to_battle.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_up'])

    time.sleep(35)
    pyautogui.moveTo(5, 5, 1)
    '''find button_art_strike'''
    browser.monoregion_multisearch_and_click('button_art_strike.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_mid'])


    time.sleep(2)
    '''click to button_art_strike'''
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                             lower_on=85,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid']
                                             )

    time.sleep(5)
    '''find button_melee'''
    browser.monoregion_multisearch_and_click('button_melee.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_mid'])

    time.sleep(1)
    '''find quest_7_5_icon'''
    browser.multiregion_monosearch_and_click('quest_7_5_icon.png',
                                             samples_dir,
                                             REGIONS_ON_FULL_SCREEN)

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)
    '''find button_linear_infantry'''
    browser.monoregion_multisearch_and_click('button_linear_infantry.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(1)
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                          lower_on=80,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid'],
                                          )

    time.sleep(5)
    '''find button_volley'''
    browser.monoregion_multisearch_and_click('button_volley.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_down'])

    time.sleep(1)
    '''find quest_7_5_icon'''
    browser.multiregion_monosearch_and_click('quest_7_5_icon.png',
                                             samples_dir,
                                             REGIONS_ON_FULL_SCREEN)

    time.sleep(25)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(10)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_8(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №8 "Заряжай"'''
    '''find quest_8_1_icon'''
    browser.monoregion_multisearch_and_click('quest_8_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(1)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find building_garrison_icon'''
    browser.monoregion_multisearch_and_click('building_garrison_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(1)
    '''find button_hire_squad'''
    browser.monoregion_multisearch_and_click('button_hire_squad.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(20)
    pyautogui.moveTo(5, 5, 1)

    time.sleep(2)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_9(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №9 "Добровольцы"'''
    '''find quest_9_1_icon'''
    browser.monoregion_multisearch_and_click('quest_9_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(1)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find button_store'''
    browser.monoregion_multisearch_and_click('button_store.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(2)
    '''find button_buy'''
    browser.monoregion_multisearch_and_click('button_buy.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down'])

    '''click to area build home'''
    '''find help_arrow_down'''
    browser.monoregion_multisearch_and_click('help_arrow_down.png',
                                             samples_dir,

                                          lower_on=80,
                                          righter_on=10,
                                          region=REGIONS_ON_FULL_SCREEN['center_mid']
                                          )

    time.sleep(10)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_10(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №10 "Рабочее пространство"'''
    '''find quest_10_1_icon'''
    browser.monoregion_multisearch_and_click('quest_10_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(1)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find quest_10_2_icon'''
    browser.monoregion_multisearch_and_click('quest_10_2_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_mid'])

    time.sleep(2)
    '''find button_upgrade'''
    browser.monoregion_multisearch_and_click('button_upgrade.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(2)
    '''click to button_ok'''
    browser.monoregion_multisearch_and_click('button_ok.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_11(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №11 "Альма-матер"'''
    '''find quest_11_1_icon'''
    browser.monoregion_multisearch_and_click('quest_11_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(1)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find quest_11_2_icon'''
    browser.monoregion_multisearch_and_click('button_buy.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_down'])

    time.sleep(2)
    '''find Town hall'''
    quest_11_2_icon = browser.multiregion_monosearch('quest_11_2_icon.png',
                                                     samples_dir,
                                                     REGIONS_ON_FULL_SCREEN)
    '''put Academy on free space'''
    browser.click_to_center(quest_11_2_icon, righter_on=200, lower_on=30)
    time.sleep(3)
    if not browser.monosearch_10('button_ok.png', samples_dir, region=REGIONS_ON_FULL_SCREEN['center_down']):
        for pix in range(1,100,10):
            browser.click_to_center(quest_11_2_icon, righter_on=200+pix, lower_on=30)
            time.sleep(3)
            button_ok = browser.monosearch_10('button_ok.png', samples_dir, region=REGIONS_ON_FULL_SCREEN['center_down'])
            if button_ok:
                '''click to button_ok'''
                browser.click_to_center(button_ok)
                break
    else:
        browser.monoregion_multisearch_and_click('button_ok.png', samples_dir, region=REGIONS_ON_FULL_SCREEN['center_down'])

@wrappers.write_log_and_video(videos_dir)
def quest_12(REGIONS_ON_FULL_SCREEN):
    time.sleep(1)
    pyautogui.moveTo(5, 5, 1)
    '''quest №12 "Полевая наука"'''
    '''find quest_12_1_icon'''
    browser.monoregion_multisearch_and_click('quest_12_1_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['left_mid'])

    time.sleep(1)
    '''find button_start_mission'''
    browser.monoregion_multisearch_and_click('button_start_mission.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(1)
    '''find button_technologies'''
    browser.monoregion_multisearch_and_click('button_technologies.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down_menu'])

    time.sleep(1)
    '''find quest_12_2_icon'''
    browser.multiregion_monosearch_and_click('quest_12_2_icon.png',
                                             samples_dir,
                                             regions=REGIONS_ON_FULL_SCREEN)

    time.sleep(1)
    '''find quest_12_3_icon'''
    browser.monoregion_multisearch_and_click('quest_12_3_icon.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['center_down'])

    time.sleep(3)
    '''click to button_ok'''
    for _ in range(2):
        browser.monoregion_multisearch_and_click('button_ok.png',
                                                 samples_dir,
                                                 region=REGIONS_ON_FULL_SCREEN['center_down'])
        time.sleep(1)

    time.sleep(1)
    '''find button_close_window'''
    browser.monoregion_multisearch_and_click('button_close_window.png',
                                             samples_dir,
                                             region=REGIONS_ON_FULL_SCREEN['right_up'])























# pyautogui.screenshot('full_scteen.png')
# pyautogui.screenshot('left_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['left_mid'])
# pyautogui.screenshot('center_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['center_mid'])
# pyautogui.screenshot('right_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['right_mid'])
# pyautogui.screenshot('center_down.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['center_down'])
# pyautogui.screenshot('right_down.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['right_down'])
# pyautogui.screenshot('center_up.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_up'])
# pyautogui.screenshot('right_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['right_mid'])
# pyautogui.screenshot('left_down.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['left_down'])
# pyautogui.screenshot('center_down.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_down'])
# pyautogui.screenshot('center_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_mid'])
# pyautogui.alert('end')
# driver.quit()




































# pyautogui.screenshot('full_scteen.png')
# pyautogui.screenshot('left_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['left_mid'])
# pyautogui.screenshot('center_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['center_mid'])
# pyautogui.screenshot('right_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['right_mid'])
# pyautogui.screenshot('center_down.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['center_down'])
# pyautogui.screenshot('right_down.png',
    # samples_dir,
    #  region=REGIONS_ON_WINDOW['right_down'])
# pyautogui.screenshot('center_up.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_up'])
# pyautogui.screenshot('right_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['right_mid'])
# pyautogui.screenshot('left_down.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['left_down'])
# pyautogui.screenshot('center_down.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_down'])
# pyautogui.screenshot('center_mid.png',
    # samples_dir,
    #  region=REGIONS_ON_FULL_SCREEN['center_mid'])
# pyautogui.alert('end')
# driver.quit()