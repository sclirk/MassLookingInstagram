from selenium import webdriver
from time import sleep


def looker():
    global name
    name = "marizhelby"
    child = 0
    iteration = 10
    default_name = name
    browser = webdriver.Chrome("C:/chromedriver.exe")
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

    def max_sleep():
        sleep(25)

    def long_sleep():
        sleep(5)

    def mid_sleep():
        sleep(3)

    def short_sleep():
        sleep(1)

    def name_user_and_log_in():
        browser.find_element_by_name("username").send_keys('passw')
        browser.find_element_by_name('password').send_keys('passw')
        browser.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                             'div:nth-child(1) > div > form '
                                             '> div:nth-child(4) > button > '
                                             'div').click()
        max_sleep()

        browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                                      '2]/button').click()
        long_sleep()

        browser.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        mid_sleep()

    long_sleep()
    name_user_and_log_in()
    browser.find_element_by_class_name('TqC_a').click()
    short_sleep()

    browser.find_element_by_css_selector(
        '#react-root > section > nav > div._8MQSO.Cx7Bp '
        '> div > div > div.LWmhU._0aCwM > input').send_keys('{}'.format(name))
    mid_sleep()
    browser.find_element_by_class_name('Ap253').click()
    mid_sleep()

    browser.find_element_by_css_selector(
        '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
    mid_sleep()

    def find_name():
        browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div').click()
        mid_sleep()
        browser.find_element_by_css_selector(
            '#react-root > section > nav > '
            'div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input').send_keys('{}'.format(name))
        mid_sleep()
        browser.find_element_by_class_name('Ap253').click()
        mid_sleep()
        browser.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a').click()
        mid_sleep()

    def click_followers():
        short_sleep()
        browser.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div'.format(child)).click()
        short_sleep()

    def another_click_followers():
        short_sleep()
        browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)).click()
        long_sleep()

    while True:
        print(child, iteration)
        child += 1
        if child < iteration:
            try:
                short_sleep()
                click_followers()
            except Exception:
                another_click_followers()
            try:
                short_sleep()
                find_name()
            except Exception:
                try:
                    browser.find_element_by_css_selector(
                        '#react-root > section > div > div > section > div.GHEPc > button.-jHC6').click()
                    short_sleep()
                except Exception:
                    find_name()
        else:
            click_followers()
            try:  # have story
                story_close = browser.find_element_by_css_selector(
                    '#react-root > section > div > div > section > header > div > div.MS2JH > div > div > div > a')
                story_close.click()
                short_sleep()
                iteration = 10
                browser.find_element_by_css_selector(
                    '#react-root > section > div > div >'
                    ' section > header > div > div.MS2JH > div > div > div > a').click()
                short_sleep()
                history = browser.find_element_by_css_selector(
                    "#react-root > section > main > div > header > section > div.nZSzR > h1")
                name = history.text
                child = 0
                long_sleep()
                browser.find_element_by_xpath(
                    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div').click()
                find_name()
            except Exception:  # without story
                profile = browser.find_element_by_css_selector(
                    "#react-root > section > main > div > header > section > div.nZSzR > h1")
                name = profile.text
                short_sleep()
                iteration -= 1
                find_name()


looker()
