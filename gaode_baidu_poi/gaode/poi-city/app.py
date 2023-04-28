from urllib.parse import quote
from urllib import request
import json
import os
import xlwt
import pandas as pd
from transCoordinateSystem import gcj02_to_wgs84, gcj02_to_bd09
#from shp import trans_point_to_shp

#################################################需要修改###########################################################

# TODO 1.替换为从高德开放平台上申请申请的密钥测试
# 在高德开发者平台申请
amap_web_key = ''

# TODO 2.分类关键字,最好对照<<高德地图POI分类关键字以及编码.xlsx>>来填写对应分类关键字(不是编码)，多个用逗号隔开
keyword = ["加油站", "加气站", "冶金化工", "自然灾害", "综合酒楼", "桥", "政府机关",
           "进站口", "检票口", "飞机场", "港口码头", "地铁站", "普通公交站", "音乐厅",
           "电影院", "电视台", "综合体育馆", "中餐厅", "住宅区", "科研机构", "图书馆",
           "风景名胜", "隧道", "超市", "水库"]

# TODO 3.城市，多个用逗号隔开
city = ['滁州']

# TODO 4.输出数据坐标系,1为高德GCJ20坐标系，2WGS84坐标系，3百度BD09坐标系
coord = 2

# TODO 5. 输出数据文件格式,1为默认xls格式，2为csv格式
data_file_format = 1

############################################以下不需要动#######################################################################


poi_search_url = "http://restapi.amap.com/v3/place/text"
poi_boundary_url = "https://ditu.amap.com/detail/get/detail"


# 根据城市名称和分类关键字获取poi数据
def getpois(cityname, keywords):
    i = 1
    poilist = []
    while True:  # 使用while循环不断分页获取数据
        result = getpoi_page(cityname, keywords, i)
        print(result)
        result = json.loads(result)  # 将字符串转换为json
        if result['count'] == '0':
            break

        hand(poilist, result)
        i = i + 1
    return poilist


