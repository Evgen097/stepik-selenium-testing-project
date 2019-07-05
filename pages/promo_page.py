

import time
import math

from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PromoPageLocators

from selenium.common.exceptions import NoAlertPresentException # в начале файла



class PromoPage(BasePage):

	def should_be_success_massage_after_add_basket(self):
		alert_success = self.browser.find_element(*PromoPageLocators.ALERT_SUCCESS)
	
	
	def should_success_message_contain_product_name(self):
		alert_success = self.browser.find_element(*PromoPageLocators.ALERT_SUCCESS)
		product_name = self.browser.find_element(*PromoPageLocators.PRODUCT_NAME)
		assert (product_name.text in alert_success.text), "The name of the product in the message must match the added product"


	def should_cost_of_basket_coincides_with_product_price(self):
		basket_mini = self.browser.find_element(*PromoPageLocators.BASKET_MINI)
		product_price = self.browser.find_element(*PromoPageLocators.PRODUCT_PRICE)
		
		product_price_text = product_price.text.split(' ')[0]
		basket_mini_text = basket_mini.text.split(' ')[3]
		
		#print(f'product_price_text: {product_price_text}')
		#print(f"product_price_text: {product_price.text}")
		#print(f'basket_mini_text: {basket_mini_text}')
		#time.sleep(100)	
		
		assert (product_price_text == basket_mini_text), "The cost of basket should coincides with product price"

	

		
		#assert (product_name.text in alert_success.text), "The name of the product in the message must match the added product"

	
	
	
	def should_be_promo_in_url(self):
		# реализуйте проверку на корректный url адрес
		assert ("?promo=newYear" in self.browser.current_url), "Verifying that the URL address contains ?promo=newYear"
	
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








