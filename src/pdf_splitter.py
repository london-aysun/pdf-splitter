
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the PDF
    reader = PdfReader(input_pdf)

    # Loop through each page and save as a separate PDF
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)

        output_path = os.path.join(output_folder, f"cross_gov_code_retreat_certifiacte{i + 1}.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

    print(f"PDF split into {len(reader.pages)} pages in '{output_folder}'.")

# Example usage:
split_pdf("input.pdf", "output_pages")
