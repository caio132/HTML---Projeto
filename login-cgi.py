 #!/usr/bin/python
  2 #-*- coding: utf8 -*-
  3
  4 var=raw_input()
  5
  6 usuario=var.split("&")[0].split("=")[1]
  7 senha=var.split("&")[1].split("=")[1]
  8
  9 def imprime(conteudo):
 10     print("content-type: text/html")
 11     print("")
 12     print("<html><head><title>" + conteudo + "</title></head>")
 13     print("<body><h1>" + conteudo + "</h1></body></html>")
 14
 15 def cabecalho():
 16     print("content-type: text/html")
 17     print("")
 18
 19 if usuario == "caio" and senha == "123":
 20     cabecalho()
 21     f = open("site/menu.html","r")
 22     arquivo =f.read()
 23     f.close()
 24     print(arquivo)
 25 else:
 26     imprime("Login Falhou")
