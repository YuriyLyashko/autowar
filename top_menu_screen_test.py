import os, datetime, time, unittest, pyautogui, warnings, HtmlTestRunner
from xmlrunner import xmlrunner

from open_chrome import open_chrome
from authentication_info import SOC_AUTH_INFO, SOC_NET_LINKS

SOCIAL = 'FB'

class ScreenTests(unittest.TestCase):
    def get_screen(self):
        for i in range(10):
            coord = pyautogui.screenshot('{}{}{}'.format(os.getcwd(),
                                                         '\\screens\\friends\\',
                                                         '{}_{}.png'.format(self, datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')))
                                         )

    def find_image(self, image_name, min_seatch_time = 0, **kwargs):
        return pyautogui.locateOnScreen('{}{}{}'.format(os.getcwd(), '\\screens\\friends\\samples\\', image_name),
                                        min_seatch_time, **kwargs)

    def click_to_center(self, button):
        x, y = pyautogui.center(button)
        pyautogui.click(x=x, y=y)



    def setUp(self):
        ''''''
        '''ignore insides warnings'''
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

        '''open chrome'''
        self.driver = open_chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        '''go to social network'''
        self.driver.get(SOC_NET_LINKS[SOCIAL])

        '''login'''
        self.driver.find_element_by_id('email').send_keys(SOC_AUTH_INFO[SOCIAL]['LOGIN'])
        self.driver.find_element_by_id('pass').send_keys(SOC_AUTH_INFO[SOCIAL]['PASS'])
        self.driver.find_element_by_id('loginbutton').click()

        '''go to game page'''
        self.driver.get(SOC_NET_LINKS[SOCIAL])

    def test_invite_friends_screen(self):
        ''''''
        '''find button_button_inv_friend'''
        self.button_button_inv_friend = self.find_image('button_inv_friend.png', 10)
        if self.button_button_inv_friend:
            '''click to invite friends button'''
            self.click_to_center(self.button_button_inv_friend)
            '''check image'''
            self.assertTrue(self.find_image('sample_invite_friend_window.png', 10))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_inv_friend")


    def test_faq_screen(self):
        ''''''
        '''find button_faq'''
        self.button_faq = self.find_image('button_faq.png', 10)
        if self.button_faq:
            '''click to invite friends button'''
            self.click_to_center(self.button_faq)
            '''check image'''
            time.sleep(5)
            self.assertTrue(self.find_image('sample_faq_window.png', 10))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_faq")

    def test_community_screen(self):
        ''''''
        '''find button_community'''
        self.button_community = self.find_image('button_community.png', 10)
        if self.button_community:
            '''click to invite friends button'''
            self.click_to_center(self.button_community)
            '''find button_not_accept_message'''
            time.sleep(15)
            self.button_not_accept_message = self.find_image('button_not_accept_message.png')
            if self.button_not_accept_message:
                self.click_to_center(self.button_not_accept_message)
            '''check image'''
            time.sleep(5)
            self.assertTrue(self.find_image('sample_community_window.png', 10))
        else:
            self.get_screen()
            raise ValueError("isn't fiding button_community")
        pyautogui.hotkey('ctrl', 'w')

    @unittest.skip('I skipped it')
    def test_add_gold_screen(self):
        ''''''
        '''get screen resolution size'''
        width_screen, height_screen = pyautogui.size()

        '''find game's top menu'''
        top_menu_location = self.find_image('top_menu.png')
        left_coord_top_menu, top_coord_top_menu, width_top_menu, height_top_menu = top_menu_location

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

        time.sleep(40)

        '''find button_add_gold'''
        self.button_add_gold = self.find_image('button_add_gold.png', 10)
        if not self.button_add_gold: self.get_screen()

        '''click to invite friends button'''
        self.click_to_center(self.button_add_gold)

        '''check image'''
        self.assertTrue(self.find_image('sample_add_gold_action_window.png', 10) or self.find_image('sample_add_gold_window.png'))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Jen', report_title='There is autotesting, MF'), verbosity=2)

    # search_tests = unittest.TestLoader().loadTestsFromTestCase(ScreenTests)
    # smoke_tests = unittest.TestSuite([search_tests, ])
    # xmlrunner.XMLTestRunner(verbosity=2, output='test-rep123').run(smoke_tests)