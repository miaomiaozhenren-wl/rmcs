import tkinter as tk

from pysnmp.hlapi import *
import time
def snmp_get(ip, oid, n=0):
    
    g = getCmd(SnmpEngine(),  # 创建SNMP引擎
               CommunityData('public'),  # 团体属性
               # userData,交换机没有配认证，这里就不需要
               UdpTransportTarget((ip, 161), timeout=1, retries=0),  # 创建被管理设备信息 包含IP和端口号 超时1秒 不重试
               ContextData(),  # 创建SNMP上下文信息
               ObjectType(ObjectIdentity(oid))  # 创建MIB节点对象 #要跟参数 否则会报错
               )
    errorIndication, errorStatus, errorIndex, varBinds = next(g)  # 发送Get请求，获取sysName
    if errorIndication:#重传三次
        if n < 3:
            n += 1
            time.sleep(0.5)
            print(ip, oid, '重试snmp_get')
            return snmp_get(ip, oid, n)
        return 'error'
    else:
        return [x.prettyPrint() for x in varBinds[0]]#列表生成器，把结果变为列表

#print(snmp_get('192.1.1.28', '1.3.6.1.4.1.3090.5.4.6.2.1.2.8'))
print(snmp_get('192.1.1.28', '1.3.6.1.4.1.3090.5.4.10.1.1.1.83.229'))


