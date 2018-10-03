#Submitted by: Anushree Srinivasan

import sys
import dpkt
import socket

capture = str(sys.argv[1])

file = open(capture)
pcap = dpkt.pcap.Reader(file)

syn_sent = dict()
syn_ack_rec = dict()

count = 0

for ts, buff in pcap:
    try:
        eth = dpkt.ethernet.Ethernet(buff)
    except:
       continue

    if type(eth.data) != dpkt.ip.IP:
        continue
    
    ip = eth.data
    if type(ip.data) != dpkt.tcp.TCP:
        continue

    tcp = ip.data
    if tcp != '':
        if 1 == 1:
            syn_flag = ( tcp.flags & dpkt.tcp.TH_SYN ) != 0
            ack_flag = ( tcp.flags & dpkt.tcp.TH_ACK ) != 0

            this_src = socket.inet_ntoa(ip.src)
            this_dst = socket.inet_ntoa(ip.dst)
            
            if not (this_src in syn_sent):
                syn_sent[this_src] = 0
            if not (this_dst in syn_ack_rec):
                syn_ack_rec[this_dst] = 0    
            if not (this_src in syn_ack_rec):
                syn_ack_rec[this_src] = 0
            
            if syn_flag == True and ack_flag == False:
                this_ip = socket.inet_ntoa(ip.src)
                syn_sent[this_ip] += 1
            
            elif syn_flag == True and ack_flag == True:
                this_ip = socket.inet_ntoa(ip.dst)
                syn_ack_rec[this_ip] += 1


for syn_val in syn_sent:
    if (syn_val in syn_sent) and (syn_val in syn_ack_rec):
        if syn_sent[syn_val] > 3*syn_ack_rec[syn_val]:
            print syn_val
    


