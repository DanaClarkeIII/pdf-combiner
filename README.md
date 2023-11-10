# PDF Merger with Table of Contents

This Python script efficiently merges multiple PDF files within a directory and generates a table of contents (TOC) for easy navigation. This is particularly useful for consolidating documents into a single file while maintaining an organized structure.

## Features

- **Automated PDF Merging**: Merge all PDF files within the current working directory into a single document.
- **Dynamic Table of Contents**: Automatically generates a TOC with links to the starting page of each included PDF.
- **Customizable Output**: Easily specify the name of the merged output PDF file.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3
- PyPDF2 library
- reportlab library

You can install the required packages using:

```bash
pip install PyPDF2 reportlab
```

## Usage

Place the Script in Directory: Copy the script into the directory with the PDF files you want to merge.
Run the Script: Execute the script in your terminal or command prompt.
Specify Output File Name: When prompted, enter the desired name for the merged PDF file.
Access Merged PDF: Find the merged PDF, complete with a TOC, in the same directory.

## Example

To use this script, you will need to specify the output filename. Here is an example on how to call the function:

```
output_pdf = 'merged_document.pdf'
merge_pdfs_with_toc(output_pdf)
```

This will merge all PDF files in the current directory and create a file named 'merged_document.pdf'.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
