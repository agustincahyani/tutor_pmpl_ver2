from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_items(self):
		# Edith goes to the homepage and accidently tries to submit
		# an empty list item. She hits Enter on the empty input box
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# The home page refreshes, and there is an error message says
		# that list items cannot be blank
		error = self.browser.find_element_by_css_selector('.has-error')		

		# She tries again with some text for the item, which now works
		
		# Perversely, she now decides to submit a second blank list

		# She receives a similar warning on the list page

		# And she can correct it by filling some text in
		self.fail('write me!')
