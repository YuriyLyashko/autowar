import datetime, time

import tutor, wipe_user_progress

from tutor_py_files import regions
from authentication_info import ADMIN_LOGIN, ADMIN_PASS, SOC_AUTH_INFO, SOC_NET_LINKS

SOCIAL = 'FB'  # 'VK', 'FB'
SERVER = 'FB'  # 'DM', 'FB'
ID = SOC_AUTH_INFO[SOCIAL]['ID']


n = 1
while True:
    start_time = datetime.datetime.now()
    print('\n\n\n          launch №', n)
    print('start_time', start_time.strftime('%d/%m/%Y %H:%M:%S'))


    wipe_user_progress.wipe(SOCIAL, SERVER, ID)
    driver = tutor.open_browser()
    tutor.go_to_social_network(driver)
    tutor.login(driver)
    tutor.go_to_social_network(driver)
    width_screen, height_screen = tutor.get_screen_resolution_size()
    left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = tutor.find_games_top_menu()
    REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN = regions.get_regions(left_coord_top_menu,
                                                                    width_top_menu,
                                                                    height_screen,
                                                                    width_screen
                                                                    )
    tutor.scroll_down(driver, left_coord_top_menu, top_coord_top_menu)
    tutor.click_to_game_area(width_top_menu, left_coord_top_menu, top_coord_top_menu, height_screen)
    tutor.accept_flash_running()


    # time.sleep(30)
    # tutor.scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu)
    # tutor.set_full_screen(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN)


    tutor.choose_nation(REGIONS_ON_WINDOW)
    tutor.first_battle(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN)
    tutor.quest_1(REGIONS_ON_FULL_SCREEN)
    tutor.quest_2(REGIONS_ON_FULL_SCREEN)
    tutor.quest_3(REGIONS_ON_FULL_SCREEN)
    tutor.quest_4(REGIONS_ON_FULL_SCREEN)
    tutor.quest_5(REGIONS_ON_FULL_SCREEN)
    tutor.quest_6(REGIONS_ON_FULL_SCREEN)



    driver.quit()
    finish_time = datetime.datetime.now()
    print('finish_time', finish_time.strftime('%d/%m/%Y %H:%M:%S'))
    time_spent = finish_time - start_time
    print('time_spent', time_spent)
    n+=1
