import sys

debug_able = False

try:
	from PIL import Image, ImageFont, ImageDraw
except:
	sys.stderr.write('Pillow is not installed.\n')

import colorsys
import random
try:
	import numpy as np
except:
	sys.stderr.write('NumPy is not installed.\n')

try:
	import rgbmatrix
except:
	sys.stderr.write('RGBMatrix library is not installed.\n')

try:
	import RGBMatrixEmulator 
	debug_able = True
except:
	debug_able = False	

class Matrix():
	def __init__(self, options, debug_mode=False):
		self.options = options
		self.set_debug(debug_mode)

	def set_debug(self, debug_mode):
		if debug_mode:
			self.matrix = RGBMatrixEmulator.RGBMatrix(self.options)
		else:
			self.matrix = rgbmatrix.RGBMatrix(options=self.options)

	def set_image(self, image, offset = tuple):
		self.matrix.SetImage(image, offset_x=offset[0], offset_y=offset[1])

	def draw_image(self, image, offset = tuple):
		self.clear()
		self.set_image(image, offset)

	def clear(self):
		self.matrix.Clear()

class MatrixOption():
	def __init__(self, debug_mode=False):
		self.set_debug(debug_mode)
		self.brightness = 100
		self.cols = 32
		self.rows = 32
		self.chain_length = 1
		self.hardware_mapping = 'regular'
		self.gpio_slowdown = 2
		self.disable_hardware_pulsing = False

	def set_debug(self, debug_mode=False):
		if debug_mode:
			self.option = RGBMatrixEmulator.RGBMatrixOptions()
		else:
			self.option = rgbmatrix.RGBMatrixOptions()
	
	def set_britness(self, britness: int):
		self.brightness = britness

	def set_panel_size(self, matrix_size: tuple, chain = 1):
		self.cols = matrix_size[0]
		self.rows = matrix_size[1]
		self.chain_length = chain
	
	def set_panel_chain_length(self, chain_length: int):
		self.chain_length = chain_length

	def set_adafruit_mapping(self):
		self.hardware_mapping = "adafruit-hat"
	
	def set_for_rpi_4(self):
		self.gpio_slowdown = 4
		self.disable_hardware_pulsing = True

	def get_option(self):
		self.apply_option()
		return self.option
	
	def apply_option(self):
		self.option.brightness = self.brightness
		self.option.cols = self.cols
		self.option.rows = self.rows
		self.option.chain_length = self.chain_length
		self.option.hardware_mapping = self.hardware_mapping
		self.option.gpio_slowdown = self.gpio_slowdown
		self.option.disable_hardware_pulsing = self.disable_hardware_pulsing

class colors:
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	green = (0, 255, 0)
	blue = (0, 0, 255)
	orange = (255, 128, 0)
	yellow = (255, 255, 0)
	magenta = (255, 0, 255)
	cyan = (0, 255, 255)

	@staticmethod
	def random_color():
		rndcolor = colorsys.hsv_to_rgb(random.random(), 0.6, 1)
		rndcolor = tuple(map(lambda x: int(x*256), rndcolor))
		return rndcolor

class ImagePanel:
	def __init__(self, debug):
		pass
		
