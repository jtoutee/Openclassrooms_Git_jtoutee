def afficher_flottant(flottant):
	# openclassrooms
	#convertir float en str:
	chaine=str(flottant)
	#convertir str en list, avec séparateur = .:
	liste=chaine.split(sep='.')
	#pour la partie décimale (2e élément de la liste), ne conserver que 3 chiffres (on travaille directement sur le 2e elt de la liste):
	liste[1]=liste[1][0:3]
	#joindre les 2 éléments (partie entière et décimales tronquées) en utilisant ',' comme caractère de jonction
	return ",".join(liste)
	
def afficher(*parametres, sep=' ', fin='\n'):
	#Convertir *parametres (qui est un tuple) en une liste:
	parametres=list(parametres)
	#convertir chaque élément de la liste en chaine:
	for i, element in enumerate(parametres):
		parametres[i]=str(element)
	#joindre les éléments en utlisant les séparateur fourni en paramètre:
	chaine=sep.join(parametres)
	#ajouter le paramètre de fin:
	chaine+=fin
	print(chaine, end='')