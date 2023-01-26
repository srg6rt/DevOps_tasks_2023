## Linux Networking

<img src="./docs/images/lan_schema.png" />

On Server_1 configure static addresses on all interfaces.

<img src="./docs/images/ip_address_set_server_1.png" />

On Server_1, configure a DHCP service that will configure Int1 Client_1 and Client_2 addresses

<img src="./docs/images/install_dhcp_server.png" />

Configure /etc/dhcp/dhcpd.conf

<img src="./docs/images/dhcpd.conf.png" />

Configure /etc/default/isc-dhcp-server

<img src="./docs/images/isc-dhcp-server.png" />

Enable ip forwarding data between local interfaces:

<strong>echo 1 > /proc/sys/net/ipv4/ip_forward </strong>

Ping packet send to default route throuth Server_1 (10.83.17.1)  via enp0s8 interface. Reach Clien_2 (10.9.83.100) and go back throuth Server_1 (10.83.17.1) via enp0s3 interface.

<img src="./docs/images/traceroute_client2.png" />

Set static route on router 192.168.1.1 for internet access from Client_1 and Client_2 hosts.

<img src="./docs/images/static_route_on_router_192.168.1.1.png" />

Set Net4 LAN:

<img src="./docs/images/Net4_Client_2.png" />

<img src="./docs/images/Net4_Client_1.png" />

Assign two IP addresses on the lo virtual interface Client_1 host:

<img src="./docs/images/set_two_lo_interfaces.png" />

Configure routing 172.17.27.0/24 throuth Server_1.

On Client_2 host set static route throuth net4

<strong>sudo ip route add 172.17.27.0/24 via 10.9.83.1</strong>

On Server_1 host set static route throuth net4

<strong>sudo ip route add 172.17.27.0/24 via 10.83.17.1</strong>

<img src="./docs/images/mtr_client_2_through_Server_1.png" />

Configure routing 172.17.37.0/24 throuth Net4.

On Client_2 host set static route throuth net4

<strong>sudo ip route add 172.17.37.0/24 via 172.16.17.2</strong>

On Client_1 host set static route throuth net4

<strong>sudo ip route add 172.17.37.0/24 via 172.16.17.1</strong>

<img src="./docs/images/mtr_client_2_through_Net4.png" />

Calculate the summarizing addresses 172.17.27.1 and 172.17.37.1, with the mask being as large as possible.

For 172.17.27.1 and 172.17.37.1
<pre>
Network Address	Usable Host Range		Broadcast Address:
172.17.0.0	172.17.0.1 - 172.17.63.254	172.17.63.255

172.17.0.0   	255.255.192.0/18</pre>

On Server_1 host set static route 

<strong>sudo ip route add 172.17.0.0/18 via 10.83.17.1</strong>

<img src="./docs/images/route_on_server_1_for_172.17.0.0.png" />

<img src="./docs/images/ping_27_37.png" />


Set ssh server on Server_1

<strong>sudo apt install openssh-server</strong>

Connect to Server_1 from Client_1

<img src="./docs/images/ssh_Client_1.png" />

Connect to Server_1 from Client_2

<img src="./docs/images/ssh_Client_2.png" />

Set ssh server on Client_1

<strong>sudo apt install openssh-server</strong>

Set ssh server on Client_2

<strong>sudo apt install openssh-server</strong>

Connect to Client_2 from Client_1

<img src="./docs/images/ssh_from_Client_1_to_Clien2.png" />

Connect to Client_1 from Client_2

<img src="./docs/images/ssh_from_Client_2_to_Clien1.png" />

Server_1 firewall:

<strong>sudo ufw enable</strong>

Allow ssh connection from Client_1

<strong>sudo ufw allow from 10.83.17.100</strong>

Ping reject from Client2 to 172.17.37.1

Add rule to /etc/ufw/before.rules

<img src="./docs/images/ping_reject_from_Client2_to_172.17.37.1.png" />

<img src="./docs/images/ping_unreacheble.png" />

Set NAT on Server_1 for 10.83.17.0/24 and 10.9.83.0/24

Enable fowarding 

<img src="./docs/images/forwarding.png" />

Edit /etc/ufw/before.rules

<img src="./docs/images/NAT_rules.png" />

Ping from Client_1

<img src="./docs/images/ping_from_Client_1_NAT.png" />

Mtr from Client_2

<img src="./docs/images/mtr_from_Client_2_NAT.png" />