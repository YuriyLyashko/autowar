import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner

import browser, dump_loader


from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS
from tutor_py_files import wrappers
from tutor_py_files import regions
from locales_py_files.directories_settings import *


SOCIAL = 'FB'
SERVER = 'FB'


class LocalesTests(unittest.TestCase):
    @wrappers.write_log_and_video(videos_dir)
    def setUp(self):
        dump_loader.load_max_lvl_dump(SOCIAL, SERVER, SOC_AUTH_INFO[SOCIAL]['ID'])
        ''''''
        '''ignore insides warnings'''
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

        '''open chrome'''
        self.driver = browser.open_browser()

        '''go to social network'''
        browser.go_to_social_network(self.driver, SOC_NET_LINKS[SOCIAL])

        '''login'''
        browser.login(self.driver, SOC_AUTH_INFO[SOCIAL]['LOGIN'], SOC_AUTH_INFO[SOCIAL]['PASS'])

        '''go to game page'''
        browser.go_to_social_network(self.driver, SOC_NET_LINKS['{}_game'.format(SOCIAL)])

        '''get screen resolution size'''
        self.width_screen, self.height_screen = pyautogui.size()

        '''find game's top menu'''
        self.left_coord_top_menu, self.top_coord_top_menu, self.width_top_menu, self.height_top_menu = \
            browser.monosearch_1000('top_menu.png', samples_dir)

        '''scroll down'''
        self.driver.execute_script('scroll({},{});'.format(self.left_coord_top_menu, self.top_coord_top_menu - 150))

        '''click to game area'''
        time.sleep(1)
        pyautogui.click(x=self.width_top_menu - self.left_coord_top_menu, y=self.top_coord_top_menu + self.height_screen / 2)

        '''accept flash running'''
        time.sleep(0.5)
        button_accept_flash_running = browser.monosearch_10('accept_flash_running.png', samples_dir)
        if button_accept_flash_running:
            button_accept_flash_running_x, button_accept_flash_running_y = pyautogui.center(button_accept_flash_running)
            pyautogui.click(x=button_accept_flash_running_x, y=button_accept_flash_running_y)
        self.REGIONS_ON_WINDOW, self.REGIONS_ON_FULL_SCREEN = regions.get_regions(self.left_coord_top_menu,
                                                                                  self.width_top_menu,
                                                                                  self.height_screen,
                                                                                  self.width_screen
                                                                                  )
        time.sleep(40)

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip('I skip it')
    @wrappers.write_log_and_video(videos_dir)
    def test_ru_button_tips_locale(self):
        ''''''
        pyautogui.moveTo(5, 5, 1)
        '''choose language'''

        if not browser.monosearch_10('ru_language_selected.png', samples_dir):
            browser.change_lanuage('ru_language_selected.png', samples_dir)
            time.sleep(40)

        pyautogui.moveTo(5, 5, 1)
        '''close_all_bonus_windows'''
        browser.close_all_bonus_windows(samples_dir,
                                        self.driver,
                                        self.height_screen,
                                        self.left_coord_top_menu,
                                        self.top_coord_top_menu
                                        )

        '''set_full_screen'''
        browser.set_full_screen(samples_dir, self.REGIONS_ON_WINDOW)

        '''get lists of buttons and locales'''
        self.buttons = os.listdir('{}{}'.format(os.getcwd(), ru_buttons_dir))
        self.locales = os.listdir('{}{}'.format(os.getcwd(), ru_locales_dir))

        '''check locales when focus to buttons'''
        for button, locale in zip(self.buttons, self.locales):
            button_coord = browser.monosearch_10(button, ru_buttons_dir)
            with self.subTest():
                self.assertTrue(button_coord, msg="{} not finded".format(button))
            if button_coord:
                browser.move_mouse_to(button_coord)
                with self.subTest():
                    self.assertTrue(browser.monosearch_10(locale, ru_locales_dir), msg="{} not finded".format(locale))

    # @unittest.skip('I skip it')
    @wrappers.write_log_and_video(videos_dir)
    def test_en_button_tips_locale(self):
        ''''''
        pyautogui.moveTo(5, 5, 1)
        '''choose language'''

        if not browser.monosearch_10('en_language_selected.png', samples_dir):
            browser.change_lanuage('en_language_selected.png', samples_dir)
            time.sleep(40)

        pyautogui.moveTo(5, 5, 1)
        '''close_all_bonus_windows'''
        browser.close_all_bonus_windows(samples_dir,
                                        self.driver,
                                        self.height_screen,
                                        self.left_coord_top_menu,
                                        self.top_coord_top_menu
                                        )

        '''set_full_screen'''
        browser.set_full_screen(samples_dir, self.REGIONS_ON_WINDOW)

        '''get lists of buttons and locales'''
        self.buttons = os.listdir('{}{}'.format(os.getcwd(), en_buttons_dir))
        self.locales = os.listdir('{}{}'.format(os.getcwd(), en_locales_dir))

        '''check locales when focus to buttons'''
        for button, locale in zip(self.buttons, self.locales):
            button_coord = browser.monosearch_10(button, en_buttons_dir)
            with self.subTest():
                self.assertTrue(button_coord, msg="{} not finded".format(button))
            if button_coord:
                browser.move_mouse_to(button_coord)
                with self.subTest():
                    self.assertTrue(browser.monosearch_10(locale, en_locales_dir), msg="{} not finded".format(locale))

    # @unittest.skip('I skip it')
    @wrappers.write_log_and_video(videos_dir)
    def test_de_button_tips_locale(self):
        ''''''
        pyautogui.moveTo(5, 5, 1)
        '''choose language'''

        if not browser.monosearch_10('de_language_selected.png', samples_dir):
            browser.change_lanuage('de_language_selected.png', samples_dir)
            time.sleep(40)

        pyautogui.moveTo(5, 5, 1)
        '''close_all_bonus_windows'''
        browser.close_all_bonus_windows(samples_dir,
                                        self.driver,
                                        self.height_screen,
                                        self.left_coord_top_menu,
                                        self.top_coord_top_menu
                                        )

        '''set_full_screen'''
        browser.set_full_screen(samples_dir, self.REGIONS_ON_WINDOW)

        '''get lists of buttons and locales'''
        self.buttons = os.listdir('{}{}'.format(os.getcwd(), de_buttons_dir))
        self.locales = os.listdir('{}{}'.format(os.getcwd(), de_locales_dir))

        '''check locales when focus to buttons'''
        for button, locale in zip(self.buttons, self.locales):
            button_coord = browser.monosearch_10(button, de_buttons_dir)
            with self.subTest():
                self.assertTrue(button_coord, msg="{} not finded".format(button))
            if button_coord:
                browser.move_mouse_to(button_coord)
                with self.subTest():
                    self.assertTrue(browser.monosearch_10(locale, de_locales_dir), msg="{} not finded".format(locale))


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'),
                  verbosity=2
                  )