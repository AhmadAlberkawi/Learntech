#!/bin/python

# Modul cgi
import cgi, cgitb

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
#form = cgi.FieldStorage()

# Einzelne Elemente des Objekts
name = form.getvalue('Name')
vorname = form.getvalue('Vorname')
email = form.getvalue('Email')

# HTML-Dokument mit Variablen
print ("content-type: text/html\n")

print ("<!DOCTYPE html>")
print ('<html lang="de">')
print ("<head>")
print ("<title>Dateneingabe</title>")
print ('<link rel="stylesheet" href="stylesheet.css">')
print ("</head>")
print ("<body>")
print ("<p><b>Registrierte Daten:</b></p>")
print ("<p>Nachname:", name, "</p>")
print ("<p>Vorname:", vorname, "</p>")
print ("<p>Email:", email, "</p>")

print ("</body>")
print ("</html>")
