iptables --flush
iptables -A INPUT -p tcp --sdport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -j ACCEPT
iptables -A OUTPUT -j ACCEPT
iptables -A FORWARD -j ACCEPT
iptables -A INPUT -j REJECT
iptables -A OUTPUT -j REJECT
iptables -A FORWARD -j REJECT
