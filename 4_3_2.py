import socket
import json
import yaml


log_old_address = open('address.log', 'r')
old_address = json.loads(log_old_address.read())
dns_hosts = ["drive.google.com", "mail.google.com", "google.com"]
ip_hosts = []
for resolve in dns_hosts:
    ip_hosts.append(socket.gethostbyname(resolve))
real_address = dict(zip(dns_hosts, ip_hosts))
log_address = open('address.log', 'w')
log_address.write(json.dumps(real_address))
log_address.close()
for item in real_address:
    if (real_address[item] == old_address[item]):
        print(item ,'-', real_address[item])
    else:
        print('[Error]',item,'','ip mismatch:', old_address[item],'', real_address[item])


