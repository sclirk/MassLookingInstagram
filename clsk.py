from instalook import *

look = looker("USERNAME", "FIND_PROFILE_NAME", "PASS_YOUR_PROFILE", "example_location_for_webdriver(C:\chromedriver.exe)")
look.open_insta()


class global_looker:
    def __init__(self, iteration):
        self.iteration = iteration

    def cycle(self):
        while True:
            look.child += 1
            if look.child < self.iteration:
                try:
                    look.short_sleep()
                    look.click_followers_with_params(3)
                except Exception:
                    look.click_followers_with_params(4)
                try:
                    look.short_sleep()
                    look.find_name()
                except Exception:
                    try:
                        look.browser.find_element_by_css_selector(
                            '#react-root > section > div > div > section > div.GHEPc > button.-jHC6').click()
                        look.short_sleep()
                    except Exception:
                        look.find_name()
            else:
                look.click_followers_with_params(4)
                try:
                    story_close = look.browser.find_element_by_css_selector(
                        '#react-root > section > div > div > section > header > div > div.MS2JH > div > div > div > a')
                    story_close.click()
                    self.iteration = 10
                    look.browser.find_element_by_css_selector(
                        '#react-root > section > div > div >'
                        ' section > header > div > div.MS2JH > div > div > div > a').click()
                    look.short_sleep()
                    history = look.browser.find_element_by_css_selector(
                        "#react-root > section > main > div > header > section > div.nZSzR > h1")
                    look.name = history.text
                    look.child = 0
                    look.long_sleep()
                    look.browser.find_element_by_xpath(
                        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div').click()
                    look.find_name()
                except Exception:
                    profile = look.browser.find_element_by_css_selector(
                        "#react-root > section > main > div > header > section > div.nZSzR > h1")
                    look.name = profile.text
                    look.short_sleep()
                    self.iteration -= 1
                    look.find_name()


gl = global_looker(10)
gl.cycle()
