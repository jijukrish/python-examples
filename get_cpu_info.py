#read cpu information from /proc/cpuinfo
try:
    with open('/proc/cpuinfo','r') as f:
        cpu_info = f.read()
    print(f"CPU info:\n{cpu_info[:200]}...")
except FileNotFoundError:
    print("/proc/cpuinfo not found")

#Read network device information from /sys/class/net
import os
try:
    net_devices = os.listdir('/sys/class/net')
    print(f"Network devices:{','.join(net_devices)}")
except FileNotFoundError:
    print("/sys/class/net not found.")
