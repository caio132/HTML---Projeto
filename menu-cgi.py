  1 #!/usr/bin/python
  2 #-*- coding:utf8 -*-
  3 import os
  4
  5 var=raw_input()
  6 #d_i=Iniciar
  7 menu=var.split("=")[0]
  8 print("content-type: text/html")
  9 print("")
 10 print("<h1>")
 11 if menu == "f_i" :
 12     print("Firewall iniciado")
 13 elif menu == "f_p":
 14     print("Firewall parado")
 15 elif menu == "f_r":
 16     print("Firewall reiniciado")
 17 elif menu == "d_i" :
 18     print("DNS iniciado")
 19     os.system("systemctl start bind9")
 20 elif menu == "d_p":
 21     print("DNS parado")
 22     logg=os.system("whoami")
 23     print("logg")
 24     os.system("systemctl stop bind9")
 25 elif menu == "d_r":
 26     print("DNS reiniciado")
 27     os.system("systemctl restart bind9")
 28 elif menu == "n_i" :
 29     print("Nagios iniciado")
 30 elif menu == "n_p":
 31     print("Nagios parado")
 32 elif menu == "n_r":
 33     print("Nagios reiniciado")
 34 else:
 35     print("Não foi possivel processar sua solicitação")
 36     print("</h1>")
