from .base import FunctionalTest

class BloggingAddressTest(FunctionalTest):

	def test_for_blogging_address(self):
		self.browser.get(self.server_url)
		blogging_box = self.browser.find_element_by_id('id_blog_address')
		self.assertIn('Please visit my blog at this address', blogging_box.text)

	def test_for_blogging_page(self):
		self.browser.get(self.server_url+"/blog/")
		self.assertIn('My Personal Blog', self.browser.title)
