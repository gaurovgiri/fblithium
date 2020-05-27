I'm not responsible for any harm , lithium is just for educational purpose.

Requirements to run lithium: selenium and python 3.x (chromedriver already provided)

How to use fblithium.py ?
- open terminal in the same directory
- python3/python lithium.py
no need to open chromedriver.exe by yourself, program will run it

How to use lithium module ?

from lithium import Lithium 

Fbcracker = Lithium("fullpathtochromedriver/chromedriver.exe")
Fbcracker.Details("usernamehere","passwordfilehere")
Fbcracker.Inject() #to initiate dictionary attack


