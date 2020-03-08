from selenium import webdriver
from time import sleep


def loocker():
    global name
    name = "marizhelby"  # name started profile
    default_name = name
    iteration = 10
    
    browser = webdriver.Chrome("C:/chromedriver.exe")
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)

    username = browser.find_element_by_name("username")
    username.send_keys('username')
    password = browser.find_element_by_name('password')
    password.send_keys('userpass')

    button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                        'div:nth-child(1) > div > form > div:nth-child(4) > button > '
                                                        'div')
    button_login.click()
    sleep(25)

    passw = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                                          '2]/button')
    passw.click()
    sleep(8)

    but = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
    but.click()
    sleep(3)

    search = browser.find_element_by_class_name('TqC_a')
    search.click()

    searc = browser.find_element_by_css_selector(
        '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
    searc.send_keys('{}'.format(name))
    sleep(3)

    s = browser.find_element_by_class_name('Ap253')
    s.click()
    sleep(3)

    e = browser.find_element_by_css_selector(
        '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
    e.click()
    sleep(3)
    child = 0

    def find_name():
        search = browser.find_element_by_class_name('TqC_a')
        search.click()
        sleep(2)
        searc = browser.find_element_by_css_selector(
            '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
        searc.send_keys('{}'.format(name))
        sleep(3)
        s = browser.find_element_by_class_name('Ap253')
        s.click()
        sleep(2)
        e = browser.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
        e.click()
        sleep(2)

    def click_followers():
        sleep(1)
        t = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div/li[{}]/div/div[1]/div'.format(child))
        t.click()
        sleep(2)

    def another_clock_followers():
        sleep(1)
        t = browser.find_element_by_xpath(
            ('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
        t.click()
        sleep(5)

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
                    sleep(1)
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
                    sleep(2)
                    history = browser.find_element_by_css_selector(
                        "#react-root > section > main > div > header > section > div.nZSzR > h1")
                    name = history.text
                    child = 0
                    sleep(4)
                    homepage = browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div')
                    homepage.click()
                    find_name()
                except Exception:
                    sleep(2)
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


loocker()
