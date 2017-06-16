#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from OpenData import OpenRecensement

# Instanciation
r = OpenRecensement("45155")

print(r.codeInsee())
print(r.validiteJeu())
print(r.nomCommune())
print(r.recensement00à14())
print(r.recensement15à29())
print(r.recensement30à44())
print(r.recensement45à59())
print(r.recensement60à74())
print(r.recensement75())

