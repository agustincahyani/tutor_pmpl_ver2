from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

	def test_layout_and_styling(self):
		# Edith goes to the home page
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024, 768)

		# she notices the input inbox is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width']/2,
			512,
			delta=5
		)

		# She starts a new list and sees the input is nicely
		# centered there too
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)

		tablebox = self.browser.find_element_by_id('id_list_table')
		self.assertAlmostEqual(
			tablebox.location['x'] + tablebox.size['width'] / 2,
			512,
			delta=5
		)