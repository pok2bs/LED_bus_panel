import bus
from LEDPanel.LEDPanel import ImagePanel

buspanel = bus.BusPanel()
panel = ImagePanel(resolution=(192, 64))

buspanel.clear()
panel.clear()

buspanel.add_bus('5511', time=10, lowdeck=True) #저상버스
buspanel.add_bus('5513', time=15)
buspanel.add_bus('5511', time=bus.BusPanel.end) #종료
buspanel.add_bus('5516', time=bus.BusPanel.depot) #차고지

buspanel.add_arrive('750A', density=2) #곧도착, 혼잡
buspanel.add_arrive('750B', density=1) #곧도착, 보통
buspanel.add_arrive('506', density=0) #곧도착, 여유

img = buspanel.get_image() #Pillow 이미지를 만들어서 가져옴
panel.draw_image(img, (0,0))

import time
time.sleep(100)
