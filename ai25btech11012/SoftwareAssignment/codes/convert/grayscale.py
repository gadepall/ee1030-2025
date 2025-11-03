from PIL import Image

img = Image.open("/Users/unnathi/Documents/ee1030-2025/ai25btech11012/SoftwareAssignment/figs/greyscale.png").convert("L")
img = img.resize((256,256))
img.save("/Users/unnathi/Documents/ee1030-2025/ai25btech11012/SoftwareAssignment/figs/greyscale.pgm")
