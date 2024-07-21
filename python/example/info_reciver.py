import requests,json,os 

class BusOpenApi():
    def __init__(self, key):
        self.key = key
        self.params = {'serviceKey' : self.key, 'pageNo' : '1', 'numOfRows' : '1000', '_type' : 'json'}

    def getApiInformation(self, url):
        try:
            response = requests.get(url, params=self.params)
            result = json.loads(response.content.decode('UTF-8'))['response']['body']['items']['item']

        except:
            print('Api를 호출하지 못함')
            print(response.content.decode('UTF-8'))
            return 'api_error'
        return result

class RouteInfoReceiver(BusOpenApi):
    def __init__(self, key, cityname=str(), citycode=str(), routeid=str(), routeno=str()):
        super().__init__(key)
        self.base_url = "http://apis.data.go.kr/1613000/BusRouteInfoInqireService/"
        self.citycode = citycode
        self.cityname = cityname
        self.routeid = routeid
        self.routeno = routeno
        self.updateParams()

    def updateParams(self):
        self.params.update({'cityCode': self.citycode, 'cityName': self.cityname, 'routeId': self.routeid, 'routeNo': self.routeno})

    def setCityCode(self, citycode):
        self.citycode = citycode
        self.updateParams()

    def setCityName(self, cityname):
        self.cityname = cityname
        self.updateParams()

    def setRouteId(self, routeid):
        self.routeid = routeid
        self.updateParams()

    def setRouteNo(self, routeno):
        self.routeno = routeno
        self.updateParams()

    def getCityCodes(self):
        return self.getApiInformation(self.base_url + "getCtyCodeList")
    
    def getRouteInfomation(self):
        return self.getApiInformation(self.base_url + "getRouteInfoIem")
    
    def getRouteStopList(self):
        return self.getApiInformation(self.base_url + "getRouteAcctoThrghSttnList")
    
    def getRouteNoList(self):
        return self.getApiInformation(self.base_url + "getRouteNoList")
    
class ArriveInfoReceiver(BusOpenApi):
    def __init__(self, key, citycode=str(), nodeid=str(), routeid=str()):
        super().__init__(key)
        self.base_url = "http://apis.data.go.kr/1613000/ArvlInfoInqireService/"
        self.citycode = citycode
        self.nodeid = nodeid
        self.routeid = routeid
        self.updateParams()

    def updateParams(self):
        self.params.update({'cityCode': self.citycode, 'nodeId': self.nodeid, 'routeId': self.routeid})

    def setCityCode(self, citycode):
        self.citycode = citycode
        self.updateParams()

    def setNodeId(self, nodeid):
        self.nodeid = nodeid
        self.updateParams()

    def setRouteId(self, routeid):
        self.routeid = routeid
        self.updateParams()

    def getStopArriveInfo(self):
        return self.getApiInformation(self.base_url + "getSttnAcctoArvlPrearngeInfoList")
    
    def getStopOnRouteArriveTime(self):
        return self.getApiInformation(self.base_url + "getSttnAcctoSpcifyRouteBusArvlPrearngeInfoList")
    
class LocationInfoReceiver(BusOpenApi):
    def __init__(self, key, citycode=str(), nodeid=str(), routeid=str()):
        super().__init__(key)
        self.base_url = "http://apis.data.go.kr/1613000/BusLcInfoInqireService/"
        self.citycode = citycode
        self.nodeid = nodeid
        self.routeid = routeid
        self.updateParams()

    def updateParams(self):
        self.params.update({'cityCode': self.citycode, 'nodeId': self.nodeid, 'routeId': self.routeid})

    def setCityCode(self, citycode):
        self.citycode = citycode
        self.updateParams()

    def setNodeId(self, nodeid):
        self.nodeid = nodeid
        self.updateParams()

    def setRouteId(self, routeid):
        self.routeid = routeid
        self.updateParams()

    def getBuslocationByRoute(self):
        return self.getApiInformation(self.base_url + "getRouteAcctoBusLcList")
    
    def getBusLocationsAccessibleByRoute(self):
        return self.getApiInformation(self.base_url + "getRouteAcctoSpcifySttnAccesBusLcInfo")