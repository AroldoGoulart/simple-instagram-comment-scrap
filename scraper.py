from selenium import webdriver
import time
import sys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url="https://www.instagram.com/"

driver.get(url) 

time.sleep (2)

"""
On the first project of me which we entered Twitter without using password,we use XPaths of
elements but in Instagram,when we refresh our website,id number of login url changes so we need
to use something different to use that link through Python Selenium. Either we can choose class name
or name selectors to use that.
"""
username=driver.find_element(By.NAME,"username")
username.send_keys ('add_user_name_here')

password =driver.find_element (By.NAME,"password")
password.send_keys('add_password_here')
password.submit()


time.sleep(4)



driver.get(sys.argv[1])

time.sleep(4)

import random
# load "sys.argv[2]" comments 
# role 1 - load comments
try:   
    count = 0
    while count < 1000:
        driver.execute_script("document.getElementsByClassName('x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x14vqqas xod5an3 x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1')[0].scrollIntoView();")
        randomTimeSleep = random.randint(1, 5)
        time.sleep(randomTimeSleep)
        count += 1
except Exception as e:
    print(e)
    pass


user_comments = []
user_names = []
# executar document.getElementsByClassName('x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')
comments_elements = driver.execute_script("return document.getElementsByClassName('x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj')")
print('comment:', len(comments_elements))
# remove first and last element
comment = comments_elements[1:-1]
isCommentTime = False
for c in comment:
    if(isCommentTime):
        user_comments.append(c.text)
        isCommentTime = False
    else:
        user_names.append(c.text)
        isCommentTime = True

# formar par de usuario e comentario 
# print(user_names)
# print(user_comments)
import excel_exporter
excel_exporter.export(user_names, user_comments)

driver.close()
