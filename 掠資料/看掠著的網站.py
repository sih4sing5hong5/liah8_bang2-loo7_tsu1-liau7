from urllib.request import urlopen
import html2text

class 看掠著的網站:
	def 對網頁看(self,網址):
		with urlopen(網址) as 資料:
			return self.提網頁文字出來(資料.read().decode('utf-8'))
	def 對檔案看(self,檔名):
		with open(檔名) as 資料:
			return self.提網頁文字出來(資料.read())
	def 提網頁文字出來(self,網頁html):
		return html2text.html2text(網頁html)

if __name__=='__main__':
	print(看掠著的網站().對網頁看("http://taigu.fhl.net/index.html"))