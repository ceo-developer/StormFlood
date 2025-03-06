# StormFlood v4.1 - Ultimate Auto UDP Flood Tool with TOR Support  

## Developed by:
- **Telegram ID:** [dəˈveləpər](https://t.me/hiden_25)  
- **Telegram Channel:** [H2I CODER </>](https://t.me/h2icoder)  

---

## Overview  

**StormFlood v4.1** is an advanced UDP flooding tool with **TOR Proxy Support** for **100% anonymity**. It allows penetration testers and security researchers to stress-test networks while remaining untraceable using the **TOR network**.  

> **Disclaimer:**  
> This tool is meant for ethical hacking, research, and educational purposes **ONLY**. Unauthorized use of this tool is illegal and punishable by law. The developer is not responsible for any misuse.  

---

## Features  

✅ **UDP Flood Attack** - High-speed attack using randomly generated packets.  
✅ **TOR Proxy Support** - Routes traffic through TOR for complete anonymity.  
✅ **Multi-threading** - Enables faster and more effective flooding.  
✅ **Adjustable Packet Size** - Random packet sizes from **512 to 2048 bytes**.  
✅ **Easy-to-Use** - Simple commands to configure attack parameters.  

---

## Requirements  

- **Python 3.x**  

Python modules needed (included in `requirements.txt`):  
- [PySocks](https://pypi.org/project/PySocks/) (For proxy support)  
- [Stem](https://stem.torproject.org/) (For interacting with the TOR network)  

To install dependencies, run:  
```bash
pip3 install -r requirements.txt
```

---

## Installation & Usage  

### 📱 Termux (Android)  
1. Install **Termux** from Play Store or F-Droid.  
2. Update and install Python:  
   ```bash
   pkg update && pkg upgrade  
   pkg install python  
   ```  
3. Clone the repository:  
   ```bash
   git clone https://github.com/ceo-developer/StormFlood.git  
   cd StormFlood
   ```  
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```  
5. **Enable TOR Support:**  
   ```bash
   pkg install tor  
   tor  
   ```  
6. Run the script:  
   ```bash
   python stormflood.py  
   ```  

---

### 🖥️ Kali Linux / Parrot OS  
1. Open **Terminal** and install required packages:  
   ```bash
   sudo apt update && sudo apt upgrade  
   sudo apt install python3 python3-pip tor  
   ```  
2. Clone the repository:  
   ```bash
   git clone https://github.com/ceo-developer/StormFlood.git
   cd StormFlood  
   ```  
3. Install required modules:  
   ```bash
   pip3 install -r requirements.txt  
   ```  
4. Start the **TOR Service**:  
   ```bash
   service tor start  
   ```  
5. Run the tool:  
   ```bash
   python3 stormflood.py  
   ```  

---

### 🖥️ Windows  
1. Download and **install Python 3** from [python.org](https://www.python.org/downloads/).  
2. Open **Command Prompt (cmd)**.  
3. Clone the repository:  
   ```bash
   git clone https://github.com/ceo-developer/StormFlood.git
   cd StormFlood
   ```  
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```  
5. Download and **install TOR** from [torproject.org](https://www.torproject.org/download/).  
6. Open TOR and **start the service**.  
7. Run the script:  
   ```bash
   python stormflood.py  
   ```  

---

## 🔥 Usage Instructions  
After launching the script, enter the **target IP, port, and duration**:  
```bash
[$] Target IP: 192.168.1.1  
[$] Enter Port (Default: 80): 8080  
[$] Enter Attack Duration (seconds): 60  
[?] Use TOR Proxy? (y/n): y  
```  
If **TOR is enabled**, the attack will be routed through the **TOR network** for **maximum anonymity**.  

---

## Contributing  
Contributions and suggestions are welcome! Fork the repo, make changes, and submit a pull request. For major changes, please open an issue first.  

---

## 📢 Contact & Support  
For any queries or support, feel free to reach out:  
- **Telegram ID:** [dəˈveləpər](https://t.me/hiden_25)  
- **Telegram Channel:** [H2I CODER </>](https://t.me/h2icoder)  

---

**Stay Anonymous | Use Responsibly | Ethical Hacking Only**🚀
