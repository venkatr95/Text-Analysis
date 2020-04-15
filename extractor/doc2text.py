import os
from docx import Document

dir = os.path.dirname(__file__)
filepath = dir + '/data/'

def convertDocxToText(filename):
	filename = filepath + filename
	document = Document(filename)
	return "\n".join([para.text for para in document.paragraphs])

lines = convertDocxToText("cover.docx")
print(lines)