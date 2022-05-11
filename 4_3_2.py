import json
import socket
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
with open('json_file.json', 'w') as js:
    js.write('')
with open('yaml_file.yml','w') as ym:
    ym.write('')

for item in real_address:
    if (real_address[item] == old_address[item]):
        print(item ,'-', real_address[item])
        wr1 = {item:real_address[item]}
        with open('json_file.json','a') as json:
            json.write(json.dumps(wr1))
        with open('yaml_file.yml','a') as yaml:
            yaml.write(yaml.dump(wr1))
    else:
        print('[Error]',item,'','ip mismatch:', old_address[item],'', real_address[item])
        wr2 = {item:real_address[item]}
        with open('json_file.json','a') as json:
            json.write(json.dumps(wr2))
        with open('yaml_file.yml','a') as yaml:
            yaml.write(yaml.dump(wr2))
