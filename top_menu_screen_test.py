import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner
from multiprocessing import Pool
from xmlrunner import xmlrunner

import browser
from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS

SOCIAL = 'FB'

class TopMenuTests(unittest.TestCase):
    def get_screen(self):
        for i in range(10):
            pyautogui.screenshot('{}{}{}'.format(os.getcwd(),
                                                 '\\screens\\friends\\',
                                                 '{}_{}.png'.format(self, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
                                                 )
                                 )

    def find_image(self, image_name, **kwargs):
        for i in range(10):
            coord = pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\friends\\samples\\', image_name),
                                             # grayscale=True,
                                             **kwargs
                                             )
            if coord:
                return coord
        return None

    def click_to_center(self, button):
        x, y = pyautogui.center(button)
        pyautogui.click(x=x, y=y)

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
        browser.go_to_social_network(self.driver, SOC_NET_LINKS[SOCIAL])

    def tearDown(self):
        self.driver.quit()

    # @unittest.skip('I have skipped it')
    def test_invite_friends(self):
        ''''''
        '''find button_button_inv_friend'''
        self.button_button_inv_friend = self.find_image('button_inv_friend.png')
        if self.button_button_inv_friend:
            '''click to invite friends button'''
            self.click_to_center(self.button_button_inv_friend)
            '''check image'''
            self.assertTrue(self.find_image('sample_invite_friend_window.png'))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_inv_friend")

    # @unittest.skip('I have skipped it')
    def test_faq(self):
        ''''''
        '''find button_faq'''
        self.button_faq = self.find_image('button_faq.png')
        if self.button_faq:
            '''click to invite friends button'''
            self.click_to_center(self.button_faq)
            '''check image'''
            time.sleep(5)
            self.assertTrue(self.find_image('sample_faq_window.png'))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_faq")

    # @unittest.skip('I have skipped it')
    def test_community(self):
        ''''''
        '''find button_community'''
        self.button_community = self.find_image('button_community.png')
        if self.button_community:
            '''click to community button'''
            self.click_to_center(self.button_community)
            '''find button_not_accept_message'''
            # time.sleep(15)
            self.button_not_accept_message = self.find_image('button_not_accept_message.png')
            if self.button_not_accept_message:
                self.click_to_center(self.button_not_accept_message)
            '''check image'''
            time.sleep(5)
            self.assertTrue(self.find_image('sample_community_window.png'))
            with self.subTest():
                self.assertTrue(self.find_image('a.png'))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_community")

        # pyautogui.hotkey('ctrl', 'w')

    # @unittest.skip('I have skipped it')
    def test_add_gold(self):
        ''''''
        '''get screen resolution size'''
        width_screen, height_screen = pyautogui.size()

        '''find game's top menu'''
        left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = self.find_image('top_menu.png')

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

        time.sleep(30)

        '''find button_add_gold'''
        self.button_add_gold = self.find_image('button_add_gold.png')
        if not self.button_add_gold: self.get_screen()

        '''click to button_add_gold'''
        self.click_to_center(self.button_add_gold)

        '''check image'''
        # with Pool(2) as p:
        #     for image in p.imap_unordered(self.find_image, ('sample_add_gold_window.png', )):
        #         if image:
        #             self.assertTrue(image)
        #             break
        self.assertTrue(self.find_image('sample_add_gold_action_window.png') or self.find_image('sample_add_gold_window.png'),
                        msg="sample_add_gold_action_window.png and sample_add_gold_window.png aren't finded")

    # @unittest.skip('I have skipped it')
    def test_language_select(self):
        ''''''
        '''find language_select'''
        self.language_select = self.find_image('language_select.png')
        if self.language_select:
            '''click to language_select'''
            self.click_to_center(self.language_select)
            '''find list_of_languages'''
            # time.sleep(15)
            '''check image'''
            time.sleep(5)
            self.assertTrue(self.find_image('list_of_languages.png'))




if __name__ == "__main__":
    for _ in range(10):
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'), verbosity=2)

    # search_tests = unittest.TestLoader().loadTestsFromTestCase(TopMenuTests)
    # smoke_tests = unittest.TestSuite([search_tests, ])
    # xmlrunner.XMLTestRunner(verbosity=2, output='test-rep123').run(smoke_tests)