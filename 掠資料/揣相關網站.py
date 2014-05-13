import urllib
from 掠資料.GoogleScrape import scrape

class 揣相關網站:
	def 揣(self, 關鍵字, 幾筆=500):
		results = scrape(關鍵字, num_results_per_page=50, num_pages=(幾筆 - 1) // 50 + 1, offset=0)
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
if __name__ == '__main__':
	結果 = 揣相關網站().揣('無法度')
	print(結果)
