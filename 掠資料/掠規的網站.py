import os

class 掠規的網站:
	指令樣版 = 'wget  --mirror --no-parent -r '\
		'--restrict-file-names=nocontrol --adjust-extension '\
		'-R css,js,png,jpg,gif,tiff,gz,bz '\
		'--directory-prefix={2} '\
		'--wait={1} --random-wait '\
		'{0}'
	def 掠(self, 網址, 等待時間=1.0, 資料夾='../網頁資料'):
		指令 = self.指令樣版.format(網址, 等待時間, 資料夾)
		os.system(指令)

if __name__=='__main__':
	掠規的網站().掠('xn--v0qr21b.xn--kpry57d/產品資訊')
