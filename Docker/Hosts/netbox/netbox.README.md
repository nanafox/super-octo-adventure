# The Network Technician's Toolbox

## What's in it?

### **Network Rechability Testing Tools**

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
  - Find the Layer 2 (MAC Address) address associated with Layer 3 (IP Address) address

### **Network Sniffing Tools**

- **nmap**
- **tcpdump**
- **macof** (MAC Address Spoofing) - flood the local network with random MAC addresses.
  - great for testing Port Security
- **arpspoof**  - Send out unrequested (and possibly forged) arp replies.
  - Dynamic ARP Inspection, DHCP Snooping
- **dnsspoof**  - forge replies to arbitrary DNS address / pointer queries the Local Area Network.
- **dsniff**    - password sniffer for several protocols.
- **filesnarf** - saves selected files sniffed from NFS traffic.
- **mailsnarf** - sniffs mail on the LAN and stores it in mbox format.
- **msgsnarf**  - record selected messages from different Instant Messengers.
- **sshmitm**   - SSH monkey-in-the-middle. proxies and sniffs SSH traffic.
- **sshow**     - SSH traffic analyser.
- **tcpkill**   - kills specified in-progress TCP connections.
- **tcpnice**   - slow down specified TCP connections via "active"shaping.
- **urlsnarf**  - output selected URLs sniffed from HTTP traffic in CLF.
- **webmitm**   - HTTP / HTTPS monkey-in-the-middle. transparently proxies.
- **webspy**    - sends URLs sniffed from a client to your local browser

### **Network Management and Monitoring Tools**

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
