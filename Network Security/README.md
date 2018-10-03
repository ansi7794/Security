# Network Security - Anomaly Detection

This program takes one command-line parameter, the path of the PCAP file to be analyzed,

## Example:
### Input:
python2.7 detector.py capture.pcap

### Output:
Set of IP addresses (one per line) that sent at least 3 times more SYN
packets than than the number of SYN+ACK packets they received. The program silently
ignores packets that are malformed or that are not using Ethernet, IP, and TCP.
