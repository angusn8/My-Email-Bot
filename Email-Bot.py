from selenium import webdriver 
from time import sleep

class EmailBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://gmail.com')

        sleep(1.5)

        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys('angusn@allegheny.edu')

        next_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_btn.click()

        sleep(1.5)

        password_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password_in.send_keys('Statman8football')

        next_btn2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_btn2.click()

        sleep(50)

    def read_email(self):

        try:
            no_thanks = bot.driver.find_element_by_xpath('//*[@id="link_enable_notifications_hide"]')
            no_thanks.click()
        except:

            sleep(.5)
        
            drop_down = self.driver.find_element_by_xpath('//*[@id=":1p"]/div[1]/div')
            drop_down.click()

            unread = self.driver.find_element_by_xpath('//*[@id=":il"]/div')
            unread.click()

            mark_as_read = self.driver.find_element_by_xpath('//*[@id=":4"]/div/div[1]/div[1]/div/div/div[3]/div[1]/div')
            mark_as_read.click()

            drop_down.click()

            none = self.driver.find_element_by_xpath('//*[@id=":ij"]/div')
            none.click()

            sleep(3)

    def close_window(self):
        self.driver.close()

bot = EmailBot()

bot.login()

bot.read_email()

bot.close_window()

