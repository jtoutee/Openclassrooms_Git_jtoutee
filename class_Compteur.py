# -*-coding:Latin-1 -*
class Compteur:
	"""Cette classe poss�de un attribut de classe qui s'incr�mente � chaque
	fois que l'on cr�e un objet de ce type"""
	objets_crees = 0
	def __init__(self):
		"""� chaque fois qu'on cr�e un objet on incr�mente le compteur"""
		Compteur.objets_crees += 1
	def combien(cls):
		"""M�thode de classe affichant combien d'objets ont �t� cr��s"""
		print("Jusqu'� pr�sent, {} objets ont �t� cr��s".format(cls.objets_crees))
	combien = classmethod(combien)