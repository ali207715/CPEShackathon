import pytesseract
from PIL import Image
import pypdfium2 as pdfium


def load_file(file):
    data = None

    if file.type == "application/pdf":
        data = []

        pdf = pdfium.PdfDocument(file)
        n_pages = len(pdf)
        for page_number in range(n_pages):
            page = pdf.get_page(page_number)
            bit_image = page.render()
            data.append(bit_image.to_pil())

    else:
        data = [Image.open(file)]

    return data


def extract_text(files):
    output = []
    for file in files:
        # Adding custom options
        custom_config = r'--oem 3 --psm 6'
        res = pytesseract.image_to_string(file, config=custom_config)
        output.append(res)
    return ['' + x for x in output]

