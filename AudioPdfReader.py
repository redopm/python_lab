import PyPDF2
import pyttsx3

pdfFileobj = open ("myfile.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileobj)

mytext = ""

for pagenum in range(pdfReader.numpages):
    pageobj = pdfReader.getPage(pagenum)

    mytext += pageobj.extractText()

pdfFileobj.close()

engine = pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("voice", "en+m5")
engine.say(mytext)
engine.runAndWait()