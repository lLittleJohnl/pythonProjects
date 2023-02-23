import aspose.words as aw

doc = aw.Document(r'C:\Users\joaov\Documentos\Github\Python\projetos\pdf_converter\teste.pdf')

# Save the document in DOCX format. Save format is automatically determined from the file extension.
doc.save("teste.docx")

# https://pypi.org/project/aspose-words/#:~:text=Aspose.,formats%20without%20needing%20Office%20Automation.
# https://code.visualstudio.com/docs/python/environments
# https://www.youtube.com/watch?v=CLlwYuFe1aA