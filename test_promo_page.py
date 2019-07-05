
import time
import math
import pytest
from .pages.promo_page import PromoPage


link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


	
def test_should_be_promo_page(browser):
	page = PromoPage(browser, link)
	page.open()
	page.should_be_promo_in_url()
	page.should_be_add_basket_button()	
	time.sleep(1)



def test_guest_can_add_product_to_cart(browser):
	page = PromoPage(browser, link)
	page.open()
	time.sleep(1)
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	time.sleep(1)
	
	page.should_be_success_massage_after_add_basket()
	page.should_success_message_contain_product_name()
	
	page.should_cost_of_basket_coincides_with_product_price()
	time.sleep(1)	


@pytest.mark.skip
def test_price(browser):
	page = PromoPage(browser, link)
	page.open()
	time.sleep(1)
		
	page.should_cost_of_basket_coincides_with_product_price()
	time.sleep(1)		

# pytest -v --tb=line --language=en test_main_page.py









