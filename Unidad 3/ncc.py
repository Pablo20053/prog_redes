from ncclient import manager
import xml.dom.minidom
import xmltodict
m = manager.connect(
    host ="devnetsandboxiosxe.cisco.com",
    port= 830,
    username="admin",
    password="C1sco12345",
    hostkey_verify= False
)
netconf_filter = """
<filter>
 <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
"""
netconf_reply = m.get(filter = netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

import xmltodict
netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
 print("Name: {} MAC: {} Input: {} Output {}".format(
 interface["name"],
 interface["phys-address"],
 interface["statistics"]["in-octets"],
 interface["statistics"]["out-octets"]
 )
 )