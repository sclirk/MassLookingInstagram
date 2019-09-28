from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

global child
child=12
step=1

chromedriver_path = 'C:/chromedriver.exe'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(3)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('sclirk')
password = webdriver.find_element_by_name('password')
password.send_keys('NEW_castle113')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_login.click()
sleep(4)

but=webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
but.click()
sleep(2)



search = webdriver.find_element_by_class_name('TqC_a')
search.click()

searc = webdriver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
searc.send_keys('marizhelby')
sleep(2)

s = webdriver.find_element_by_class_name('Ap253')
s.click()
sleep(2)

e = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
e.click()
sleep(2)
g = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child(1) > div > div.Igw0E.IwRSH.YBx95.vwCYk')
g.click()
sleep(2)
while True:
    child+=1
    step+=0.3
    if child<11:
        try:
            sleep(1)
            t = webdriver.find_element_by_xpath(('/html/body/div[2]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(2)
            print(child,child)
        except Exception:
            print(pyautogui.position())
            sleep(1)
            t = webdriver.find_element_by_xpath(('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(2)
            print(child,child,child)
        try:
            t.click()
        except Exception:
            try:
                r=webdriver.find_element_by_css_selector('#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep(1)
            except Exception:
                search = webdriver.find_element_by_class_name('TqC_a')
                search.click()
                sleep(2)
                searc = webdriver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(1)
                s = webdriver.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = webdriver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)
    else:
        try:
            print(pyautogui.position())
            pyautogui.moveTo(780, 636)
            pyautogui.click(780, 636, (int(child)+int(step//2)) ,0.5)
            sleep(1)
            #t = webdriver.find_element_by_xpath(('/html/body/div[2]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            #t.click()
            #sleep(2)
            print(child,step)
            try:
                r = webdriver.find_element_by_css_selector('#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep(1)
            except Exception:
                search = webdriver.find_element_by_class_name('TqC_a')
                search.click()
                sleep(2)
                searc = webdriver.find_element_by_css_selector(
                    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(1)
                s = webdriver.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = webdriver.find_element_by_css_selector(
                    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)
        except Exception:
            print(pyautogui.position())
            sleep(1)
            t = webdriver.find_element_by_xpath(('/html/body/div[3]/div/div[2]/ul/div/li[{}]/div/div[1]/div[1]'.format(child)))
            t.click()
            sleep(1)
            print(child,step,step)
            try:
                r = webdriver.find_element_by_css_selector(
                    '#react-root > section > div > div > section > div.GHEPc > button.-jHC6')
                r.click()
                sleep(1)
            except Exception:
                search = webdriver.find_element_by_class_name('TqC_a')
                search.click()
                sleep(3)
                searc = webdriver.find_element_by_css_selector(
                    '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
                searc.send_keys('marizhelby')
                sleep(2)
                s = webdriver.find_element_by_class_name('Ap253')
                s.click()
                sleep(2)
                e = webdriver.find_element_by_css_selector(
                    '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
                e.click()
                sleep(2)