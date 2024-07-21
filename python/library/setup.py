from setuptools import setup

setup(
	name='seoul-bus-panel',
	version='1.0',
	author='Jiyong Youn',
	author_email='01@0101010101.com',
	description='Seoul bus LED panel library',
	url='https://github.com/hletrd/LED_bus_panel',
	packages=['LEDPanel', 'bus'],
    package_data={'bus': ['font.png', 'font.txt']},
	install_requires=['Pillow', 'numpy'],
)
