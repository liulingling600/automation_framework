
# -*- coding:utf-8 -*-
import os.path
from selenium import webdriver
from framework.logger import Logger
import configparser

logger = Logger(logger="BrowserEngine").getlog()

class BrowerEngine(object):
    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        #读取conifg.ini文件
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        print(file_path)
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        Logger.info("Now, Close and quit the browser.")
        self.driver.quit()
