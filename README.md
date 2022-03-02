# Image-to-Doc-Converter
* Extracts text from images and convert it to _Document format_
* It can be used for automating re-typing jobs.
* This _README_ is intended for _WIndows 10 users_

# Installation
1. Create [_virtual environment_](https://medium.com/@dev.jhesed/how-to-install-and-setup-pycharm-and-venv-in-windows-10-d4af56399b00)
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Install `tesseract`  [executable for windows](https://github.com/UB-Mannheim/tesseract/wiki)
4. Locate the file path of the executable file. It is usually located in
```
C:\Program Files\Tesseract-OCR\tesseract.exe
```
5. Set _environment variables_ listed down in `config.py`

# Usage
1. Place the images that you need to convert in `input/`
2. Run `main.py`
3. Check the results under `output/`. The file name except the file extension will be retained.

# Acknowledgement
* To God
* To my beautiful wife Hannah
* To morning coffee


_____
_Jhesed D. Tacadena_
