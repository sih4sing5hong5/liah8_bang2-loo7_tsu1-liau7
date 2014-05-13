from urllib.request import urlopen
import html2text
import os
import subprocess

class 看掠著的網站:
	def 對網頁看(self, 網址):
		with urlopen(網址) as 資料:
			return self.提網頁文字出來(資料.read().decode('utf-8'))
	def 對檔案看(self, 檔名):
		print(檔名)
		try:
			with open(檔名) as 資料:
				return self.提網頁文字出來(資料.read())
		except:
			轉碼過 = subprocess.check_output(
				["iconv", '-c',
				 '-f', 'big5', '-t', 'utf-8',
				 檔名],
				universal_newlines=True)
# 			print(轉碼過)
			return self.提網頁文字出來(轉碼過)
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
# 	print(看掠著的網站().對網頁看("http://taigu.fhl.net/index.html"))
# 	print(看掠著的網站().對資料夾看('../網頁資料'))
	print(看掠著的網站().提網頁文字出來(
	"""
	<p style='layout-grid-mode: char; margin-top:5px; margin-bottom:5px'>
<font size="3"><font face="Taigi Unicode">旭</font><span lang="EN-NZ" style="font-family: Taigi Unicode; ">--á 
kap</span><font face="Taigi Unicode">董</font><span lang="EN-NZ" style="font-family: Taigi Unicode; ">--ê</span></font><font FACE="新細明體" LANG="ZH-TW"><span lang="EN-US" style="font-family: Taigi Unicode"><font size="3"> 
/ Ui-chì</font></span></font><span lang="EN-US" style="font-family: Taiwanese Serif"><FONT FACE="Taigi Unicode" LANG="ZH-TW"><o:p><font size="3">
</font>
      </o:p>
</FONT></span></p>
"""
))