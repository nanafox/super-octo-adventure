# The Network Technician's Toolbox

## What's in it?

### Network Testing and Sniffing Tools

- **ping** (aliased to `ping -c 5`)
  - Supports both IPv4 and IPv6 testing
  - Pings are limited to 5 counts.
  - this behavior can be modified by editing the *~/.bash_aliases* file
- **traceroute**
- **tracepath**
  - Network path tracer. It also attempts to discover the MTU of the path
  - IPv4 and IPv6 support. See `tracepath6` on how to use if for IPv6 testing
- **tracepath6** (aliased to `tracepath -6`)
  - the original command syntax could be used as well. E.g. `tracepath -6 <destination>`
  - the aliased version is just for convenience sake.
  To use it the syntax looks like this `tracepath6 <destination>`
- **arp**
- **arping (ARP ping)**
  - MAC Address -> IP Address
  - use this when you have the MAC address of a host and want to find the Layer 3 address
  associated with it
  - Examples
    - `arping 02:42:ac:11:00:02`
- **nmap**
- **Tshark**
- **tcpdump**
- **dsniff**
  - macof (MAC Address Spoofing)
    - great for testing DHCP Snooping, Dynamic ARP Inspection and Port Security

### Network Management and Monitoring Tools

- **SSH**
- **SNMP**
  - inlcudes traps
- **Syslog**
- **DHCP Client**
- **FTP Server and Client**
  - SFTP Server (vsftpd)
  - TFTP client (tftp)
- **IP Address Calculator (ipcalc-ng)**
  - IPv4 and IPv6 support

### Test Editors

- **Vim**
- **Nano**
