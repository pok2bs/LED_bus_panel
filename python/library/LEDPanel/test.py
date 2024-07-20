from PIL import Image
from PIL import ImageDraw
import time
from LEDPanel import Matrix, MatrixOptionFile
# Configuration for the matrix

matrix = Matrix()
# RGB example w/graphics prims.
# Note, only "RGB" mode is supported currently.
image = Image.new("RGB", (32, 32))  # Can be larger than matrix if wanted!!
draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
# Draw some shapes into image (no immediate effect on matrix)...
draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 255))
draw.line((0, 0, 31, 31), fill=(255, 0, 0))
draw.line((0, 31, 31, 0), fill=(0, 255, 0))
# Then scroll image across matrix...
matrix.draw_image(image, offset=(0, 0))
time.sleep(10)

for n in range(-32, 33):  # Start off top-left, move off bottom-right
    matrix.draw_image(image, offset=(n, n))
    time.sleep(0.05)
matrix.clear()