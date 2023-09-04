import os
import sys

def effacer_ecran():
    """Cette fonction permet d'effacer l'ecran"""
    
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')

def saisir_entier(min,max,expression):
    """Cette fonction permet de controler la saisie d'un entier"""
    ok=False
    while ok==False:
        choix=input(expression)
        if choix.isdigit():
            choix=int(choix)
            if(choix>=min and choix<=max):
                return choix
            
        else:
                print("Saisir un entier")
                
   
def menu_generale():
    effacer_ecran()
    print("1----------------------------PLATS DU JOUR")
    print("2----------------------------FAST FOOD")
    print("3----------------------------CAISSE")
    print("4----------------------------QUITTER")
    
    saisir_entier(1,4,"Faites votre choix \n")
    
menu_generale()