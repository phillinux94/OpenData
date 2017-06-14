#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from OpenData import OpenRevenus


r = OpenRevenus("75105")

print(r.codeGeographique())
print(r.dataset())
print(r.nombrePersonneMenagesFiscaux())
print(r.revenuMedian())
print(r.nombreMenagesFiscaux())
print(r.nomCommune())

print(r.partRetraites())
print(r.partRevenuActivite())
print(r.partPrestationsSociales())
print(r.partRevenusPatrimoine())
print(r.partImpots())
print(r.tauxPauvreteMoins30ans())
print(r.tauxPauvrete30à39())
print(r.tauxPauvrete40à49())
print(r.tauxPauvrete50à59())
print(r.tauxPauvrete60à74())
print(r.tauxPauvretePlus74())
print(r.tauxPauvreteProprietaire())
print(r.tauxPauvreteLocataire())
print(r.tauxPauvreteEnsemble())
print(r.dateInformation())
print(r.validiteJeu())