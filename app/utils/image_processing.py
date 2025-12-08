from PIL import Image
from io import BytesIO
import hashlib

def load_image_bytes(file_bytes: bytes) -> Image.Image:
    return Image.open(BytesIO(file_bytes))

def sha256_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def generate_variant(img: Image.Image, size: int, fmt: str):
    img_copy = img.copy()
    img_copy.thumbnail((size, size), Image.LANCZOS)

    buffer = BytesIO()
    img_copy.save(buffer, format=fmt.upper(), optimize=True)
    data = buffer.getvalue()

    return {
        "width": size,
        "height": img_copy.height,
        "bytes": data,
        "size_bytes": len(data),
        "content_type": f"image/{fmt.lower()}"
    }
