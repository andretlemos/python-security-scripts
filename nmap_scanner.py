import nmap
import sys

target = str(sys.argv[1])
ports = [21,22,80,139,443,8080]

scan_v  = nmap.PortScanner()

print(f"\nScanning {target} for ports 21,22,80,139,443,8080...\n")

for port in ports:
    portscan = scan_v.scan(target, str(port))
    print(f"Port {port} is {portscan['scan'][target]['tcp'][port]['state']}")

print(f"\nHost {target} is {portscan['scan'][target]['status']['state']}")