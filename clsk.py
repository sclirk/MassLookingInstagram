'''Use 3-4 cecs of 'sleep' because of slowly ethernet, your may change this
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

global child
child = 0
step = 1

browser = webdriver.Chrome("C:/chromedriver.exe")
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = browser.find_element_by_name("username")
username.send_keys('username')
password = browser.find_element_by_name('password')
password.send_keys('pass')

button_login = browser.find_element_by_css_selector('#react-root > section > main > div > article > div > '
                                                      'div:nth-child(1) > div > form > div:nth-child(4) > button > '
                                                      'div')
button_login.click()
sleep(15)

passw = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                                        '1]/div/label/input')
passw2 = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div['
                                         '2]/button')
passw2.click()
sleep(14) #sms time
# if len(passw.get_attribute('value'))==6:
#     env=webdriver.find_element_by_css_selector('#react-root > section > main >div > article > div > div:nth-child(1) '
#                                                '> div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.CovQj.jKUp7.iHqQ7 '
#                                                '>button')
#     env.click()
#     sleep(7)
# else:
#     sleep(5)
# work in lowly progress


but = browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
but.click()
sleep(2)

search = browser.find_element_by_class_name('TqC_a')
search.click()

searc = browser.find_element_by_css_selector(
    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
searc.send_keys('marizhelby')
sleep(2)

s = browser.find_element_by_class_name('Ap253')
s.click()
sleep(2)

e = browser.find_element_by_css_selector(
    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
e.click()
sleep(2)
g = browser.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child(1) > div > div.Igw0E.IwRSH.YBx95.vwCYk')
g.click()
sleep(2)
while True:
    child += 1
    step += 0.3
    if child < 11:
        try:
            sleep(1)
            t = browser.find_element_by_xpath(
                ('/html/body/div[2]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(2)
            print(child, child)
        except Exception:
            print(pyautogui.position())
            sleep(1)
            t = browser.find_element_by_xpath(
                ('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(2)
            print(child, child, child)
        try:
            t.click()
        except Exception:
            try:
                r = browser.find_element_by_css_selector(
                    '#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep(1)
            except Exception:
                search = browser.find_element_by_class_name('TqC_a')
                search.click()
                sleep(2)
                searc = browser.find_element_by_css_selector(
                    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(1)
                s = browser.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = browser.find_element_by_css_selector(
                    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)
    else:
        try:
            print(pyautogui.position())
            pyautogui.moveTo(780, 636) #actual for 1366x768
            pyautogui.click(780, 636, (int(child) + int(step // 2)), 0.5)
            sleep(1)
            print(child, step)
            try:
                r = webdriver.find_element_by_css_selector(
                    '#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep1(1)
            except Exception:
                search = browser.find_element_by_class_name('TqC_a')
                search.click()
                sleep(2)
                searc = browser.find_element_by_css_selector(
                    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(1)
                s = browser.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = browser.find_element_by_css_selector(
                    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)
        except Exception:
            print(pyautogui.position())
            sleep(1)
            t = browser.find_element_by_xpath(
                ('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(1)
            print(child, step, step)
            try:
                r = browser.find_element_by_css_selector(
                    '#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep(1)
            except Exception:
                search = browser.find_element_by_class_name('TqC_a')
                search.click()
                sleep(3)
                searc = browser.find_element_by_css_selector(
                    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(2)
                s = browser.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = browser.find_element_by_css_selector(
                    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)