# 数据写入excel
def write_to_excel(poilist, cityname, classfield):
    # 一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet(classfield, cell_overwrite_ok=True)

    # 第一行(列标题)
    sheet.write(0, 0, 'lon')
    sheet.write(0, 1, 'lat')
    sheet.write(0, 2, 'name')
    sheet.write(0, 3, 'address')
    sheet.write(0, 4, 'pname')
    sheet.write(0, 5, 'cityname')
    sheet.write(0, 6, 'business_area')
    sheet.write(0, 7, 'type')
    #
    # sheet.write(0, 0, 'cm_kid')
    # sheet.write(0, 1, 'orgid')
    # sheet.write(0, 2, 'org_name')
    # sheet.write(0, 3, 'orgtype_code')
    # sheet.write(0, 4, 'orggrade_code')
    # sheet.write(0, 5, 'address')
    # sheet.write(0, 6, 'longitude')
    # sheet.write(0, 7, 'latitude')
    # sheet.write(0, 8, 'mainfeature')
    # sheet.write(0, 9, 'be_dnum')
    # sheet.write(0, 10, 'doctor_num')
    # sheet.write(0, 11, 'nurse_num')
    # sheet.write(0, 12, 'ambulance_num')
    # sheet.write(0, 13, 'equipdesc')
    # sheet.write(0, 14, 'aseisinten')
    # sheet.write(0, 15, 'duty_tel')
    # sheet.write(0, 16, 'clinicu_num')
    # sheet.write(0, 17, 'department_num')
    # sheet.write(0, 18, 'build_time')
    # sheet.write(0, 19, 'hospitalnature')
    # sheet.write(0, 20, 'inpatien_tnum')
    # sheet.write(0, 21, 'datasource')
    # sheet.write(0, 22, 'charge_man')
    # sheet.write(0, 23, 'contact_phone')
    # sheet.write(0, 24, 'fill_man')
    # sheet.write(0, 25, 'fill_phone')
    # sheet.write(0, 26, 'fill_date')
    # sheet.write(0, 27, 'remake')
    # sheet.write(0, 28, 'cm_addtime')
    # sheet.write(0, 29, 'cm_uptime')
    # sheet.write(0, 30, 'cm_creator')
    # sheet.write(0, 31, 'cm_modifier')
    # sheet.write(0, 32, 'cm_version')
    # sheet.write(0, 33, 'cm_regflag')
    # sheet.write(0, 34, 'cm_orgflag')
    #
    # sheet.write(1, 0, '主键')
    # sheet.write(1, 1, '医院编号')
    # sheet.write(1, 2, '医院名称')
    # sheet.write(1, 3, '医疗卫生机构类型代码')
    # sheet.write(1, 4, '医院机构等级代码')
    # sheet.write(1, 5, '地址')
    # sheet.write(1, 6, '经度')
    # sheet.write(1, 7, '纬度')
    # sheet.write(1, 8, '主要特色')
    # sheet.write(1, 9, '病床数')
    # sheet.write(1, 10, '医生数')
    # sheet.write(1, 11, '护士数')
    # sheet.write(1, 12, '急救车辆数量')
    # sheet.write(1, 13, '主要医疗装备')
    # sheet.write(1, 14, '抗震设防烈度')
    # sheet.write(1, 15, '值班电话')
    # sheet.write(1, 16, '年诊疗人次')
    # sheet.write(1, 17, '科室数量')
    # sheet.write(1, 18, '医院建院年份')
    # sheet.write(1, 19, '经济类型')
    # sheet.write(1, 20, '年入院人次')
    # sheet.write(1, 21, '数据来源')
    # sheet.write(1, 22, '主要负责人')
    # sheet.write(1, 23, '联系电话')
    # sheet.write(1, 24, '填报人')
    # sheet.write(1, 25, '填报人电话')
    # sheet.write(1, 26, '填报时间')
    # sheet.write(1, 27, '备注')
    # sheet.write(1, 28, '创建时间')
    # sheet.write(1, 29, '修改时间')
    # sheet.write(1, 30, '创建人')
    # sheet.write(1, 31, '修改人')
    # sheet.write(1, 32, '版本号')
    # sheet.write(1, 33, '所属区域')
    # sheet.write(1, 34, '所属组织')

    for i in range(len(poilist)):
        # 只采集个别区县
        if ( poilist[i].get('adcode') == "341126" ):
            location = poilist[i].get('location')
            name = poilist[i].get('name')
            address = poilist[i].get('address')
            # pname = poilist[i].get('pname')
            # cityname = poilist[i].get('cityname')
            business_area = poilist[i].get('business_area')
            type = poilist[i].get('type')
            lng = str(location).split(",")[0]
            lat = str(location).split(",")[1]
            reg = poilist[i].get('adcode')

            if (coord == 2):
                result = gcj02_to_wgs84(float(lng), float(lat))
                lng = result[0]
                lat = result[1]
            if (coord == 3):
                result = gcj02_to_bd09(float(lng), float(lat))
                lng = result[0]
                lat = result[1]

            # 每一行写入
            sheet.write(i + 1, 1, lng)
            sheet.write(i + 1, 2, lat)
            sheet.write(i + 1, 3, name)
            sheet.write(i + 1, 4, address)
            # sheet.write(i + 1, 6, pname)
            # sheet.write(i + 1, 5, cityname)
            sheet.write(i + 1, 5, business_area)
            sheet.write(i + 1, 6, type)
            sheet.write(i + 1, 7, reg)

    # 最后，将以上操作保存到指定的Excel文件中
    book.save(r'data' + os.sep + 'poi-' + cityname + "-" + classfield + ".xls")


# 数据写入csv文件中
def write_to_csv(poilist, cityname, classfield):
    data_csv = {}
    lons, lats, names, addresss, pnames, citynames, business_areas, types = [], [], [], [], [], [], [], []

    for i in range(len(poilist)):
        print('===================')
        print(poilist[i])
        location = poilist[i].get('location')
        name = poilist[i].get('name')
        address = poilist[i].get('address')
        pname = poilist[i].get('pname')
        cityname = poilist[i].get('cityname')
        business_area = poilist[i].get('business_area')
        type = poilist[i].get('type')
        lng = str(location).split(",")[0]
        lat = str(location).split(",")[1]

        if (coord == 2):
            result = gcj02_to_wgs84(float(lng), float(lat))
            lng = result[0]
            lat = result[1]
        if (coord == 3):
            result = gcj02_to_bd09(float(lng), float(lat))
            lng = result[0]
            lat = result[1]
        lons.append(lng)
        lats.append(lat)
        names.append(name)
        addresss.append(address)
        pnames.append(pname)
        citynames.append(cityname)
        if business_area == []:
            business_area = ''
        business_areas.append(business_area)
        types.append(type)
    data_csv['lon'], data_csv['lat'], data_csv['name'], data_csv['address'], data_csv['pname'], \
    data_csv['cityname'], data_csv['business_area'], data_csv['type'] = \
        lons, lats, names, addresss, pnames, citynames, business_areas, types

    df = pd.DataFrame(data_csv)

    folder_name = 'poi-' + cityname + "-" + classfield
    folder_name_full = 'test' + os.sep + folder_name + os.sep
    if os.path.exists(folder_name_full) is False:
        os.makedirs(folder_name_full)

    file_name = 'poi-' + cityname + "-" + classfield + ".csv"
    file_path = folder_name_full + file_name

    df.to_csv(file_path, index=False, encoding='utf_8_sig')
    return folder_name_full, file_name


