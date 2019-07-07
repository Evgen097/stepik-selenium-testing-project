
from selenium.webdriver.common.by import By



class PromoPageLocators(object):
	ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
	ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert.alert-success")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	CART_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn")


class CartPageLocators(object):
	PAGE_HEADLINE = (By.CSS_SELECTOR, ".page-header h1")
	BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators(object):
	PAGE = (By.CSS_SELECTOR, "h1")









