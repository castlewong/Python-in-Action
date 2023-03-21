from urllib.parse import quote
from urllib import request
import json
import xlwt
import xlrd
import re
import requests
import time
#http://api.tianditu.gov.cn/geocoder?ds={"keyWord":"延庆区北京市延庆区延庆镇莲花池村前街50夕阳红养老院"}&tk=您的密钥
web_key = '0aa532540042980837ac82fc7df2294c' #自己天地图的地图的key密钥
url = "http://api.tianditu.gov.cn/v2/search?postStr={\"keyWord\":"
keyWord = "湖泊" #搜索关键字
keyWord =keyWord.encode('unicode_escape').decode('ascii')
start = 0 #分页数量
specify = '156500000' #行政区划代码
#dataTypes = "230213" #类型

Mess_Num_list_name = []
Mess_Num_list_poiType = []
Mess_Num_list_address = []
Mess_Num_list_lonlat = []
Mess_Num_list_phone = []
Mess_Num_list_county = []
Mess_Num_list_countyCode = []
Mess_Num_list_typeName = []
while start < 10:
    # http: // api.tianditu.gov.cn / v2 / search?postStr = {"keyWord": "商厦", "queryType": 12, "start": 0, "count": 10,
    #                                                   "specify": "156110108"} & type = query & tk = 您的密钥
    req_url = url  + "\"" +  keyWord  + "\"" + ",\"queryType\":12,\"start\":" + str(start) \
              + ',\"count\":300,\"specify\":\"' +specify + '\"'+'}&type=query&tk=' + web_key
    print(req_url)

    Headers = {'cookie': 'TDTSESID=rBACA2OJvkcjV0Yc+++dAg==; HWWAFSESID=97e50a6f5c9fa67',
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    #request_site = request.Request(url, headers= Headers)
    Mess = requests.get(req_url, headers=Headers).content.decode()
    time.sleep(1)
    #print(Mess)
    data = ''
    #f = request.urlopen(request_site)
    #data = f.read()
    #data = Mess.decode('utf-8')
    result=json.loads(Mess)
    print(result['count'])
    if result['count'] == '0':
        break
    for i in range(len(result['pois'])):
            Mess_Num_name = result['pois'][i]['name']
            Mess_Num_poiType = result['pois'][i]['poiType']
            Mess_Num_address = result['pois'][i]['address']
            Mess_Num_lonlat = result['pois'][i]['lonlat']
            #Mess_Num_phone = result['pois'][i]['phone']
            # Mess_Num_county = result['pois'][i]['county']
            #Mess_Num_countyCode = result['pois'][i]['countyCode']
            #Mess_Num_typeName = result['pois'][i]['typeName']
            Mess_Num_list_name.append(Mess_Num_name)
            Mess_Num_list_poiType.append(Mess_Num_poiType)
            Mess_Num_list_address.append(Mess_Num_address)
            Mess_Num_list_lonlat.append(Mess_Num_lonlat)
           # Mess_Num_list_phone.append(Mess_Num_phone)
            #Mess_Num_list_county.append(Mess_Num_county)
            #Mess_Num_list_countyCode.append(Mess_Num_countyCode)
            #Mess_Num_list_typeName.append(Mess_Num_typeName)
            print('名称:',result['pois'][i]['name']
            ,'，类型:',result['pois'][i]['poiType']
            ,'，详细地址:',result['pois'][i]['address']
            ,'，经纬度:',result['pois'][i]['lonlat']
           # , '，电话号码:', result['pois'][i]['phone']
            #, '，所属区县名称:', result['pois'][i]['county']
            #, '，区县行政区编码:', result['pois'][i]['countyCode']
            #, '，分类名称:', result['pois'][i]['typeName']
            )
    start = start + 1

# 输出企业联系方式到新Excel文件
book = xlwt.Workbook()
sheet1 = book.add_sheet(r'poi')
sheet1.write(0, 0, r'名称')
sheet1.write(0, 1, r'类型')
sheet1.write(0, 2, r'详细地址')
sheet1.write(0, 3, r'经纬度')
#sheet1.write(0, 4, r'电话号码')
#sheet1.write(0, 5, r'所属区县名称')
#sheet1.write(0, 6, r'区县行政区编码')
#sheet1.write(0, 7, r'分类名称')

for j in range(len(Mess_Num_list_name)):
        sheet1.write(j + 1, 0, Mess_Num_list_name[j])
        sheet1.write(j + 1, 1, Mess_Num_list_poiType[j])
        sheet1.write(j + 1, 2, Mess_Num_list_address[j])
        sheet1.write(j + 1, 3, Mess_Num_list_lonlat[j])
        #sheet1.write(j + 1, 4, Mess_Num_list_phone[j])
        #sheet1.write(j + 1, 5, Mess_Num_list_county[j])
        #sheet1.write(j + 1, 6, Mess_Num_list_countyCode[j])
        #sheet1.write(j + 1, 7, Mess_Num_list_typeName[j])
book.save(r'keyword.xls' + keyWord)



