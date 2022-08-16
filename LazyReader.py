import pyttsx3
import PyPDF2
book = open(r"F:\Books\Little Women ( PDFDrive ).pdf", "rb")    #PDF USED opened in 'rb' mode
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)   #Voice used is female, for male voice speaker.setProperty('voice', voices[0].id)
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)
speaker.setProperty('rate', 125) 
for i in range(_startpage_, _endpage_):
    start_page = pdfreader.getPage(i)
    text = start_page.extractText()
    speaker.say(text)
    speaker.runAndWait()
