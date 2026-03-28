"""

Note: This scanner is a simple example and not suitable for
production use. By default it targets localhost (127.0.0.1).

"""

import socket

# Dictionary mapping common port numbers and their namesS
PORT_NAMES = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    25 : "SMTP",
    53 : "DNS",
    80 : "HTTP",
    443 : "HTTPS",
    445 : "SMB",
    3389 : "RDP",
}

# Iterate through the defined ports and check if they are open or closed.
for port in PORT_NAMES:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    status = s.connect_ex(("127.0.0.1", port))
    
    if status == 0:
        print(f"Port {port} ({PORT_NAMES[port]}) is open.")
    else:
        print(f"Port {port} ({PORT_NAMES[port]}) is closed.")

