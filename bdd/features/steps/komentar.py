from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

@given('I am opening the web page')
def impl(context):
	context.browser.get('http://agustin01.cloudapp.net')
	assert context.browser.title == "To-Do lists"

@when("I see 0 item's in my to do list")
def impl(context):
	table = context.browser.find_element_by_id('id_div_table')
	text1 = table.find_element_by_tag_name('p')
	assert text1.text == "Your to-do list goes here."

@when("I see 3 item's in my to do list")
def impl(context):
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('1 item')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('2 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('3 items')
	inputbox.send_keys(Keys.ENTER)
	items = context.browser.find_element_by_id('id_list_table')
	table = items.find_elements(By.TAG_NAME, 'tr')
	assert len(table) == 3

@when("I see 5 item's in my to do list")
def impl(context):
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('1 item')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('2 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('3 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('4 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('5 items')
	inputbox.send_keys(Keys.ENTER)
	items = context.browser.find_element_by_id('id_list_table')
	table = items.find_elements(By.TAG_NAME, 'tr')
	assert len(table) == 5

@then("I see a \"yey, waktunya berlibur\" about how busy i'm")
def impl(context):
	comment = context.browser.find_element_by_id('id_comment')
	assert comment.text == "yey, waktunya berlibur"


@then("I see a \"sibuk tapi santai\" about how busy i'm")
def impl(context):
	comment = context.browser.find_element_by_id('id_comment')
	assert comment.text == "sibuk tapi santai"

@then("I see a \"oh tidak\" about how busy i'm")
def impl(context):
	comment = context.browser.find_element_by_id('id_comment')
	assert comment.text == "oh tidak"

@when("I see 9 item's in my to do list")
def impl(context):
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('1 item')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('2 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('3 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('4 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('5 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('6 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('7 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('8 items')
	inputbox.send_keys(Keys.ENTER)
	time.sleep(1)
	inputbox = context.browser.find_element_by_id('id_new_item')
	inputbox.send_keys('9 items')
	inputbox.send_keys(Keys.ENTER)
	items = context.browser.find_element_by_id('id_list_table')
	table = items.find_elements(By.TAG_NAME, 'tr')
	assert len(table) == 9

@then('I see a "Semangat, kerja keras!" about how busy i\'m')
def impl(context):
	comment = context.browser.find_element_by_id('id_comment')
	assert comment.text == "oh tidak"