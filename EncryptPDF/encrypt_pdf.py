# Encrypt PDF
# pip install PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
writer = PdfFileWriter()
file = 'text_file.pdf'
reader = PdfFileReader(file)
for page in range(reader.numPages):
    writer.addPage(reader.getPage(page))
writer.encrypt('**********')
with open(f'text_file.pdf', 'wb') as f:
    writer.write(f)
print('PDF Encrypted')
