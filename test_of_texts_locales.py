import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner

import browser

from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS
from tutor_py_files import regions


SOCIAL = 'FB'


class LocalesTests(unittest.TestCase):
    def setUp(self):
        # import load_max_lvl_dump
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
        browser.go_to_social_network(self.driver, SOC_NET_LINKS[SOCIAL])

        '''get screen resolution size'''
        width_screen, height_screen = pyautogui.size()

        '''find game's top menu'''
        left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = browser.persistent_search('top_menu.png')

        '''scroll down'''
        self.driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 150))

        '''click to game area'''
        time.sleep(1)
        pyautogui.click(x=width_top_menu - left_coord_top_menu, y=top_coord_top_menu + height_screen / 2)

        '''accept flash running'''
        time.sleep(0.5)
        button_accept_flash_running = self.find_image('accept_flash_running.png')
        if button_accept_flash_running:
            button_accept_flash_running_x, button_accept_flash_running_y = pyautogui.center(button_accept_flash_running)
            pyautogui.click(x=button_accept_flash_running_x, y=button_accept_flash_running_y)

        time.sleep(20)

        # self.button_get_daily_bonus = self.find_image('button_get_daily_bonus.png')
        # if self.button_get_daily_bonus: self.click_to_center(self.button_get_daily_bonus)

        '''close all bonus windows'''
        self.button_close_window = self.find_image('button_close_window.png')
        if self.button_close_window: self.click_to_center(self.button_close_window)

        REGIONS_ON_WINDOW, REGIONS_ON_FULL_SCREEN = regions.get_regions(left_coord_top_menu,
                                                                        width_top_menu,
                                                                        height_screen,
                                                                        width_screen
                                                                        )
        '''set_full_screen'''
        browser.set_full_screen(REGIONS_ON_WINDOW)

    def tearDown(self):
        self.driver.quit()

    def find_image(self, image_name, **kwargs):
        for i in range(10):
            coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\locales\\samples\\', image_name),
                                             # grayscale=True,
                                             **kwargs
                                             )
            if coord:
                return coord
        return None

    def find_button(self, image_name, **kwargs):
        for i in range(10):
            coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\buttons\\', image_name),
                                             # grayscale=True,
                                             **kwargs
                                             )
            if coord:
                return coord
        return None

    def find_locale(self, image_name, **kwargs):
        for i in range(10):
            coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\locales\\', image_name),
                                             # grayscale=True,
                                             **kwargs
                                             )
            if coord:
                return coord
        return None

    def click_to_center(self, button):
        x, y = pyautogui.center(button)
        pyautogui.click(x=x, y=y)

    def move_mouse_to(self, button, righter_on=0, lefter_on=0, lower_on=0, higher_on=0):
        x, y = pyautogui.center(button)
        pyautogui.moveTo(x=x + righter_on - lefter_on, y=y + lower_on - higher_on, duration=0.5)

    def test_ru_button_tips_locale(self):
        self.buttons = os.listdir('{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\buttons'))
        self.locales = os.listdir('{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\locales'))
        ''''''
        for button, locale in zip(self.buttons, self.locales):
            self.move_mouse_to(self.find_button(button))
            with self.subTest():
                self.assertTrue(self.find_locale(locale), msg="{} not finded".format(locale))

        # time.sleep(60*5)




if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'), verbosity=2)