# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:42:30 2020

@author: chiakai
"""

#分析姓名得分
def goodName(surname, name, sex, year, month, day, hour, minute):
    import requests,re
    from bs4 import BeautifulSoup
    
    s = requests.session()
    
    url = 'https://www.lnka.tw/app/analyzename.aspx'
    
    r = s.get('https://www.lnka.tw/app/analyzename.aspx', verify=False)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #print(r.text)
    
    VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
    
    VIEWSTATEGENERATOR = soup.find(id="__VIEWSTATEGENERATOR")['value']
    
    data = {
            '__VIEWSTATE': VIEWSTATE,
            '__VIEWSTATEGENERATOR': VIEWSTATEGENERATOR,
            'txtXing': str(surname),
            'txtName': str(name),
            'sex': str(sex),
            'ddlYear': str(year),
            'ddlMonth': str(month),
            'ddlDay': str(day),
            'ddlHour': str(hour),
            'ddlMinute': '0',
            'firsthour': 'n',
            'btnStart': '免費分析',          
            }
    
    r1 = s.post(url, data=data)
    
    #print(r1.text)
    
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    
    content = soup1.find_all(class_="half_div")
    
    #print(content)

    wuxing = re.findall(r'名字的五行是：“(\S+)”',str(content[0]))[0]
    wuxing_score = re.findall(r'最終得分是：(\S+)分',str(content[0]))[0]
    temp = soup1.find_all("td")
    score = re.findall('(\S+)分',temp[22].string)[0]
    
    msg = f'\n>>姓名：{surname}{name}({wuxing},{score}分,五行:{wuxing_score}分)\n\n參考來源網址(詳情請到網址內查詢)：\nhttps://www.lnka.tw/app/analyzename.aspx'
    
    return msg, wuxing, score, wuxing_score


if __name__ == '__main__':
    surname = '張'
    name = '英英'
    sex = '0'
    year = '2014'
    month = '9'
    day = '13'
    hour = '9'
    minute = '0'
    msg, wuxing, score, wuxing_score = goodName(surname, name, sex, year, month, day, hour, minute)
    print(msg)