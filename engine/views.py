from django.shortcuts import render

from lxml import etree

from docx import *

# Create your views here.
def home(request):
	document = Document('teste.docx')
	document.add_heading("teste")
	# document.save("teste.docx")
	return render(request, 'index.html')