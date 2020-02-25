from aip import AipOcr

import os

accept=[] #正确
unaccept=[]#错误

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
    wrong='返程健康登记'
    extra=''
    isextra=0

    

    for result in results:
        text = result["words"]
        if (wrong in text):
            extra='非安康码'
            isextra=1
        elif(rule in text):
            newName=text
            break

    print(newName)
    if(isextra):
        unaccept.append(text.replace('姓名:','')) 
    else:
        accept.append(text.replace('姓名:','')) 
    
    os.rename('801/801/'+item,'801/801/'+ extra+newName.replace(':','--').replace('*','')+'.jpg')#非法字符处理
if __name__ == '__main__':
    filePath = '801/801'
    names = os.listdir(filePath)
    #print(name)
    for item in names:
        try:
            work(item)
        except:
            print('姓名包含非法字符或者有重复图片：',item)
            continue
    
    print('正确')
    print(accept)
    print('错误')
    print(unaccept)


