from PIL import Image
import os

def convert_to_webp(filepath: str) -> str:
    dirname = os.path.dirname(filepath)
    filename = os.path.splitext(os.path.basename(filepath))[0]
    out_dir = os.path.join(dirname, "webp")
    output = os.path.join(out_dir, filename + ".webp")
    os.makedirs(out_dir, exist_ok=True)

    img = Image.open(filepath)
    img.save(output, "webp")

    return output

if __name__ == "__main__": 
    filepath = input("Enter the file path: ").replace("'", "")
    convert_to_webp(filepath)

    
