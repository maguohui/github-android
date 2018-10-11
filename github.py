# encoding: utf-8
from urllib.request import urlopen
from urllib.request import Request
import datetime
import json
import sys

def get_stared(token,page,per_page):
    url = 'https://api.github.com/users/maguohui/starred?page={page}&per_page={per_page}&access_token={token}'.format(token=token,page=page,per_page=per_page)
    print('__get_stared__  ++++++++++++++++++>get_stared  begin<++++++++++++++++++   page=',page,' per_page=',per_page)
    print('__get_stared__  url=',url)
    req = Request(url,headers=headers)
    response = urlopen(req).read()
    if len(response)==0:
        print('__get_stared__  response=0')
        return response
    else:
        result = json.loads(response.decode('utf-8'))
        #result = json.loads(response.decode())
        return result

#https://raw.githubusercontent.com/maguohui/ArmsComponent/master/README.md
def get_ReadMe(full_name):
    url = 'https://raw.githubusercontent.com/{full_name}/master/README.md'.format(full_name=full_name)
    print('__get_ReadMe__  url=',url)
    req = Request(url,headers=headers)
    response = urlopen(req).read()
    response = response.decode('utf-8')
    #print('__get_ReadMe__  response=',response)
    if len(response)==0:
        print('__get_ReadMe__  response=0')
        return response
    else:
        #result = json.loads(response.decode())
        #return result
        return response
def writeFile(name,full_name,html_url,description,owner,login):
    #__main__   get_stared  results item name = CalendarView  full_name= huanghaibin-dev/CalendarView
    #html_url= https://github.com/huanghaibin-dev/CalendarView  login= huanghaibin-dev
    
    path = '%s_%s.md'%(login,name)
    print('__writeFile__   path =',path)
    f = open(path, 'w',encoding='utf8')

    f.write('---\n')
    content = 'title: %s\nauthor:\n  nick:  %s\n  link: %s\neditor:\n  name:  %s\n  link:  %s\nsubtitle: %s\n'%(full_name,login,html_url,'magh','https://www.github.com/maguohui',description)
    #print('__writeFile__   content =',content)
    f.write(content)
    f.write('---\n\n')

    readmeCotent = get_ReadMe(full_name)
    f.write(readmeCotent)
    f.close()

def startProcess():
    results = get_stared(access_token,page,per_page)
    print('__startProcess__   get_stared  results=',results)
    for item in results:
        print('__startProcess__    ---------------->start<----------------')
        name = item['name']
        full_name = item['full_name']
        html_url = item['html_url']
        description = item['description']
        owner = item['owner']
        login = owner['login']
        #print('__startProcess__   get_stared  results item name =',name,' full_name=',full_name,' html_url=',html_url,' login=',login)
        print('__startProcess__   get_stared  results item login=%s name = %s full_name= %s html_url= %s description=%s' %(login,name,full_name,html_url,description))

        writeFile(name,full_name,html_url,description,owner,login)
        print('__startProcess__   get_stared  ---------------->end<----------------\n\n\n\n')
    return results

''' 
this is zhushi
'''
if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0',
               'Authorization': 'token 39ae45d3b545dce1d3e57d33e3dcc5abe242....',
               'Content-Type':'application/json',
               'Accept':'application/json'
               }
    access_token = '39ae45d3b545dce1d3e57d33e3dcc5abe242....'
    
    page=135
    per_page=10
    print('__main__    =====================>begin<=====================')
    results = startProcess()
    length = len(results)
    print('__main__   get_stared  results length=',length)
    if length==0:
        print('__main__    =====================>over<=====================')
        sys.exit()
    else:
        page = page+1
        startProcess()


