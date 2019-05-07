#urllib模块提供了读取Web页面数据的接口
import urllib
import requests

# 获取英雄列表数据
def getListData(url,page):
    allData = []
    r = requests.get(url+'&page='+page)
    # print(r.json())
    pageData = r.json()
    dicData = pageData['data']
    for dic in dicData['goods']:
        allData.append(dic)
    return allData

# 获取英雄图片所需的相关信息
def getDetailImg(id):
    url = 'http://apps.game.qq.com/daoju/go/zmgoods/detail?goodsid='+str(id)
    r = requests.get(url)
    goodsData = r.json()
    imgUrl = goodsData['goods']['sExtShowInfo']['picInfo']['sGoodsPic2']
    imgName = goodsData['goods']['sGoodsName']
    msg = {'imgUrl':imgUrl,'imgName':imgName}
    return msg

dataUrl = "http://apps.game.qq.com/daoju/go/zmgoods/list?cat=16&plat=android&version=9841"
allData = []
idData = []
for i in range(1,8):
    data = getListData(dataUrl,str(i))
    for dic in data:
        allData.append(dic)
        idData.append(dic['iGoodsId'])

imgs = []
for idStr in idData:
    imgDic = getDetailImg(idStr)
    imgs.append(imgDic)
print(imgs)
for img in imgs:
    filePath = 'D:\\英雄图片\\'+img['imgName']+'.jpg'
    print('-------------------'+filePath+'    '+img['imgUrl'] )
    urllib.request.urlretrieve(img['imgUrl'],filePath)

