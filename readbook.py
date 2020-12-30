import pyttsx3
import PyPDF2
book = open('Press_Note_Bihar_2020.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(51, pages):
	page = pdfReader.getPage(num)
	text = page.extractText()
	speaker.say(text)
	speaker.runAndWait()