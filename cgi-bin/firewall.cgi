#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os

acao=var.split("=")[1]

print("content-type: text/html")
print("")

if acao == "Iniciar":
	os.system("sudo /usr/lib/cgi-bin/iniciar.sh")
	print("<h1>Iniciado!!!</h1>")
elif acao == "Parar":
	os.system("sudo /usr/lib/cgi-bin/panico.sh")
	print("<h1>Parado!!!</h1>")
elif acao == "Reiniciar":
	os.system("sudo /usr/lib/cgi-bin/reiniciar.sh")
	print("<h1>Reiniciado!!!</h1>")

