from PIL import Image
import moderngl as mgl


def LoadBackground(filename, context):
    img = (Image.open(f"textures/{filename}").transpose(Image.FLIP_TOP_BOTTOM)).convert("RGB")
    Background = context.texture(img.size, 3, img.tobytes())
    Background.use()
    return Background, 0 #zero is the priortity value, it ranges from 0 to 255, the higher, the more important.