from urllib.request import urlopen
import lxml.html
import lxml.html.clean
import html2text

class 看掠著的網站:
	def 對網頁提(self,網址):
		with urlopen(網址) as data:
			return self.提網頁文字出來(data.read().decode('utf-8'))
	def 提網頁文字出來(self,網頁html):
		return html2text.html2text(網頁html)

if __name__=='__main__':
	看掠著的網站().對網頁提("http://taigu.fhl.net/index.html")