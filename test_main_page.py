
import time
import math
import pytest


from .pages.main_page import MainPage




link = "http://selenium1py.pythonanywhere.com"


#def test_guest_can_go_to_login_page(browser):
#	page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#	page.open()                      # открываем страницу
#	page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
#	time.sleep(1)
	
@pytest.mark.skip	
def test_guest_should_see_login_link(browser):
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()	
	time.sleep(1)

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
#	link = "http://selenium1py.pythonanywhere.com"
	page = MainPage(browser, link)
	page.open()
	login_page = page.go_to_login_page()
	login_page.should_be_login_form()
		

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
	#Гость открывает главную страницу 
	#Переходит в корзину по кнопке в шапке сайта
	#Ожидаем, что в корзине нет товаров
	#Ожидаем, что есть текст о том что корзина пуста 	
	link = "http://selenium1py.pythonanywhere.com"	
	
	page = MainPage(browser, link)
	page.open()
	time.sleep(1)
	
	basket_page = page.go_to_cart_page()
	time.sleep(1)
	page.should_be_cart_page()
	page.should_be_cart_basket_empty()
	page.should_be_text_that_cart_is_empty()



	
# pytest  -s -v -rsx --language=en test_main_page.py
# pytest -v --tb=line --language=en test_main_page.py









