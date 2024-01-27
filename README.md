# network-rst-attack
please use this for "education purposes" only and i am not responsible for any unethical stuff you do with this code, instructions are in the code, open the rst.py file, there will be infromation inside.


this code spoofs ur mac and ip into the device you want to attack, and sends alot of rst tcp requests to the router the device is connected too, so then they can disconnect easily.
the code is not complete yet, maybe later ill add a part where it also adds the handshake in, so its more realistic to the router that the device wants to disconnect.

<: REPLACE THESE PARTS :>
    source_ip = "10.9.1.0" #the device u want to disconnect, its ip adress, like ur friends computer's ip adress
    source_mac = "3c:a6:f6:01:83:01" #ur friends mac adress
    router_ip = "10.9.0.1"  # Replace with the actual router IP
    router_port = 22  # Replace with actual router port (sudo nmap router_ip)
    target_mac = "6c:8d:77:7d:a2:4d" # replace with actual router mac adress
