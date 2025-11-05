import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from base_pages.Login_Admin_Page import Login_Admin_Page
from utilities.custom_logger import Log_Maker

class Test_01_Admin_login:
    admin_page_url = Read_Config().get_admin_page_url()
    username = Read_Config().get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config().get_invalid_username()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("********test_title_verification********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        if act_title == exp_title:
            self.logger.info("********title verification test passed********")
            assert True
            self.driver.close()
        else:
            self.logger.info("********title verification test failed********")
            self.driver.save_screenshot(".\\Screenshots\\test_title_verification.png")
            self.driver.close()
            assert False
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self,setup):
        self.logger.info("********test_valid_admin_login********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        error_message = self.driver.find_element(By.XPATH,"//div[@class='content-header']//h1").text
        if error_message == "Dashboard":
            self.logger.info("********test_valid_admin_login test passed********")
            assert True
            self.driver.close()
        else:
            self.logger.info("********test_valid_admin_login test failed********")
            self.driver.save_screenshot(".\\Screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False
    @pytest.mark.smoke
    def test_invalid_admin_login(self,setup):
        self.logger.info("********test_invalid_admin_login********")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        act_dashboard_text = self.driver.find_element(By.XPATH,"//li").text
        if act_dashboard_text == "No customer account found":
            self.logger.info("********test_invalid_admin_login test passed********")
            assert True
            self.driver.close()
        else:
            self.logger.info("********test_invalid_admin_login test failed********")
            self.driver.save_screenshot(".\\Screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False


