

import time
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage
from .locators import MainPageLocators
from .locators import CartPageLocators

class MainPage(BasePage):


	def should_be_cart_page(self):
		try:
			cart_page = CartPage(browser=self.browser, url=self.browser.current_url)
			cart_page.should_be_basket_url()
		except AssertionError as error:
			print(error)
			raise ValueError('should move from the main page to the cart page after check url')
			
						
	def should_be_cart_basket_empty(self):
		try:
			cart_page = CartPage(browser=self.browser, url=self.browser.current_url)
			cart_page.should_be_the_basket_empty()
		except AssertionError as error:
			print(error)
			raise ValueError('should move from the main page to the cart page after what basket is empty')
					
			
	def should_be_text_that_cart_is_empty(self):
		try:
			cart_page = CartPage(browser=self.browser, url=self.browser.current_url)
			cart_page.should_be_text_that_cart_is_empty()

		except AssertionError as error:
			print(error)
			raise ValueError('should move from the main page to the cart page after check text that cart is empty')
			

