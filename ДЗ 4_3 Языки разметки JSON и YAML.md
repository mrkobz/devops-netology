# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"


## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip" : "71.78.22.43"
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис 
  
    Ответ: не было обернуто в кавычки ip, 71.78.22.43 
## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
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
        with open('json_file.json','a') as jsn:
            jsn.write(json.dumps(wr1))
        with open('yaml_file.yml','a') as yml:
            yml.write(yaml.dump(wr1))
    else:
        print('[Error]',item,'','ip mismatch:', old_address[item],'', real_address[item])
        wr2 = {item:real_address[item]}
        with open('json_file.json','a') as jsn:
            jsn.write(json.dumps(wr2))
        with open('yaml_file.yml','a') as yml:
            yml.write(yaml.dump(wr2))
```

### Вывод скрипта при запуске при тестировании:
```
[Error] drive.google.com  ip mismatch: 64.233.163.194  173.194.222.194
[Error] mail.google.com  ip mismatch: 142.251.1.18  74.125.131.19
[Error] google.com  ip mismatch: 64.233.162.100  64.233.164.100

Process finished with exit code 0
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "173.194.222.194"}{"mail.google.com": "74.125.131.19"}{"google.com": "64.233.164.100"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com: 173.194.222.194
mail.google.com: 74.125.131.19
google.com: 64.233.164.100
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

### Ваш скрипт:
```python
???
```

### Пример работы скрипта:
???