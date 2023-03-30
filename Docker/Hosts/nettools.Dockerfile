# this docker file is used for network testing and monitoring
# it contains enough tools to thoroghly test a network as well as pulling information


# use the latest Ubuntu image
FROM ubuntu

# set working directory to the home of root user
WORKDIR /root

# update and install required tools
RUN apt update
RUN apt install -y isc-dhcp-client tftp openssh-server vsftpd
RUN apt install -y rsyslog rsyslog-snmp snmp snmpd snmptrapd

# network connectivity testing tools
RUN apt install -y net-tools iproute2 bash-completion \
    inetutils-ping inetutils-traceroute iputils-tracepath

# install a CLI network capture tool - Tshark can be manually installed
RUN apt install -y nmap tcpdump

# IP Address tools and text editors
RUN apt install -y ipcalc-ng vim nano

# Add a few aliases
COPY ./bash_aliases /root/.bash_aliases