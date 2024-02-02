# Selenium version: 4.17.2
# Chrome version: 121.0.6167.86 
#------------------------------
# Script's expected behaviour
#  1) Open Chrome browser
#  2) Navigate to google.com
#  3) Enter "Centennial College" into the Google search box
#  4) Execute search
#  5) On the search results page, click on the link that reads "Centennial College - Centennial College"
#  6) Click on the "Have Questions" box (bottom right-hand corner of the page)
#  7) Select "I'm planning on applying"
#  8) Click the "Canadian" button
#  9) Enter a question
# 10) Enter first name
# 11) Enter last name
# 12) Enter email
# 13) Enter confirm email
# 14) Pause execution for 20 seconds and manually solve CAPTCHA (this is the only step that requires user intervention)
# 15) Click Submit
#------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()

# Keep Chrome browser open after the script completes execution
chrome_options.add_experimental_option("detach", True)

# Assign instance of webdriver to driver    
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to google.com
    driver.get('https://www.google.com/')
    
    # Verify page title
    title = driver.title
    assert title == 'Google'
    
    # Identify Google search box
    search_box = driver.find_element(By.NAME, 'q')
                                      # name = "q"
    # Enter search term
    search_box.send_keys('Centennial College')
    
    # Do search
    search_box.submit()
    
    title = driver.title
    assert title == 'Centennial College - Google Search'
    
    # CSS_SELECTOR can be used to search for values like 'div > p'. However,
    # CSS_SELECTOR has a unique feature that allows it to reference an
    # element's name by inserting a dot before the name and replacing all 
    # empty spaces with dots.
    #
    # On the Google search result page, the link with the title 
    # "Centennial College - Centennial College" has an h3 class with the name
    # LC20lb MBeuO DKV0Md.
    link = driver.find_element(By.CSS_SELECTOR, '.LC20lb.MBeuO.DKV0Md')
                                        # class = "LC20lb MBeuO DKV0Md"
    link.click()
    
    title = driver.title
    assert title == 'Centennial College - Centennial College'
    
    # Click the "Have Questions" box
    questions = driver.find_element(By.CSS_SELECTOR, '.sc-jJoQJp.jWzbxV.sc-gWXbKe.sc-jEieoE.gTrCCI.fCHTAS.sc-cnTVOG.Kfjgq')
    questions.click()
    
    # Select the third index in the "Topic" dropdown - "I'm planning on applying"
    # Index is based 0
    select_topic = driver.find_element(By.NAME, 'mainTopicId')
    select = Select(select_topic)
    select.select_by_index(3)
    
    # Click the "Canadian" button with ActionChains 
    #
    # XPATH breakdown - //input[@id="studentTypeCanadianCanadian"]
    # // - current node
    # input - tag name
    # @id - input tag's id attribute
    # "studentTypeCanadianCanadian" - id attribute's value
    canadian_button = driver.find_element(By.XPATH, '//input[@id="studentTypeCanadianCanadian"]')
    actions = ActionChains(driver)
    actions.click(canadian_button).perform()

    # Enter question
    question_text_area = driver.find_element(By.NAME, 'question')
    question_text_area.send_keys('What are all the programs that Centennial offers?')
    
    # Enter first name
    first_name_textbox = driver.find_element(By.NAME, 'firstName')
    first_name_textbox.send_keys('John')
    
    # Enter last name
    last_name_textbox = driver.find_element(By.NAME, 'lastName')
    last_name_textbox.send_keys('Doe')
    
    # Enter email address
    email_textbox = driver.find_element(By.NAME, 'emailAddress')
    email_textbox.send_keys('John.Doe@email.com')
    
    # Enter confirm email
    confirm_email_textbox = driver.find_element(By.NAME, 'emailAddressConfirm')
    confirm_email_textbox.send_keys('John.Doe@email.com')

    # Selenium documentation recommends that CAPTCHA elements be deactivated 
    # during testing. However, I do not have access to the website's 
    # development environment. For the purposes of this demo, pause the script 
    # execution for 20 seconds and manually solve the CAPTCHA element.    
    time.sleep(20)
    
    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, '.sc-jJoQJp.jWzbxV.sc-gWXbKe.sc-hrjYtz.kySGUu.ldRmeA')
    submit_button.click()

    confirmation_message = driver.find_element(By.CSS_SELECTOR, '.sc-hiwPVj.gokfdU')
    value = confirmation_message.text
    
    assert value == "HAVE QUESTIONS?"
    
    print('Execution succeeded')
except:
    print('Execution failed')