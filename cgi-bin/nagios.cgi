#!/usr/bin/python
#-*- coding: utf8 -*-
var=raw_input()

import os

acao=var.split("=")[1]

print("content-type: text/html")
print("")

if acao == "Iniciar":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 start")
	print("<h1>Iniciado!!!</h1>")
elif acao == "Parar":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 stop")
	print("<h1>Parado!!!</h1>")
elif acao == "Reiniciar":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1>Reiniciado!!!</h1>")

