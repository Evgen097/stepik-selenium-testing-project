
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en", help="Choose language: ru, es, fr... Default: English")


@pytest.fixture(scope="function")
def browser(request):
	language = request.config.getoption("language")
	print("\n--------------------------------------")
	print(F"Check for language: {language}")
	
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': language})
	browser = webdriver.Chrome(options=options)
	
	yield browser
	browser.quit()
	print("\n--------------------------------------")
	
	
	