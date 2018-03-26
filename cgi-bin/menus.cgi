#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
menu=var.split("=")[0]

def cabecalho():
	print("content-type: text/html")
	print("")

def gerencia():
	cabecalho()
	ge=open("/var/www/html/gerencia.html", "r")
	html=ge.read()
	ge.close()
	print(html)

def processos():
	cabecalho()
	pro=open("/var/www/html/processos.html", "r")
	html=pro.read()
	pro.close()
	print(html)

def agenda():
	cabecalho()
	age=open("/var/www/html/agenda.html", "r")
	html=age.read()
	age.close()
	print(html)

def erro():
	cabecalho()
	print("<h1>ERROOOOOOOO!</h1>")

if menu == "geren":
	gerencia()
elif menu == "proc":
	processos()
elif menu == "agen":
	agenda()
else:
	erro() 
