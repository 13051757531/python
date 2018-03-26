#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @分享者  : 小强测试品牌 (xqtesting@qq.com)
# @官网    : http://www.xqtesting.com
# @博客	: http://www.xqtesting.com/blog.html
# @微信公众号  : 测试帮日记



import hashlib
import base64
#把pydes压缩包中的pyDes.py拷贝到python安装目录下的Lib中
from pyDes import * 


def md5_encode(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()#经过特殊处理之后以字符串形式返回



def sha1_encode(data):
    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    return sha1.hexdigest()


result1=md5_encode('小强测试')
print("md5加密：", result1)
result2=sha1_encode('testingbang')
print("sha1加密：", result2)




# DES加密
'''
语法格式：
pyDes.des(key, [mode], [IV], [pad], [padmode])

参数的意思分别如下：
key:加密密钥，长度只能为8位。必选

mode:加密方式。ECB（默认）、CBC（安全性好于前者）
IV：初始字节数（长度只能为8位），如果你选择的加密方式为CBC就必须有这个参数，否则可以没有

pad：加密时，将该字符添加到数据的结尾；解密时，将删除从最后一个往前的8位
     如果被加密的数据不是8 bytes的倍数，则pad的数量只能为单数
     如果被加密的数据是8 bytes的倍数，则无所谓
padmode：PAD_NORMAL（可有pad参数）
         PAD_PKCS5（不能有pad参数）
'''
#data为加密数据，key为密钥
def des_encode(data,key):
    k = des(key,mode=ECB,IV=None,pad=None,padmode=PAD_PKCS5)
    #k = des(key,mode=CBC,IV="goodluck",pad="q",padmode=PAD_NORMAL)
    
    #encrypt来加密我的数据，然后进行base64编码
    encodeStr = base64.b64encode(k.encrypt(data))
    return encodeStr


result3 = des_encode('wow', 'xqtest66')
print("des加密：", result3)
print(str(result3,'utf-8'))