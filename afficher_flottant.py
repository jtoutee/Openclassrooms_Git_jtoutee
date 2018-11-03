def afficher_flottant(flottant):
	# openclassrooms
	#convertir float en str:
	chaine=str(flottant)
	#convertir str en list, avec s�parateur = .:
	liste=chaine.split(sep='.')
	#pour la partie d�cimale (2e �l�ment de la liste), ne conserver que 3 chiffres (on travaille directement sur le 2e elt de la liste):
	liste[1]=liste[1][0:3]
	#joindre les 2 �l�ments (partie enti�re et d�cimales tronqu�es) en utilisant ',' comme caract�re de jonction
	return ",".join(liste)
	
def afficher(*parametres, sep=' ', fin='\n'):
	#Convertir *parametres (qui est un tuple) en une liste:
	parametres=list(parametres)
	#convertir chaque �l�ment de la liste en chaine:
	for i, element in enumerate(parametres):
		parametres[i]=str(element)
	#joindre les �l�ments en utlisant les s�parateur fourni en param�tre:
	chaine=sep.join(parametres)
	#ajouter le param�tre de fin:
	chaine+=fin
	print(chaine, end='')