import time
from selenium import webdriver
from pyvirtualdisplay import Display


display = Display(visible=0, size=(800, 800))  
display.start()

# driver = webdriver.Chrome()
# driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()

def login(email, password):
    """ Logging into our own profile """

    global driver
    
    options = Options()

    #  Code to disable notifications pop up of Chrome Browser
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    # options.add_argument("headless")

    try:
        driver = webdriver.Chrome(
            executable_path="/usr/bin/chromedriver", options=options)
        print("try webdrive", driver)

    except Exception:
        # print("your chromedriver",Driver,"\nchrome path",chromedriver_versions[platform_])
        print("webdrive", webdriver.Chrome(executable_path=chromedriver_versions[platform_], options=options ))
        print(
            "Kindly replace the Chrome Web Driver with the latest one from "
            "http://chromedriver.chromium.org/downloads "
            "and also make sure you have the latest Chrome Browser version."
            "\nYour OS: {}".format(platform_)
        )
        exit(1)   
    print("going on facebook")
    fb_path = facebook_https_prefix + "facebook.com"
    driver.get(fb_path)
    driver.maximize_window()
    print("on facebook site")
    # filling the form
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)

    try:
        # clicking on login button
        driver.find_element_by_id("loginbutton").click()
    except NoSuchElementException:
        # Facebook new design
        driver.find_element_by_name("login").click()

    # if your account uses multi factor authentication
    mfa_code_input = safe_find_element_by_id(driver, "approvals_code")

    if mfa_code_input is None:
        return

    mfa_code_input.send_keys(input("Enter MFA code: "))
    driver.find_element_by_id("checkpointSubmitButton").click()

    # there are so many screens asking you to verify things. Just skip them all
    while safe_find_element_by_id(driver, "checkpointSubmitButton") is not None:
        dont_save_browser_radio = safe_find_element_by_id(driver, "u_0_3")
        if dont_save_browser_radio is not None:
            dont_save_browser_radio.click()

        driver.find_element_by_id("checkpointSubmitButton").click()

# email = "madmag111@gmail.com"
# password = "hugwy0-wobqyf-xypVuf"
# login(email, password)
i = -10
for i in range(0,5):
	i+=1
	if i in (1,2,3):
		print("i",i)