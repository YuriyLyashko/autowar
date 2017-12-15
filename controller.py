if __name__ == '__main__':
    import datetime, time, logging

    import browser, tutor, wipe_user_progress

    from tutor_py_files import regions, log_config
    from authentication_info import ADMIN_LOGIN, ADMIN_PASS, SOC_AUTH_INFO, SOC_NET_LINKS

    SOCIAL = 'FB'  # 'VK', 'FB'
    SERVER = 'FB'  # 'DM', 'FB'
    ID = SOC_AUTH_INFO[SOCIAL]['ID']




    n = 1
    while True:
        start_time = datetime.datetime.now()
        logging.info('\n\n\n          launch {}'.format(n))
        logging.info('start')


        # wipe_user_progress.wipe(SOCIAL, SERVER, ID)
        driver = browser.open_browser()
        browser.go_to_social_network(driver, SOC_NET_LINKS[SOCIAL])
        browser.login(driver, SOC_AUTH_INFO[SOCIAL]['LOGIN'], SOC_AUTH_INFO[SOCIAL]['PASS'])
        browser.go_to_social_network(driver, SOC_NET_LINKS[SOCIAL])
        width_screen, height_screen = browser.get_screen_resolution_size()
        left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = browser.persistent_search('top_menu.png')
        REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN = regions.get_regions(left_coord_top_menu,
                                                                        width_top_menu,
                                                                        height_screen,
                                                                        width_screen
                                                                        )
        browser.scroll_down(driver, left_coord_top_menu, top_coord_top_menu)
        browser.click_to_game_area(width_top_menu, left_coord_top_menu, top_coord_top_menu, height_screen)
        browser.accept_flash_running(REGIONS_ON_FULL_SCREEN['left_up'])


        time.sleep(30)
        browser.scroll_to_see_top_menu(driver, left_coord_top_menu, top_coord_top_menu)
        browser.set_full_screen(REGIONS_ON_WINDOW)


        # tutor.choose_nation(REGIONS_ON_WINDOW)
        # tutor.first_battle(REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN)
        # tutor.quest_1(REGIONS_ON_FULL_SCREEN)
        # tutor.quest_2(REGIONS_ON_FULL_SCREEN)
        # tutor.quest_3(REGIONS_ON_FULL_SCREEN)
        # tutor.quest_4(REGIONS_ON_FULL_SCREEN)
        # tutor.quest_5(REGIONS_ON_FULL_SCREEN)
        # tutor.quest_6(REGIONS_ON_FULL_SCREEN)
        tutor.quest_7(REGIONS_ON_FULL_SCREEN)
        tutor.quest_8(REGIONS_ON_FULL_SCREEN)
        tutor.quest_9(REGIONS_ON_FULL_SCREEN)
        tutor.quest_10(REGIONS_ON_FULL_SCREEN)



        driver.quit()
        finish_time = datetime.datetime.now()
        logging.info('finish')
        time_spent = finish_time - start_time
        logging.info('time_spent {}'.format(time_spent))
        time.sleep(5)
        # times.append(time_spent)
        # logging.info('average time: {}'.format(sum(times)/len(times)))

        n+=1
