from selenium import webdriver
from src.pages.homepage import Homepage
from src.pages.signinpage import SignInPage

def test_browserstack():
    driver = webdriver.Chrome(executable_path="driver/chromedriver")
    driver.get("https://bstackdemo.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    driver.quit()