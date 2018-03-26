#!/usr/bin/python
#-*- coding: utf8 -*-
var=raw_input()

import os

acao=var.split("=")[0]

print("content-type: text/html")
print("")

if acao == "Iniciar":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
	print("<h1>Iniciado!!!</h1>")
elif acao == "Parar":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
	print("<h1>Parado!!!</h1>")
elif acao == "Reiniciar":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
	print("<h1>Reiniciado!!!</h1>")

