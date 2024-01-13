Extraction of pdf data
#import PyPDF2
def extract_text_from_pdf(pdf_path):
 text = ""
 with open(pdf_path, "rb") as file:
 pdf_reader = PyPDF2.PdfReader(file)
 num_pages = len(pdf_reader.pages)
 for page_num in range(num_pages):
 page = pdf_reader.pages[page_num]
 text += page.extract_text()
 return text
def main():
 # Replace 'your_pdf_file.pdf' with the path to your PDF file
 pdf_path = r'pdf path’
 # Extract text from PDF
 pdf_text = extract_text_from_pdf(pdf_path)
 # Display the extracted text
 print(pdf_text)
if _name_ == "_main_":
 main()


 
