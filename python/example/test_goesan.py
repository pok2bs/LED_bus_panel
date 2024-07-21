import bus, time
from LEDPanel import ImagePanel
from info_reciver import ArriveInfoReceiver

buspanel = bus.BusPanel()
panel = ImagePanel(resolution=(192, 64))
key = 'eJO+CaSYpebfSPJI3R0BKMU9Ua2/LAVpnlqCZxlKH6XzKHL+eKC9CY6xrBJQA4croYCZ/6OFZEU2d3elBLsIbg=='
cityCode = 33360
nodeid = "TSB280000104"
while True:
    bus_data = ArriveInfoReceiver(key=key, citycode=cityCode, nodeid=nodeid)

    datas = bus_data.getStopArriveInfo()
    if datas == 'api_error':
        time.sleep(30)
        continue
    buspanel.clear()
    panel.clear()
    count = 0
    for data in datas:
        arrive_time = int(int(data['arrtime'])/60)
        
        if arrive_time > 3 and count <= 5:
            buspanel.add_bus(str(data['routeno']), time=arrive_time) #저상버스
            count += 1
        else:
            buspanel.add_arrive(str(data['routeno']))

    img = buspanel.get_image() #Pillow 이미지를 만들어서 가져옴
    panel.draw_image(img, (0,0))
    time.sleep(60)

    

