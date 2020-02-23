from aip import AipOcr

import os


def work(item):
    """ 你的 APPID AK SK  图2的内容"""
    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    fname = '801/801/'+item#图片路径

    """ 读取图片 """

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(fname)

    """ 调用通用文字识别, 图片参数为本地图片 """
    results = client.general(image)["words_result"]  # 还可以使用身份证驾驶证模板，直接得到字典对应所需字段
    newName=''
    rule='姓名'
    for result in results:
        text = result["words"]
        if(rule in text):
            newName=text
            break

    print(newName)
    os.rename('801/801/'+item,'801/801/'+ newName.replace(':','--')+'.jpg')
if __name__ == '__main__':
    filePath = '801/801'
    names = os.listdir(filePath)
    #print(name)
    for item in names:
        work(item)




