

from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorindex, varBinds = cmdGen.setCmd(
    cmdgen.CommunityData('public'),#写入Community
    cmdgen.UdpTransportTarget(('192.1.1.28',161)),#IP地址和端口号
    ('1.3.6.1.4.1.3090.5.4.7.1.1.7.1673.5',rfc1902.OctetString('CIRCULAR'))#OID和写入的内容，需要进行编码！
)

if errorIndication:
    print('--',errorIndication)
elif errorStatus:
    print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorindex and varBinds[int(errorindex)-1][0] or '??'
        )
    )
for name,val in varBinds:
    print('%s = %s' % (name.prettyPrint(),val.prettyPrint()))#打印修改的结果

print('end')