from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "platformName": "Android",
  "appium:deviceName": "RFCX50S71RH",
  "appium:automationName": "UiAutomator2",
  "appPackage": "com.google.android.youtube",
  "appActivity": "com.google.android.youtube.app.honeycomb.Shell$HomeActivity"
}

options = UiAutomator2Options().load_capabilities(desired_cap)

driver = webdriver.Remote(
    command_executor="http://localhost:4723",
    options=options
)

driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Search"]').click()

