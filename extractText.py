import PIL.Image as Image
import pytesseract
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    """
    Extracts text from an image using OCR.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text.
    """
    try:
        loaded_image = Image.open(image_path)
        decoded_text = pytesseract.image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        return cleaned_text
    except Exception as e:
        print("An error occurred while extracting text from the image:", e)
        return None

def text_to_speech(text, output_path="output.mp3", lang="en"):
    """
    Converts text to speech and saves it as an audio file.

    Args:
        text (str): The text to convert to speech.
        output_path (str): The path to save the audio file (default: "output.mp3").
        lang (str): The language for text-to-speech (default: "en").
    """
    try:
        sound = gTTS(text, lang=lang)
        sound.save(output_path)
        print(f"Text converted to speech and saved as {output_path}")
    except Exception as e:
        print("An error occurred while converting text to speech:", e)

if __name__ == "__main__":
    image_path = "Capture_1.jpg"
    extracted_text = extract_text_from_image(image_path)
    
    if extracted_text:
        text_to_speech(extracted_text)
