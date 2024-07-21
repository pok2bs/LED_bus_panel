from PIL import Image
from PIL import ImageDraw
import time
from LEDPanel import Matrix, MatrixOptionFile, ImagePanel
# Configuration for the matrix

panel = ImagePanel(resolution=(192, 64))
# RGB example w/graphics prims.
# Note, only "RGB" mode is supported currently.
# image = Image.new("RGB", (32, 32))  # Can be larger than matrix if wanted!!
image = Image.open("test.jpeg", "r")
image = image.resize((64, 64))
# Then scroll image across matrix...
panel.draw_image(image, offset=(0, 0))
time.sleep(100)