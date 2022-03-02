"""Created by Jhesed Tacadena on March 2, 2022."""

import os

# Path to windows executable file for tessearct
# Default: program files
TESSERACT_PATH = os.getenv(
    "TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

CURRENT_DIR = os.getcwd()

# Input directory path containing image files
# Default: input directory in current path
PATH_INPUT_IMAGES = os.getenv("PATH_INPUT_IMAGE", f"{CURRENT_DIR}\\input")

# Output directory path
# Default: output directory in current path
PATH_OUTPUT_DOCS = os.getenv("PATH_OUTPUT_DOC", f"{CURRENT_DIR}\\output")
