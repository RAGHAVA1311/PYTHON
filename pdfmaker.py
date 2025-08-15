from PyPDF2 import PdfMerger

# List of PDF files to merge
pdfs = ["file1.pdf", "file2.pdf", "file3.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
