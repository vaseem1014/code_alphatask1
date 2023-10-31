# code_alphatask1
# Image Text-to-Speech (OCR to Speech) Utility

This Python script is designed to extract text from an image using Optical Character Recognition (OCR) and convert the extracted text into speech. It utilizes the following Python libraries:

- `PIL` (Python Imaging Library): For opening and manipulating image files.
- `pytesseract`: For OCR functionality.
- `gTTS` (Google Text-to-Speech): For converting text to speech.

## Prerequisites

Before using this script, make sure you have the following components installed:

- Python 3.x
- Tesseract OCR installed and set up properly. You need to set the path to the Tesseract executable using the `pytesseract.pytesseract.tesseract_cmd` line in the script.
- Python packages installed:
  - `PIL` (Python Imaging Library)
  - `pytesseract`
  - `gTTS`

## Usage

1. Make sure you have Python and the required libraries installed.
2. Install Tesseract OCR and set the path to the Tesseract executable as mentioned in the script.
3. Save the image you want to process in the same directory as this script or provide the full path to the image.

Run the script, and it will perform the following actions:

1. Open the specified image.
2. Extract text from the image using OCR.
3. Clean up the extracted text (removing newline characters).
4. Convert the cleaned text to speech and save it as an audio file (default: "output.mp3").

