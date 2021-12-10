# devops-netology
 В terraform.gotignor судя по всему будут игнориороваться:
1.локальные каталоги terrraform
** /. terraform / *
2.файлы файлы .tfstate
3.Файлы журналов
4. исключаются файлы содержащие пароли/приватные ключи и тд 
.tfvars
5.Файлы переопределения, ибо они используются для локального переопределения ресурсов
override.tf
override.tf.json
*_override.tf
*_override.tf.json
6.игнорируется файлы конфигурации CLI
.terraformrc
terraform.rc
