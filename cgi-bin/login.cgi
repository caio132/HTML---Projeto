#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

def cabecalho():
	print("content-type: text/html")
	print("")

def menu():
	cabecalho()
	f=open("/var/www/html/menu.html", "r")
	html=f.read()
	f.close()
	print(html)

def erro():
	cabecalho()
	print("<h1>Login Falhou...</h1>")

if usuario == "grupo6" and senha == "senai132":
	menu()
else:
	erro()
