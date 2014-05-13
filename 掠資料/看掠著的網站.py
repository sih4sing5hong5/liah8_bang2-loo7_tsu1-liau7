from urllib.request import urlopen
import html2text
import os

class 看掠著的網站:
	def 對網頁看(self, 網址):
		with urlopen(網址) as 資料:
			return self.提網頁文字出來(資料.read().decode('utf-8'))
	def 對檔案看(self, 檔名):
		with open(檔名) as 資料:
			return self.提網頁文字出來(資料.read())
	def 對資料夾看(self, 路徑):
		資料 = []
		for (所在, 資料夾, 檔案) in os.walk(路徑):
			for 檔名 in 檔案:
				if 檔名.endswith('.html'):
					資料.append(self.對檔案看(所在 + '/' + 檔名))
		return '\n\n'.join(資料)
	def 提網頁文字出來(self, 網頁html):
		return html2text.html2text(網頁html).strip()

if __name__ == '__main__':
	print(看掠著的網站().對網頁看("http://taigu.fhl.net/index.html"))
	print(看掠著的網站().對資料夾看('../網頁資料'))
