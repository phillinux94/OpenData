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
        return(self.reponseData['parameters']['refine']['codgeo'])
    
    def dataset(self):
        
        # Nom du Dataset
        return(self.reponseData['parameters']['dataset'][0])
    
    def nombrePersonneMenagesFiscaux(self):
        
        # Nombre de personnes dans les ménages fiscaux
        return(self.reponseData['records'][0]['fields']['nombre_de_personnes_dans_les_menages_fiscaux'])
    
    def revenuMedian(self):
        
        # Revenu médian
        return(self.reponseData['records'][0]['fields']['mediane_revenu_disponible_par_uc_en_euros'])
    
    def nombreMenagesFiscaux(self):
        
        # Nombre de ménages fiscaux
        return(self.reponseData['records'][0]['fields']['menages_fiscaux'])
    
    def nomCommune(self):
        
        # Nom de la commune
        return(self.reponseData['records'][0]['fields']['libelle_commune_ou_arm'])
    
    def partRetraites(self):
        
        # Part des retraites 
        return(self.reponseData['records'][0]['fields']['part_pensions_retraites_rentes'])

    def partRevenuActivite(self):
        
        # Part des revenus d'activité
        return(self.reponseData['records'][0]['fields']['part_revenus_d_activite'])
        
    def partPrestationsSociales(self):
        
        # Part des prestations sociales
        return(self.reponseData['records'][0]['fields']['part_prestations_sociales_ensemble'])
    
    def partRevenusPatrimoine(self):
        
        # Part des revenus du patrimoine
        return(self.reponseData['records'][0]['fields']['part_revenus_du_patrimoine'])
    
    def partImpots(self):
        
        # Part des impôts
        return(self.reponseData['records'][0]['fields']['part_impots'])
    
    def tauxPauvreteMoins30ans(self):
        
        # Taux de pauvreté des moins de 30 ans
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_moins_de_30_ans'])
        
    def tauxPauvrete30à39(self):
        
        # Taux de pauvreté de 30 à 39 ans
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_30_a_39_ans'])
    
    def tauxPauvrete40à49(self):
        
        # Taux de pauvreté de 40 à 49 ans
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_40_a_49_ans'])
    
    def tauxPauvrete50à59(self):
        
        # Taux de pauvreté de 50 à 59 ans
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_50_a_59_ans'])
    
    def tauxPauvrete60à74(self):
        
        # Taux de pauvreté de 60 à 74 ans
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_60_a_74_ans'])
    
    def tauxPauvretePlus74(self):
        
        # Taux de pauvreté 75 ans et plus
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_75_ans_ou_plus'])
    
    def tauxPauvreteProprietaire(self):
        
        # Taux de pauvreté des propriétaires
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_proprietaire'])
    
    def tauxPauvreteLocataire(self):
        
        # Taux de pauvreté des locataires
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_locataire'])
    
    def tauxPauvreteEnsemble(self):
        
        # Taux de pauvreté de l'ensemble
        return(self.reponseData['records'][0]['fields']['taux_de_pauvrete_ensemble'])
        