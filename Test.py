#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from OpenData import OpenCodePostal

# Instanciation
r = OpenCodePostal("75009")



print(r.listeInsee())
print(r.listeCommunes())
print(r.listeLatitudes())
print(r.listeLongitudes())