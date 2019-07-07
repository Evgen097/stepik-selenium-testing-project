

import time
import math

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException # в начале файла


from .base_page import BasePage
from .locators import PromoPageLocators

from .cart_page import CartPage
from .locators import CartPageLocators


class PromoPage(BasePage):

#	def should_not_be_success_message(self):
#		assert not self.is_element_present(*PromoPageLocators.ALERT_SUCCESS), "Success message is presented"


	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False
	

	def is_disappeared(self, how, what, timeout=4):
		try:
			#print('----------------------------------------')
			#print('----------------------------------------')
			#print(how)
			#print(what)
			#print(timeout)
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True

	
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*PromoPageLocators.ALERT_SUCCESS), "Success message is presented, but should not be"	
	
	
	def should_is_disappeared_the_success_message(self):
		assert self.is_disappeared(*PromoPageLocators.ALERT_SUCCESS), "Проверяем, что нет сообщения об успехе с помощью is_disappeared"	
	

	def should_be_success_massage_after_add_basket(self):
		alert_success = self.browser.find_element(*PromoPageLocators.ALERT_SUCCESS)
	
	
	def should_success_message_contain_product_name(self):
		alert_success = self.browser.find_element(*PromoPageLocators.ALERT_SUCCESS)
		product_name = self.browser.find_element(*PromoPageLocators.PRODUCT_NAME)
		#print('--------------------------------------------------------------')
		#print('--------------------------------------------------------------')

		#print(alert_success.text)
		#print(product_name.text+' has been added to your basket.')
		#print(alert_success.text == (product_name.text+' has been added to your basket.'))
		#print(len(alert_success.text.strip()), len((product_name.text.strip())+' has been added to your basket.'))

		assert (alert_success.text.endswith(product_name.text + " has been added to your basket.")), "The the succes message must ends with: has been added to your basket."

		#Coders at Work был добавлен в вашу корзину.
		#Coders at Work has been added to your basket.
		#Coders at Work book has been added to your basket.



	def should_cost_of_basket_coincides_with_product_price(self):
		basket_mini = self.browser.find_element(*PromoPageLocators.BASKET_MINI)
		product_price = self.browser.find_element(*PromoPageLocators.PRODUCT_PRICE)
		
		product_price_text = product_price.text.split(' ')[0]
		basket_mini_text = basket_mini.text.split(' ')[2]
		
		#print('--------------------------------------------------------------')
		#print('--------------------------------------------------------------')

		#print(product_price_text)
		#print(basket_mini_text)
		#print(basket_mini_text.startswith(product_price_text))
		
		assert (basket_mini_text.startswith(product_price_text)), "The cost of basket should coincides with product price"
	
	
	def should_be_promo_in_url(self):
		# реализуйте проверку на корректный url адрес
		assert ("?promo=" in self.browser.current_url), "Verifying that the URL address contains ?promo="
	
	
	def should_be_add_basket_button(self):
		add_basket_btn = self.browser.find_element(*PromoPageLocators.ADD_BUTTON)
		assert (add_basket_btn.text), "Verifying that add_basket_btn contains text"


	def add_to_basket(self):
		add_basket_btn = self.browser.find_element(*PromoPageLocators.ADD_BUTTON)
		add_basket_btn.click()
		time.sleep(1)


	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			print("Your code: {}".format(alert.text))
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")



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
			




