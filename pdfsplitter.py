from PyPDF2 import PdfReader, PdfWriter

input_path = "LECTII LICENTA.pdf"  # Replace with your PDF filename
reader = PdfReader(input_path)
total_pages = 29
counter = 2

for i in range(4, total_pages, 29):
    writer = PdfWriter()
    for j in range(i, min(i + 29, total_pages)):
        writer.add_page(reader.pages[j])
    
    output_filename = f"Kinesiologie improved/{counter}.pdf"
    with open(output_filename, "wb") as output_pdf:
        writer.write(output_pdf)
    counter += 1

print("Splitting complete.")
