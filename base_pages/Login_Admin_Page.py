from selenium.webdriver.common.by import By


class Login_Admin_Page:
    text_username_id = "Email"
    text_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID,self.text_username_id).clear()
        self.driver.find_element(By.ID,self.text_username_id).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.ID,self.text_password_id).clear()
        self.driver.find_element(By.ID,self.text_password_id).send_keys(password)
    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()