from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import pytest
import time

desired_capability = {
    "deviceName": "Android Emulator",
    "udid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "11.0",
    "appPackage": "com.android.camera2",
    "appActivity": "com.android.camera.CameraLauncher"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capability)
touch = TouchAction(driver)


def test_intro():
    intro = driver.find_element(AppiumBy.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView").get_attribute(
        'text')
    assert intro == 'Remember photo locations?'


def test_tag():
    tag = driver.find_element(AppiumBy.ID,
                              'com.android.camera2:id/check_box').get_attribute(
        'text')
    assert tag == "Tag your photos and videos with the locations where they're taken."


def test_click_next():
    driver.find_element(AppiumBy.ID, 'com.android.camera2:id/confirm_button').click()
    time.sleep(2)
    driver.quit()

