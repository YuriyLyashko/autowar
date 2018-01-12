import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner

import browser, dump_loader

from tutor_py_files import wrappers
from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS
from tutor_py_files import regions


SOCIAL = 'FB'
SERVER = 'FB'


class LocalesTests(unittest.TestCase):
    @wrappers.write_log_and_video
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
            browser.monosearch_1000('top_menu.png')

        '''scroll down'''
        self.driver.execute_script('scroll({},{});'.format(self.left_coord_top_menu, self.top_coord_top_menu - 150))

        '''click to game area'''
        time.sleep(1)
        pyautogui.click(x=self.width_top_menu - self.left_coord_top_menu, y=self.top_coord_top_menu + self.height_screen / 2)

        '''accept flash running'''
        time.sleep(0.5)
        button_accept_flash_running = self.find_image('accept_flash_running.png')
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

    def find_image(self, image_name, **kwargs):
        for i in range(10):
            coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\locales\\samples\\', image_name),
                                             # grayscale=True,
                                             **kwargs
                                             )
            if coord:
                return coord
        return None

    def find_all_images(self, image_name, **kwargs):
        for i in range(10):
            coords = pyautogui.locateAllOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\locales\\samples\\', image_name),
                                                 # grayscale=True,
                                                 **kwargs
                                                 )
            if coords:
                return coords
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

    def close_all_bonus_windows(self):
        '''close all bonus windows'''

        while self.find_image('button_close_window.png'):
            self.all_buttons_close_window = self.find_all_images('button_close_window.png')
            for coord in self.all_buttons_close_window: self.click_to_center(coord)

        browser.scroll_down(self.driver, 0, self.height_screen)

        self.button_thank_you_for_comeback = self.find_image('button_thank_you_for_comeback.png')
        if self.button_thank_you_for_comeback: self.click_to_center(self.button_thank_you_for_comeback)

        self.button_restore = self.find_image('button_restore.png')
        if self.button_restore: self.click_to_center(self.button_restore)

        browser.scroll_down(self.driver, self.left_coord_top_menu, self.top_coord_top_menu - 100)



    def change_lanuage(self):
        self.click_to_center(self.find_image('language_select.png'))
        self.click_to_center(self.find_image('language_select.png'))

    @wrappers.write_log_and_video
    def test_ru_button_tips_locale(self):
        if not self.find_image('ru_language_selected.png'): self.change_lanuage()
        self.close_all_bonus_windows()

        '''set_full_screen'''
        browser.set_full_screen(self.REGIONS_ON_WINDOW)

        '''get lists of buttons and locales'''
        self.buttons = os.listdir('{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\buttons'))
        self.locales = os.listdir('{}{}'.format(os.getcwd(), '\\screens\\locales\\ru\\locales'))

        '''check locales when focus to buttons'''
        for button, locale in zip(self.buttons, self.locales):
            button_coord = self.find_button(button)
            with self.subTest():
                self.assertTrue(button_coord, msg="{} not finded".format(button))
            if button_coord:
                self.move_mouse_to(button_coord)
                with self.subTest():
                    self.assertTrue(self.find_locale(locale), msg="{} not finded".format(locale))

        # time.sleep(60*5)




if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'),
                  verbosity=2
                  )