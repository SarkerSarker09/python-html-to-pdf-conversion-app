import pdfkit



def makePdfFromHtmlFile():
	try:
			pdfkit.from_file('test.html', 'test01.pdf')
			print('generated test01.pdf')
	except:
			print('test01.pdf cannot generate')		



def makePdfFromWebsiteUrl():
	try:
			pdfkit.from_url('https://google.com/', 'test02.pdf')
			print('test02.pdf generated')
	except:
			print('test02.pdf cannot generate')









makePdfFromHtmlFile()
makePdfFromWebsiteUrl()