# 将返回的poi数据装入集合返回
def hand(poilist, result):
    # result = json.loads(result)  # 将字符串转换为json
    pois = result['pois']
    for i in range(len(pois)):
        poilist.append(pois[i])


# 单页获取pois
def getpoi_page(cityname, keywords, page):
    req_url = poi_search_url + "?key=" + amap_web_key + '&extensions=all&keywords=' + quote(
        keywords) + '&city=' + quote(cityname) + '&citylimit=true' + '&offset=25' + '&page=' + str(
        page) + '&output=json'
    data = ''
    print('============请求url:' + req_url)
    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    return data


def get_areas(code):
    '''
    获取城市的所有区域
    :param code:
    :return:
    '''

    print('获取城市的所有区域：code: ' + str(code).strip())
    data = get_distrinctNoCache(code)

    print('get_distrinct result:' + data)

    data = json.loads(data)

    districts = data['districts'][0]['districts']
    # 判断是否是直辖市
    # 北京市、上海市、天津市、重庆市。
    if (code.startswith('重庆') or code.startswith('上海') or code.startswith('北京') or code.startswith('天津')):
        districts = data['districts'][0]['districts'][0]['districts']

    i = 0
    area = ""
    for district in districts:
        name = district['name']
        adcode = district['adcode']
        i = i + 1
        area = area + "," + adcode

    print(area)
    print(str(area).strip(','))
    return str(area).strip(',')


def get_data(city, keyword):
    '''
    根据城市名以及POI类型爬取数据
    :param city:
    :param keyword:
    :return:
    '''
    isNeedAreas = True
    if isNeedAreas:
        area = get_areas(city)
    all_pois = []
    if area != None and area != "":
        area_list = str(area).split(",")
        if area_list == 0:
            area_list = str(area).split("，")

        for area in area_list:
            pois_area = getpois(area, keyword)
            print('当前城区：' + str(area) + ', 分类：' + str(keyword) + ", 总的有" + str(len(pois_area)) + "条数据")
            all_pois.extend(pois_area)
        print("所有城区的数据汇总，总数为：" + str(len(all_pois)))
        if data_file_format == 2:
            # 写入CSV
            file_folder, file_name = write_to_csv(all_pois, city, keyword)
            # 写入SHP
            #trans_point_to_shp(file_folder, file_name, 0, 1)
            return
        return write_to_excel(all_pois, city, keyword)
    else:
        pois_area = getpois(city, keyword)
        if data_file_format == 2:
            # 写入CSV
            file_folder, file_name = write_to_csv(all_pois, city, keyword)
            # 写入SHP
            #trans_point_to_shp(file_folder, file_name, 0, 1)
            return
        return write_to_excel(pois_area, city, keyword)

    return None


def get_distrinctNoCache(code):
    '''
    获取中国城市行政区划
    :return:
    '''

    url = "https://restapi.amap.com/v3/config/district?subdistrict=2&extensions=all&key=" + amap_web_key

    req_url = url + "&keywords=" + quote(code)

    print(req_url)

    with request.urlopen(req_url) as f:
        data = f.read()
        data = data.decode('utf-8')
    print(code, data)
    return data


if __name__ == '__main__':

    for ct in city:
        for type in keyword:
            get_data(ct, type)
    print('共', len(city), '个城市, ', len(keyword), '个分类数据全部爬取完成!')


'''
版本更新说明：

2019.10.05：
    1. 数据导出格式支持CSV格式以及XLS两种格式;
    2. 支持同时采集多个城市的POI数据;
    3. 支持同时采集多个POI分类数据

2019.10.10:
    1. 数据导出支持CSV以及XLS两种格式;
    2. CSV格式数据会生成.shp文件，可以直接在ARCGIS中使用

2020.06.19:
    1.清除了poi数据写入shp文件相关操作
    2.修改为根据POI分类关键字来爬取，而不是分类编码
'''
