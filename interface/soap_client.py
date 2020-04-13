from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import


# 电话号码归属地
# url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
# client = Client(url)
# result = client.service.getMobileCodeInfo(15910945157)
# print(client)


# 天气查询
url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?WSDL'
imp = Import('http://www.w3.org/2001/XMLSchema',
             location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')

client = Client(url, plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCtiyNmae("上海")
print(result)


