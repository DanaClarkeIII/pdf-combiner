import os
from PyPDF2 import PdfMerger, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to get the number of pages in a PDF
def get_pdf_page_count(filename):
    reader = PdfReader(filename)
    return len(reader.pages)

# Function to create a table of contents PDF
def create_toc_pdf(pdf_files, toc_filename):
    c = canvas.Canvas(toc_filename, pagesize=letter)
    c.setFont("Helvetica", 10)  # Smaller font size
    c.drawString(100, 750, "Table of Contents")
    y = 730  # Adjusted starting position for the text
    page_num = 1  # Start with page number 1 for the first document after TOC

    for title in pdf_files:
        title_without_path = os.path.basename(title)  # Remove any directory path from title if present
        c.drawString(100, y, f"{title_without_path} ..... Page: {page_num}")
        y -= 12  # Adjust y position for the next entry
        page_num += get_pdf_page_count(title)  # Increment the page number by the count of pages in the current document

    c.save()

# Function to merge PDFs and include a table of contents
def merge_pdfs_with_toc(output):
    # List PDF files in the current working directory
    pdf_files = [file for file in os.listdir('.') if file.endswith('.pdf')]
    
    # Sort the files or arrange them in the order you prefer
    pdf_files.sort()

    # Create a table of contents PDF
    toc_filename = 'toc_temp.pdf'
    create_toc_pdf(pdf_files, toc_filename)

    # Start the merging process
    merger = PdfMerger()

    # Append the TOC first
    merger.append(toc_filename)

    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except FileNotFoundError as e:
            print(f"Error: The file {pdf} was not found.")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    # Write out the merged PDF
    merger.write(output)
    merger.close()

    # Remove the temporary TOC file
    os.remove(toc_filename)

    print(f"Merged PDF with TOC saved as {output}")

# Ask user for the desired output file name
output_pdf = 'merged.pdf'

# Call the function with the desired output file name
merge_pdfs_with_toc(output_pdf)
