import urllib
from 掠資料.GoogleScrape import scrape

class 揣相關網站:
	def 揣(self, 關鍵字, 幾筆=500):
		results = scrape(關鍵字, num_results_per_page=25, num_pages=(幾筆 - 1) // 25 + 1, offset=0, search_params=self._SEARCH_PARAMS,)
		結果 = []
		for page in results:
			for link_title, link_snippet, link_url in page['results']:
				try:
					結果.append(
						(link_title,
						urllib.parse.unquote(link_url.geturl()),
						link_snippet,)
					)
				except:
					pass
		return 結果
	
	# http://www.rankpanel.com/blog/google-search-parameters/
	_SEARCH_PARAMS = {
		'start': '0',  # Specifies the index number of the first entry in the result set that is to be returned. page number = (start / num) + 1
		              # The maximum number of results available for a query is 1,000, i.e., the value of the start parameter added to the value of the num parameter cannot exceed 1,000.
		'rc': '',  # Request an accurate result count for up to 1M documents. If a user submits a search query without the site parameter, the entire search index is queried.
		'site': None,  # Limits search results to the contents of the specified collection.
		'sort': None,  # Specifies a sorting method. Results can be sorted by date.
		'client': None,  # required parameter. Indicates a valid front end.
		'output': None,  # required parameter. Selects the format of the search results.
		'partialfields': None,  # Restricts the search results to documents with meta tags whose values contain the specified words or phrases.
		'pws': '0',  # personalization turned off
		'complete': 0,  # Turn auto-suggest and Google Instant on (=1) or off (=0)
		'nfpr': 1,  # Turn off auto-correction of spelling
		'ncr': 1,  # No country redirect: Allows you to set the Google country engine you would like to use despite your current geographic location.
		'safe': 'off',  # Turns the adult content filter on or off
		'rls': None,  # Source of query with version of the client and language set, other examples are can be found
		'lr': 'lang_tw',  # Restricts searches to pages in the specified language. If there are no results in the specified language, the search appliance displays results in all languages .
		                 # lang_xx where xx is the country code such as en, de, fr, ca, ...
		'hl': 'tw',  # Language settings passed down by your browser
		'cr': 'countryTW',  # The region the results should come from
		'gl': 'tw',  # as if the search was conducted in a specified location. Can be unreliable.
		'ie': 'utf-8',  # Sets the character encoding that is used to interpret the query string.
		'oe': 'utf-8'  # Sets the character encoding that is used to encode the results.
		}
if __name__ == '__main__':
	結果 = 揣相關網站().揣('無法度 台語 閩南語', 幾筆=25)
	for 一筆 in 結果[:8]:
		print(一筆[0])
	print(len(結果))
	print(len(set(結果)))
