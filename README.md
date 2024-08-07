# 基于snmp的设备监控
利用Python对基于SNMP协议的设备进行状态数据的采集，以及对该设备的控制。这里利用pysnmp第三方模块。主要提供三种方法：
* getCmd方法取具体的OID的值，参见snmp_get.pys
* setCmd方法修改具体的OID的配置，参见snmp_set.py
* bulkCmd方法对OID值的遍历，参见snmp_bulk.py