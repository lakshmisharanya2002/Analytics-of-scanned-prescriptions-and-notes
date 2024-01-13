import PyPDF2
import pandas as pd
def extract_text_from_pdf(pdf_path):
 text = ""
 with open(pdf_path, "rb") as file:
 pdf_reader = PyPDF2.PdfReader(file)
 num_pages = len(pdf_reader.pages)
 for page_num in range(num_pages):
 page = pdf_reader.pages[page_num]
 text += page.extract_text()
 return text
def save_to_excel(data, excel_path):
 df = pd.DataFrame(data)
 df.to_excel(excel_path, index=False)
def main():
 # Replace 'your_pdf_file.pdf' with the path to your PDF file
 pdf_path = r'pdf path'
 # Extract text from PDF
 pdf_text = extract_text_from_pdf(pdf_path)
 # Split the text into lines and process as needed
 # For demonstration, splitting the text by lines
 lines = pdf_text.split('\n')
 # Assuming you have a list of lists where each sublist represents a row of data
 # For demonstration, creating a simple example
 data = [line.split() for line in lines if line.strip()]
 
# Specify a different Excel file path
 output_excel_file = 'excel path'
 # Save data to Excel
 save_to_excel(data, output_excel_file)
 print(f"Data has been extracted from the PDF and saved to {output_excel_file}")
if _name_ == "_main_":
 main()
