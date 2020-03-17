from selenium import webdriver
from time import sleep


class looker:
    def __init__(self, user_name,
                 name,
                 password,
                 driver_place,
                 instagram_url='https://www.instagram.com/accounts/login/?source=auth_switcher'):
        self.name = name
        self.driver_place = driver_place
        self.browser = webdriver.Chrome(self.driver_place)
        self.browser.get(instagram_url)
        self.user_name = user_name
        self.password = password
        self.child, self.text = (0, 0)

    def max_sleep(self):
        sleep(25)

    def long_sleep(self):
        sleep(5)

    def middle_sleep(self):
        sleep(3)

    def short_sleep(self):
        sleep(1)

    def open_insta(self):
        self.long_sleep()
        self.browser.find_element_by_name('username').send_keys(self.user_name)
        self.browser.find_element_by_name('password').send_keys(self.password)
        self.browser.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                  'div:nth-child(1) > div > form '
                                                  '> div:nth-child(4) > button > '
                                                  'div').click()
        self.long_sleep()

        while True:
            self.text = self.browser.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input') \
                .get_attribute('value')
            print(self.text)
            self.middle_sleep()
            if len(self.text) != 6:
                self.middle_sleep()
                print(len(self.text))
            else:
                self.browser.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                    '2]/button').click()
                break

        self.long_sleep()

        self.browser.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        self.middle_sleep()

        self.browser.find_element_by_class_name('TqC_a').click()
        self.short_sleep()

        self.browser.find_element_by_css_selector(
            '#react-root > section > nav > div._8MQSO.Cx7Bp '
            '> div > div > div.LWmhU._0aCwM > input').send_keys('{}'.format(self.name))
        self.middle_sleep()
        self.browser.find_element_by_class_name('Ap253').click()
        self.middle_sleep()

        self.browser.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
        self.middle_sleep()

    def find_name(self):
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div').click()
        self.middle_sleep()
        self.browser.find_element_by_css_selector(
            '#react-root > section > nav > '
            'div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input').send_keys('{}'.format(self.name))
        self.middle_sleep()
        self.browser.find_element_by_class_name('Ap253').click()
        self.middle_sleep()
        self.browser.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
        self.middle_sleep()

    def click_followers_with_params(self, div_code):
        self.short_sleep()
        self.browser.find_element_by_xpath(
            ('/html/body/div[{}]/div/div[2]/ul/div/li[{}]/div/div[1]/div'.format(div_code, self.child))).click()
        self.long_sleep()
