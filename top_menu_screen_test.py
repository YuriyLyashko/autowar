import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner
from multiprocessing import Pool
from xmlrunner import xmlrunner

import browser
from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS
from top_menu_py_files.directories_settings import *

SOCIAL = 'FB'

class TopMenuTests(unittest.TestCase):
    def setUp(self):
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

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip('I have skipped it')
    def test_invite_friends(self):
        ''''''
        '''find button_button_inv_friend'''
        self.button_button_inv_friend = browser.monosearch_10('button_inv_friend.png', samples_dir)
        if self.button_button_inv_friend:
            '''click to invite top_menu_py_files button'''
            browser.click_to_center(self.button_button_inv_friend)
            '''check image'''
            self.assertTrue(browser.monosearch_10('sample_invite_friend_window.png', samples_dir))
        else:
            browser.get_screen(screens_dir)
            raise ValueError("isn't fiding button_inv_friend")

    # @unittest.skip('I have skipped it')
    def test_faq(self):
        ''''''
        '''find button_faq'''
        self.button_faq = browser.monosearch_10('button_faq.png', samples_dir)
        if self.button_faq:
            '''click to invite top_menu_py_files button'''
            browser.click_to_center(self.button_faq)
            '''check image'''
            time.sleep(5)
            self.assertTrue(browser.monosearch_10('sample_faq_window.png', samples_dir))
        else:
            browser.get_screen(screens_dir)
            raise ValueError("isn't fiding button_faq")

    # @unittest.skip('I have skipped it')
    def test_community(self):
        ''''''
        '''find button_community'''
        self.button_community = browser.monosearch_10('button_community.png', samples_dir)
        if self.button_community:
            '''click to community button'''
            browser.click_to_center(self.button_community)
            '''find button_not_accept_message'''
            # time.sleep(15)
            self.button_not_accept_message = browser.monosearch_10('button_not_accept_message.png', samples_dir)
            if self.button_not_accept_message:
                browser.click_to_center(self.button_not_accept_message)
            '''check image'''
            time.sleep(5)
            self.assertTrue(browser.monosearch_10('sample_community_window.png', samples_dir))
            with self.subTest():
                self.assertTrue(browser.monosearch_10('a.png', samples_dir))
        else:
            browser.get_screen(screens_dir)
            raise ValueError("isn't fiding button_community")

        # pyautogui.hotkey('ctrl', 'w')

    # @unittest.skip('I have skipped it')
    def test_add_gold(self):
        ''''''
        '''get screen resolution size'''
        width_screen, height_screen = pyautogui.size()

        '''find game's top menu'''
        left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = browser.monosearch_10('top_menu.png', samples_dir)

        '''scroll down'''
        self.driver.execute_script('scroll({},{});'.format(left_coord_top_menu, top_coord_top_menu - 150))

        '''click to game area'''
        time.sleep(1)
        pyautogui.click(x=width_top_menu - left_coord_top_menu, y=top_coord_top_menu + height_screen / 2)

        '''accept flash running'''
        time.sleep(0.5)
        button_accept_flash_running = browser.monosearch_10('accept_flash_running.png', samples_dir)
        if button_accept_flash_running:
            button_accept_flash_running_x, button_accept_flash_running_y = pyautogui.center(button_accept_flash_running)
            pyautogui.click(x=button_accept_flash_running_x, y=button_accept_flash_running_y)

        time.sleep(30)

        '''find button_add_gold'''
        self.button_add_gold = browser.monosearch_10('button_add_gold.png', samples_dir)
        if not self.button_add_gold:
            browser.get_screen(screens_dir)

        '''click to button_add_gold'''
        browser.click_to_center(self.button_add_gold)

        '''check image'''
        # with Pool(2) as p:
        #     for image in p.imap_unordered(self.find_image, ('sample_add_gold_window.png', )):
        #         if image:
        #             self.assertTrue(image)
        #             break
        self.assertTrue(browser.monosearch_10('sample_add_gold_action_window.png', samples_dir) or
                        browser.monosearch_10('sample_add_gold_window.png', samples_dir),
                        msg="sample_add_gold_action_window.png and sample_add_gold_window.png aren't finded")

    # @unittest.skip('I have skipped it')
    def test_language_select(self):
        ''''''
        '''find language_select'''
        self.language_select = browser.monosearch_10('language_select.png', samples_dir)
        if self.language_select:
            '''click to language_select'''
            browser.click_to_center(self.language_select)
            '''find list_of_languages'''
            # time.sleep(15)
            '''check image'''
            time.sleep(5)
            self.assertTrue(browser.monosearch_10('list_of_languages.png', samples_dir))




if __name__ == "__main__":
    for _ in range(10):
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'), verbosity=2)

    # search_tests = unittest.TestLoader().loadTestsFromTestCase(TopMenuTests)
    # smoke_tests = unittest.TestSuite([search_tests, ])
    # xmlrunner.XMLTestRunner(verbosity=2, output='test-rep123').run(smoke_tests)