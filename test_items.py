import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_btn(browser):
    browser.get(link)

    time.sleep(30)

    add_to_cart_button = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
    )
    assert add_to_cart_button is not None, "Button to add item to cart not found"
