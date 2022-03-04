"""Created by Jhesed Tacadena on March 2, 2022."""
import os

from docx import Document
from PIL import Image
from pytesseract import pytesseract

from config import PATH_INPUT_IMAGES, PATH_OUTPUT_DOCS, TESSERACT_PATH

# Setup pytesseract library
pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_from_image(file_name: str) -> str:
    """Extracts text from image."""

    # Locate the physical file
    input_file = f"{PATH_INPUT_IMAGES}\\{file_name}"

    # Opening file as image
    image = Image.open(input_file)

    # Using tes``seract library to extract text from image
    return pytesseract.image_to_string(image)


def save_text_to_doc(file_name: str, text: str) -> None:
    """Writes string to docx document."""

    # Example: input file named screenshot.PNG will be named as sample.docx
    output_file = f"{PATH_OUTPUT_DOCS}\\{file_name.split('.')[0]}.docx"

    document = Document()
    document.add_paragraph(text)
    document.save(output_file)


if __name__ == "__main__":

    file_names = os.listdir(PATH_INPUT_IMAGES)
    for name in file_names:

        print(f"Extracting text from {name}")
        extracted_text = extract_text_from_image(file_name=name)

        print(f"Saving docx counterpart of {name}")
        save_text_to_doc(file_name=name, text=extracted_text)

    print("Done processing input images.")
