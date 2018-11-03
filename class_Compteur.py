# -*-coding:Latin-1 -*
class Compteur:
	"""Cette classe possède un attribut de classe qui s'incrémente à chaque
	fois que l'on crée un objet de ce type"""
	objets_crees = 0
	def __init__(self):
		"""À chaque fois qu'on crée un objet on incrémente le compteur"""
		Compteur.objets_crees += 1
	def combien(cls):
		"""Méthode de classe affichant combien d'objets ont été créés"""
		print("Jusqu'à  présent, {} objets ont été créés".format(cls.objets_crees))
	combien = classmethod(combien)