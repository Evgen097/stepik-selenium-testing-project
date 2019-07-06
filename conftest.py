
import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default="en", help="Choose language: ru, es, fr... Default: English")


@pytest.fixture(scope="function")
def browser(request):
	language = request.config.getoption("language")
	print("\n--------------------------------------")
	print(F"Check for language: {language}")
	
	options = Options()
	browser = webdriver.Firefox(options=options)
	
	#opt = webdriver.ChromeOptions()
	#opt.add_experimental_option('w3c', False)
	#browser = webdriver.Chrome(chrome_options=opt)
	
	yield browser
	browser.quit()
	print("\n--------------------------------------")
	
	
	