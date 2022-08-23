from PIL import Image

image = Image.open(r"F:\Hackathon\hackathon\test\dyslexia\hij.png")
rgb = image.convert("RGB")
rgb.save(r"F:\Hackathon\hackathon\test\dyslexia\sam.jpg")
