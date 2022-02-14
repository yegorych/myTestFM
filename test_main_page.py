import time

import pytest

from page_obj.pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
         assert False

    def test_guest_should_see_login_link(self, browser):
         pass

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_empty_basket_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.should_be_empty_basket_message()






# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# # def test__login_page_is_correct(browser):
# #     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
# #     page = LoginPage(browser, link)
# #     page.open()
# #     page.should_be_login_page()

