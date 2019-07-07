
import time
from selenium.common.exceptions import (NoSuchElementException)
from .locators import BasePageLocators


class BasePage(object):


	def __init__(self, browser, url):
		self.browser = browser
		self.url = url
		
		
	def open(self):
		self.browser.get(self.url)
		time.sleep(1)


	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True
		
		
	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()


	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


	def go_to_cart_page(self):
		link = self.browser.find_element(*BasePageLocators.CART_BUTTON)
		link.click()

	def should_be_cart_button(self):
		assert self.is_element_present(*BasePageLocators.CART_BUTTON), "CART BUTTON is not presented"

















