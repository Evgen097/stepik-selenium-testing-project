
import time
import math
import pytest
from .pages.promo_page import PromoPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"

#@pytest.mark.parametrize('offer', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


@pytest.mark.skip
def test_should_be_promo_page(browser, offer):
	page = PromoPage(browser, link+offer)
	page.open()
	time.sleep(1)
	
	page.should_be_promo_in_url()
	page.should_be_add_basket_button()	


@pytest.mark.parametrize('offer', ["7", "0"])
@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser, offer):
	page = PromoPage(browser, link+offer)
	page.open()
	time.sleep(1)
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	time.sleep(1)
	
	page.should_be_success_massage_after_add_basket()
	page.should_success_message_contain_product_name()
	
	page.should_cost_of_basket_coincides_with_product_price()
	time.sleep(0)	


@pytest.mark.skip
def test_something(browser):
	page = PromoPage(browser, link)
	page.open()
	time.sleep(1)
		
	page.should_not_be_success_message()
	time.sleep(0)	


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#Открываем страницу товара 
#Добавляем товар в корзину 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present	
	page = PromoPage(browser, link)
	page.open()
	time.sleep(1)
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
#Открываем страницу товара 
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page = PromoPage(browser, link)
	page.open()
	page.should_not_be_success_message()



def test_message_disappeared_after_adding_product_to_cart(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
	page = PromoPage(browser, link)
	page.open()
	time.sleep(1)
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	time.sleep(1)
	page.should_is_disappeared_the_success_message()








# pytest -v --tb=line --language=en test_main_page.py









