#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
import os
import re
mini=var.split("&")[0].split("=")[1]
hor=var.split("&")[1].split("=")[1]
dia=var.split("&")[2].split("=")[1]
mes=var.split("&")[3].split("=")[1]
sem=var.split("&")[4].split("=")[1]
usr=var.split("&")[5].split("=")[1]
cmd=var.split("&")[6].split("=")[1]

#min=20&hor=10&dim=1&mes=1&dis=2&sem=root&cmd=ping+8.8.8.8&Agendar=Agendar

def cabecalho():
	print("content-type: text/html")
	print("")

def validacao():
	if re.match("^([*]|[1-9]|[1-5][0-9])", mini) \
		and re.match("^([*]|[0-9]|1[0-9]|2[0-3])$", hor)\
		and re.match("^([*]|[1-9]|[12][0-9]|3[01])$", dia)\
		and re.match("^([*]|[1-9]|1[0-2])$", mes)\
		and re.match("^([*][0-7])$", sem)\
		and re.match("^([*]|[A-Za-z0-9])$", usr)\
		and re.match("^.{1,}+$", cmd):

		return True
	else:
		return False

def agendar():
	so.system("echo " + \
	mini + " " + \
	hor + " " + \
	dia + " " + \
	mes + " " + \
	sem + " " + \
	usr + " " + \
	cmd + "&>> /var/www/html/cgi-bin/cron.log")

if validacao():
	cabecalho()
	agendar()
	print("<h1>Agendamento Concluído</h1>")
else:
	cabecalho()
	print("<h1>Erro</h1>")
