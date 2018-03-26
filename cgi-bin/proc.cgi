#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()

import os

acao=var.split("=")[0]

def cabecalho():
	print("content-type: text/html")
	print("")

def bindo():
	binn=open("/dns.tmp", "r")
	bind9=binn.read()
	binn.close
	print(bind9)

def nagio():
	nagg=open("/nag.tmp", "r")
	nagios=nagg.read()
	nagg.close
	print(nagios)

def fire():
	fill=open("/fire.tmp", "r")
	firer=fill.read()
	fill.close
	print ("<h1>")
	print(firer)
	print ("</h1>")

def tudo():
	tutu=open("/todos.tmp", "r")
	tt=tutu.read()
	tt.close
	print(tutu)

if acao == "bind":	
	cabecalho()
	print("<h1>Serviço BIND9</h1>")
	print ("<textarea rows='100' cols='100'>")
	os.system("/etc/init.d/bind9 status > /dns.tmp")
	bindo()

elif acao == "nag":
	cabecalho()
	print("<h1>Serviço NAGIOS</h1>")
	print ("<textarea rows='100' cols='100'>")
	os.system("/etc/init.d/nagios3 status > /nag.tmp")
	nagio()

elif acao == "fire":
	cabecalho()
	print("<h1>Serviço FIREWALL</h1>")
	print ("<textarea rows='100' cols='100'>")	
	os.system("iptables -L > /fire.tmp")	
	fire()
	
elif acao == "tod":
	cabecalho()
	print("<h1>Todos os Serviços</h1>")
	print ("<textarea rows='100' cols='100'>")
	os.system("ps -aux > /todos.tmp")
	a=open("/todos.tmp", "r")
	vm=a.read()
	a.close
	print(vm)
