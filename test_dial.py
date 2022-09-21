import base64
import os

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
    "appPackage": "com.android.dialer",
    "appActivity": "com.android.dialer.main.impl.MainActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capability)
touch = TouchAction(driver)

driver.start_recording_screen()


# click on recents contacts
# driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView').click()

# search for contact

def test_search_contact():
    driver.find_element(AppiumBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.TextView').click()
    driver.implicitly_wait(30)


# Pass a name
def test_pass_a_name():
    driver.find_element(AppiumBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.EditText').send_keys(
        'Michelle')


def test_press_search():
    driver.execute_script('mobile: performEditorAction', {'action': 'search'})


# Click on search on keyboard

def test_all_contacts_text():
    contact = driver.find_element(AppiumBy.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup[2]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.TextView').get_attribute(
        "text")
    assert contact == "All contacts"
    print(contact)


def test_click_back():
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="stop searching"]').click()


def test_click_contact():
    driver.find_element(AppiumBy.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ImageView').click()
    time.sleep(2)


def test_down_contacts():
    TouchAction(driver).press(x=465, y=670).move_to(x=459, y=568).release().perform()
    time.sleep(2)
    # if user wants to scroll down 5 times
    # for i in range(5):
    # TouchAction(driver).press(x=495, y=1683).move_to(x=474, y=711).release().perform()


def test_swipe_up_contacts():
    TouchAction(driver).press(x=474, y=477).move_to(x=474, y=588).release().perform()


# saving video recording
video_rawdata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_H%M%S")
filepath = os.path.join("/Users/dennis/PycharmProjects/AppiumTest/Screenshots/", video_name+".mp4")
with open(filepath, "wb+") as vd:
    vd.write(base64.b64decode(video_rawdata))
