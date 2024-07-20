import sys, json, random, colorsys

try:
	from PIL import Image, ImageFont, ImageDraw
except:
	sys.stderr.write('Pillow is not installed.\n')

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
	EMULATE_ABLE = True
except:
	EMULATE_ABLE = False	

class Matrix():
	def __init__(self, options, emul_use=EMULATE_ABLE):
		self.options = options
		self.matrix = self.select_matrix_module(emul_use)

	def select_matrix_module(self, emul_use):
		if emul_use:
			matrix =  RGBMatrixEmulator.RGBMatrix(self.options)
		else:
			print(1)
			matrix =  rgbmatrix.RGBMatrix(self.options)
			print(2)
		return matrix

	def set_image(self, image, offset = tuple):
		self.matrix.SetImage(image, offset_x=offset[0], offset_y=offset[1])

	def draw_image(self, image, offset = tuple):
		self.clear()
		self.set_image(image, offset)

	def clear(self):
		self.matrix.Clear()

class MatrixOptionFile():
	def __init__(self, path=r"matrix_config.json", emul_use=EMULATE_ABLE):
		self.path = path
		self.options = self.select_option_module(emul_use)
		self.data = dict()
		self.try_load()

	def try_load(self):
		try:
			self.load_options()
		except:
			self.set_default_options()
			self.save_options()


	def select_option_module(self, emul_use):
		if emul_use:
			return RGBMatrixEmulator.RGBMatrixOptions()
		else:
			return rgbmatrix.RGBMatrixOptions()

	def load_options(self):
		with open(self.path, 'r', encoding='utf-8') as file:
			self.data = json.load(file)
		self.convert_dict_to_option()

	def save_options(self):
		self.convert_option_to_dict()
		with open(self.path, 'w') as file:
			json.dump(self.data, file, indent='\t')

	def set_path(self, path):
		self.path = path
	
	def get_options(self):
		return self.options

	def convert_dict_to_option(self):
		self.options.brightness = self.data['brightness']
		self.options.chain_length = self.data['chain_length']
		self.options.cols = self.data['cols']
		self.options.disable_hardware_pulsing = self.data['disable_hardware_pulsing']
		self.options.gpio_slowdown = self.data['gpio_slowdown']
		self.options.hardware_mapping = self.data['hardware_mapping']
		self.options.led_rgb_sequence = self.data['led_rgb_sequence']
		self.options.multiplexing = self.data['multiplexing']
		self.options.parallel = self.data['parallel']
		self.options.pwm_bits = self.data['pwm_bits']
		self.options.row_address_type = self.data['row_address_type']
		self.options.rows = self.data['rows']

	def convert_option_to_dict(self):
		self.data['brightness'] = self.options.brightness
		self.data['chain_length'] = self.options.chain_length
		self.data['cols'] = self.options.cols
		self.data['disable_hardware_pulsing'] = self.options.disable_hardware_pulsing
		self.data['gpio_slowdown'] = self.options.gpio_slowdown
		self.data['hardware_mapping'] = self.options.hardware_mapping
		self.data['led_rgb_sequence'] = self.options.led_rgb_sequence
		self.data['multiplexing'] = self.options.multiplexing
		self.data['parallel'] = self.options.parallel
		self.data['pwm_bits'] = self.options.pwm_bits
		self.data['row_address_type'] = self.options.row_address_type
		self.data['rows'] = self.options.rows

	def set_default_options(self):
		self.options.brightness = 100
		self.options.chain_length = 1
		self.options.cols = 32
		self.options.disable_hardware_pulsing = False
		self.options.gpio_slowdown = 0
		self.options.hardware_mapping = 'regular'
		self.options.led_rgb_sequence = 'RGB'
		self.options.multiplexing = 0
		self.options.parallel = 1
		self.options.pwm_bits = 11
		self.options.row_address_type = 1
		self.options.rows = 32

class Colors:
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
		rand_color = colorsys.hsv_to_rgb(random.random(), 0.6, 1)
		rand_color = tuple(map(lambda x: int(x*256), rand_color))
		return rand_color

class ImagePanel:
	def __init__(self, options_file_path = r"matrix_config.json", resolution = (32, 32), emul_use = EMULATE_ABLE):
		self.options_file = MatrixOptionFile(options_file_path)
		self.options = self.options_file.get_options()
		self.matrix = Matrix(self.options)
		self.gen_new_image(resolution)
	

	def gen_new_image(self, resolution: tuple):
		self.set_panel_resolution(self, resolution)
		self.image = Image.new("RGB", resolution)
		self.draw = ImageDraw(self.image)

	def set_panel_resolution(self, resolution: tuple):
		self.resolution = resolution

    
		
