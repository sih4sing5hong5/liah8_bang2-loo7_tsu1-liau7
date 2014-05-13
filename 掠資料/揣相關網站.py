import urllib
from 掠資料.GoogleScrape import scrape

class 揣相關網站:
	def 揣(self,關鍵字):
		
		results = scrape(關鍵字, num_results_per_page=50, num_pages=3, offset=0)
		for page in results:
			for link_title, link_snippet, link_url in page['results']:
				# You can access all parts of the search results like that
				# link_url.scheme => URL scheme specifier (Ex: 'http')
				# link_url.netloc => Network location part (Ex: 'www.python.org')
				# link_url.path => URL scheme specifier (Ex: ''help/Python.html'')
				# link_url.params => Parameters for last path element
				# link_url.query => Query component
				try:
					print(urllib.parse.unquote(link_url.geturl())) # This reassembles the parts of the url to the whole thing
				except:
					pass
				# How many hits has google found with our keyword (as shown on the first page)?
		print(results[0]['num_results_for_kw'])