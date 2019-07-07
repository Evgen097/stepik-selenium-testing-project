
import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

	def should_be_basket_url(self):
		# реализуйте проверку на корректный url адрес
		assert (self.browser.current_url.endswith("basket/")), "Verifying that the URL address contains basket"


	def should_page_contain_basket_headline(self):
		try:
			basket_headline = self.browser.find_element(*CartPageLocators.PAGE_HEADLINE)
		except:
			raise ValueError('should_page_contain_basket_headline')



	def should_be_the_basket_empty(self):
		assert self.is_not_element_present(*CartPageLocators.BASKET_ITEMS), "We expect no items in the basket"


	def is_not_element_present(self, css,  what):
		try:
			basket_items = self.browser.find_element_by_css_selector(what)
		except:
			return True	
		return False



	def should_be_text_that_cart_is_empty(self):
		print(*CartPageLocators.BASKET_EMPTY_MESSAGE)
		basket_empty_message = self.browser.find_element(*CartPageLocators.BASKET_EMPTY_MESSAGE)
		assert ( "Your basket is empty" in basket_empty_message.text), "We expect that there is a text that the basket is empty."





















