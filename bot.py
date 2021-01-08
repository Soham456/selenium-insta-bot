from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from password import pw,un
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
driver.implicitly_wait(5)
action = ActionChains(driver)

#Posts
def like():
    posts=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span").get_attribute("innerHTML")    
    pics=int(posts)-1
    print(posts) 
    print(pics)
    if(int(posts) != 0):
        try:
            driver.find_element_by_class_name('_9AhH0').click()              
            like = driver.find_element_by_class_name('fr66n')
            soup = bs(like.get_attribute('innerHTML'),'html.parser')
            if(soup.find('svg')['aria-label'] == 'Like'):
                like.click()                             
            #next of first img
            if (pics != 0):                    
                driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
        except NoSuchElementException :
            if (pics != 0):                    
                driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a').click()
            else:
                pass
            #driver.find_element_by_xpath('/html/body/div[5]/div[3]/button/div').click()
            #driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div').click()                  
                        
        while(pics > 0):                                          
            #like
            try:
                like = driver.find_element_by_class_name('fr66n')
                soup = bs(like.get_attribute('innerHTML'),'html.parser')
                if(soup.find('svg')['aria-label'] == 'Like' ):
                    like.click()                                       
                if(pics != 1):
                    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click() #Next 
                #time.sleep(2)
                pics -= 1
                print(pics)
                continue
            except NoSuchElementException :
                pics -= 1
                #if(pics==0): break
                print("lookinkg for next-->",pics)
                if(pics!=0):
                    driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]').click()                    
                continue
        #Cancel the loop                 
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div').click()                              
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div').click()        

def person(a):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(a)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div[2]/div/span').click()
    like()

def following():
    #Profile                       
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    
    scroll_box= driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
    last_el,ht = 0,1 
    while last_el != ht:
        last_el = ht
        time.sleep(3)
        ht=driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight;' ,scroll_box) 
        links = scroll_box.find_elements_by_tag_name('a')
        #names =[name.text for name in links if name.text !=''] 
        try:
            names =[name.text for name in links if name.text !='']
            continue
        except StaleElementReferenceException :
            print("try again bitch!!")
            ht=driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight;' ,scroll_box)
            continue
    
    count = 0
    for i in names:
        print(i)
        count+=1
    print("Number of friends are-->", count)

    driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button/div').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]').click()
    for i in names:
        print("Username -->",i)
        person(i)
    

#Login
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(un)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pw,Keys.ENTER)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


#like()
#person('sanjay_sawadkar7')
following()
#sanket07__
