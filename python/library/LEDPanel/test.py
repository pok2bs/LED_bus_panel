from PIL import Image
from PIL import ImageDraw
import time
print(1)
from LEDPanel import Matrix, MatrixOption
print(2)
# Configuration for the matrix
print(3)
optioner = MatrixOption(debug_mode=False)
optioner.set_panel_size((64, 32))
optioner.set_for_rpi_4()
options = optioner.get_option()
print(4)

matrix = Matrix(options=options, debug_mode=False)
print(5)
# RGB example w/graphics prims.
# Note, only "RGB" mode is supported currently.
image = Image.new("RGB", (32, 32))  # Can be larger than matrix if wanted!!
draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
# Draw some shapes into image (no immediate effect on matrix)...
draw.rectangle((0, 0, 31, 31), fill=(0, 0, 0), outline=(0, 0, 255))
draw.line((0, 0, 31, 31), fill=(255, 0, 0))
draw.line((0, 31, 31, 0), fill=(0, 255, 0))
print(6)
# Then scroll image across matrix...
matrix.draw_image(image, (0, 0))
time.sleep(10)
for n in range(-32, 33):  # Start off top-left, move off bottom-right
    matrix.draw_image(image, (n, n))
    time.sleep(0.05)
print(7)
matrix.clear()