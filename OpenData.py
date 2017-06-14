#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import json


class OpenRevenus:
    
    def __init__(self, codeInsee):
        
        # Constitution URL Web Service Open Data Soft
        urlRevenus = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=revenu-pauvrete-menage-2012%40public&facet=codgeo&facet=libelle_commune_ou_arm&refine.codgeo="
        urlRevenus = urlRevenus + codeInsee
        
        # Soumission requête HTTP
        reponse = requests.get(urlRevenus)
        
        # Parsing de la réponse JSON
        self.reponseData = json.loads(reponse.text)
        
        
    def codeGeographique(self): 
        
        # Code géographique (code INSEE)
        try:
            reponse = self.reponseData['parameters']['refine']['codgeo']
        except IndexError:
            reponse = ""
        
        return reponse
    
    
    def dataset(self):
        
        # Nom du Dataset
        try:
            reponse = self.reponseData['parameters']['dataset'][0]
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def nombrePersonneMenagesFiscaux(self):
        
        # Nombre de personnes dans les ménages fiscaux
        try:
            reponse = self.reponseData['records'][0]['fields']['nombre_de_personnes_dans_les_menages_fiscaux']
        except IndexError:
            reponse = ""
        return reponse
    
    
    def revenuMedian(self):
        
        # Revenu médian
        try:
            reponse = self.reponseData['records'][0]['fields']['mediane_revenu_disponible_par_uc_en_euros']
        except IndexError:
            reponse = ""
        
        return reponse
    
    
    def nombreMenagesFiscaux(self):
        
        # Nombre de ménages fiscaux
        try:
            reponse = self.reponseData['records'][0]['fields']['menages_fiscaux']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def nomCommune(self):
        
        # Nom de la commune
        try:
            reponse = self.reponseData['records'][0]['fields']['libelle_commune_ou_arm']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def partRetraites(self):
        
        # Part des retraites 
        try:
            reponse = self.reponseData['records'][0]['fields']['part_pensions_retraites_rentes']
        except IndexError:
            reponse = ""
            
        return reponse
    

    def partRevenuActivite(self):
        
        # Part des revenus d'activité
        try:
            reponse = self.reponseData['records'][0]['fields']['part_revenus_d_activite']
        except IndexError:
            reponse = ""
            
        return reponse
    
        
    def partPrestationsSociales(self):
        
        # Part des prestations sociales
        try:
            reponse = self.reponseData['records'][0]['fields']['part_prestations_sociales_ensemble']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def partRevenusPatrimoine(self):
        
        # Part des revenus du patrimoine
        try:
            reponse = self.reponseData['records'][0]['fields']['part_revenus_du_patrimoine']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def partImpots(self):
        
        # Part des impôts
        try:
            reponse = self.reponseData['records'][0]['fields']['part_impots']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvreteMoins30ans(self):
        
        # Taux de pauvreté des moins de 30 ans
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_moins_de_30_ans']
        except IndexError:
            reponse = ""
            
        return reponse
    
        
    def tauxPauvrete30à39(self):
        
        # Taux de pauvreté de 30 à 39 ans
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_30_a_39_ans']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvrete40à49(self):
        
        # Taux de pauvreté de 40 à 49 ans
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_40_a_49_ans']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvrete50à59(self):
        
        # Taux de pauvreté de 50 à 59 ans
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_50_a_59_ans']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvrete60à74(self):
        
        # Taux de pauvreté de 60 à 74 ans
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_60_a_74_ans']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvretePlus74(self):
        
        # Taux de pauvreté 75 ans et plus
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_75_ans_ou_plus']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvreteProprietaire(self):
        
        # Taux de pauvreté des propriétaires
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_proprietaire']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvreteLocataire(self):
        
        # Taux de pauvreté des locataires
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_locataire']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def tauxPauvreteEnsemble(self):
        
        # Taux de pauvreté de l'ensemble
        try:
            reponse = self.reponseData['records'][0]['fields']['taux_de_pauvrete_ensemble']
        except IndexError:
            reponse = ""
            
        return reponse
    
    
    def dateJeuDonnees(self): 
        
        # Date information Web Service
        try:
            reponse = self.reponseData['records'][0]['record_timestamp']
        except IndexError:
            reponse = ""
        
        return reponse
    
    def validiteJeu(self):
        
        # Jeu de données valide
        if len(self.reponseData['records']) > 0:
            reponse = True
        else:
            reponse = False
        
        return reponse
