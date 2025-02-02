import pyfiglet
import socket
import time

result = pyfiglet.figlet_format("PortSpy")
print(result)
print ("\nAuthor - MR SUDO")
print ("Copyright 2022")

time.sleep(0.2)

# Dictionary of ports and their associated service names (partial list)
ports_and_services = {
    0: "Reserved",
    1: "TCP Port Service Multiplexer",
    7: "Echo",
    9: "Discard",
    11: "Systat",
    13: "Daytime",
    17: "Quote of the Day",
    19: "Character Generator",
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "Trivial File Transfer Protocol (TFTP)",
    80: "HTTP",
    110: "POP3",
    115: "Simple File Transfer Protocol (SFTP)",
    119: "Network News Transfer Protocol (NNTP)",
    123: "Network Time Protocol (NTP)",
    143: "IMAP",
    161: "Simple Network Management Protocol (SNMP)",
    162: "SNMP Trap",
    177: "X Window System",
    194: "Internet Relay Chat (IRC)",
    443: "HTTPS",
    445: "Microsoft-DS",
    465: "SMTPS",
    514: "Remote Shell (rsh)",
    515: "Line Printer Daemon (LPD)",
    543: "Klogin",
    548: "AppleTalk Filing Protocol (AFP)",
    561: "Biff",
    587: "SMTP (Submission)",
    636: "LDAP (Secure)",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Server Resolution",
    1521: "Oracle Database",
    1723: "PPTP",
    3306: "MySQL",
    3389: "Remote Desktop Protocol (RDP)",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP (Alternate)",
    8081: "HTTP (Alternate)",
    8443: "HTTPS (Alternate)",
    9000: "SonarQube",
    10000: "Webmin",
    12345: "NetBus",
    31337: "Back Orifice",
    33060: "MySQL (X Protocol)",
    44444: "Blaster Worm",
    49152: "Dynamic/Private Ports",
    65535: "Reserved",
}

def scan_ports(ip):
    print(f"Scanning ports on {ip}...")
    
    # Scan ports from 1 to 1024 (well-known ports and some common ones)
    for port in range(1, 1025):
        service_name = ports_and_services.get(port, 'Unknown')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection attempt
        result = sock.connect_ex((ip, port))  # Try to connect to the port
        
        if result == 0:
            print(f"Port {port} ({service_name}) is open")
        sock.close()

if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    scan_ports(ip_address)
