import os
import pyttsx3
import PyPDF2

BOOK_PATH = r"C:\Users\Uchek\OneDrive\Documents\Book\Poem\Notes_200728_235402.pdf"


if __name__ == "__main__":
    book = open(BOOK_PATH, 'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    speaker = pyttsx3.init()
    for item in range(pages):
        page = pdfreader.getPage(item)
        text = ''
        for i in page:
            text = page.extractText()

    speaker.say(text)
    speaker.runAndWait()
