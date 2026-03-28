# Port Scanner

## Overview

A simple and lightweight Python port scanner designed to check the status of commonly used network ports on a target host. This tool demonstrates basic socket programming concepts and is intended for educational purposes and network diagnostics on localhost.

**Default Target:** 127.0.0.1 (localhost)

## Description

This port scanner iterates through a predefined list of popular ports (FTP, SSH, HTTP, HTTPS, etc.) and determines whether each port is open or closed by attempting a TCP connection. It provides immediate feedback on port availability with a 1-second timeout per connection attempt.

**Supported Ports:**
- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 25 (SMTP)
- 53 (DNS)
- 80 (HTTP)
- 443 (HTTPS)
- 445 (SMB)
- 3389 (RDP)

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses Python standard library)

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/iker-cpu/port-scanner.git
   cd port-scanner
   ```

2. No additional installation is needed—just run the script.

## Usage

Run the scanner with:

```bash
python3 scanner.py
```

## Limitations & Disclaimers

**Important:**

- This scanner is a **simple educational example**, not suitable for production use
- Currently targets **localhost (127.0.0.1) only**—modifying the target IP requires editing the source code
- Scans only a **fixed set of common ports**
- **No concurrent scanning**—runs sequentially (slower for large port ranges)
- Does **not perform deep protocol analysis**—only checks if a port accepts TCP connections
- Socket resources are not explicitly closed using context managers (see code review notes)

**Legal Notice:** Use this tool only on systems you own or have explicit permission to scan. Unauthorized port scanning may be illegal in your jurisdiction.

## Contributing

Contributions are welcome! If you'd like to improve this project, please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes and test thoroughly
4. Submit a pull request with a clear description of your changes

## License

This project is licensed under the MIT License—see the [LICENSE](LICENSE) file for details.

---

**Author:** Iker
**Last Updated:** March 2026
