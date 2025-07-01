from PyPDF2 import PdfReader, PdfWriter

input_path = "LECTII LICENTA.pdf"  # Replace with your PDF filename
reader = PdfReader(input_path)
total_pages = 75
counter = 2

for i in range(63, total_pages, 3):
    writer = PdfWriter()
    for j in range(i, min(i + 3, total_pages)):
        writer.add_page(reader.pages[j])
    
    output_filename = f"BGK/{counter}.pdf"
    with open(output_filename, "wb") as output_pdf:
        writer.write(output_pdf)
    counter += 1

print("Splitting complete.")
