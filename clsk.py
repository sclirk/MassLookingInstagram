from selenium import webdriver
from time import sleep


def looker():
    global name
    name = "marizhelby"  # имя посещаемого профиля
    default_name = name
    iteration = 10
    
    def max_sleep():
        sleep(25)

    def long_sleep():
        sleep(5)

    def mid_sleep():
        sleep(3)

    def short_sleep():
        sleep(1)

    browser = webdriver.Chrome("C:/chromedriver.exe")
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    mid_sleep()

    username = browser.find_element_by_name("username")
    username.send_keys('USERNAME')
    password = browser.find_element_by_name('password')
    password.send_keys('PASSWORD')

    button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                        'div:nth-child(1) > div > form > div:nth-child(4) > button > '
                                                        'div')
    button_login.click()
    max_sleep()

    passw = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                                          '2]/button')
    passw.click()
    long_sleep()

    but = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    but.click()
    mid_sleep()

    search = browser.find_element_by_class_name('TqC_a')
    search.click()

    searc = browser.find_element_by_css_selector(
        '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
    searc.send_keys('{}'.format(name))
    mid_sleep()

    s = browser.find_element_by_class_name('Ap253')
    s.click()
    mid_sleep()

    e = browser.find_element_by_css_selector(
        '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
    e.click()
    mid_sleep()
    child = 0

    def find_name():
        search = browser.find_element_by_class_name('TqC_a')
        search.click()
        mid_sleep()
        searc = browser.find_element_by_css_selector(
            '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        searc.send_keys('{}'.format(name))
        mid_sleep()
        s = browser.find_element_by_class_name('Ap253')
        s.click()
        mid_sleep()
        e = browser.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
        e.click()
        mid_sleep()

    def click_followers():
        short_sleep()
        t = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div'.format(child))
        t.click()
        short_sleep()

    def another_clock_followers():
        short_sleep()
        t = browser.find_element_by_xpath(
            ('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
        t.click()
        long_sleep()

    while True:
        child += 1
        if child < iteration:
            try:
                click_followers()
            except Exception:
                another_clock_followers()
            try:
                click_followers.t.click()
            except Exception:
                try:
                    r = browser.find_element_by_css_selector(
                        '#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                    r.click()
                    short_sleep()
                except Exception:
                    find_name()
        else:
            try:
                click_followers()
            except Exception:
                another_clock_followers()
            try:
                another_clock_followers.t.click()
            except Exception:
                try:
                    iteration = 10
                    close_story = browser.find_element_by_css_selector(
                        '#react-root > section > div > div > section > header > div > div.MS2JH > div > div > div > a')
                    close_story.click()
                    short_sleep()
                    history = browser.find_element_by_css_selector(
                        "#react-root > section > main > div > header > section > div.nZSzR > h1")
                    name = history.text
                    child = 0
                    mid_sleep()
                    homepage = browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div')
                    homepage.click()
                    find_name()
                except Exception:
                    short_sleep()
                    name = default_name
                    iteration -= 1
                    find_name()
                    # history = browser.find_element_by_css_selector(
                    #     "#react-root > section > main > div > header > section > div.nZSzR > h1")
                    # name = history.text
                    # child = 0
                    # sleep(4)
                    # homepage = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div')
                    # homepage.click()
                    # find_name()


looker()
