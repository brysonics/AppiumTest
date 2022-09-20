from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import pytest

desired_capability = {
    "deviceName": "Android Emulator",
    "udid": "emulator-5554",
    "platformName": "Android",
    "platformVersion": "11.0",
    "appPackage": "com.android.dialer",
    "appActivity": "com.android.dialer.main.impl.MainActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capability)


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
