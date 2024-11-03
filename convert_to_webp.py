from PIL import Image
import os

def convert_to_webp(filepath: str) -> None:
    dirname = os.path.dirname(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]

    img = Image.open(filepath)
    img.save(os.path.join(dirname, filename + ".webp"), "webp")

if __name__ == "__main__": 
    filepath = input("Enter the file path: ").replace("'", "")
    convert_to_webp(filepath)

    
