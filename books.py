import logging
import json
f =open('opac.lib.lut.cn.har',encoding='utf-8')
s = set()
j =json.load(f)
for target in j['log']['entries']:
    if target['request']['queryString']:
        for item in eval(target['response']['content']['text']):
            if 'bookTitle' in item:
                s.add(item['操作类型'])
                if item['操作类型']=='X':
                    # print(item)
                    print(item['bookTitle'],item['处理时间'])
                # s.add(item['bookTitle'])
# for i in s:
#     print(i)
    # :
        # print(item)
        # if 'bookTitle' in item:
            # print(item['bookTitle'])