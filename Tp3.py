from abc import ABC, abstractmethod

class Humain(ABC):
    def __init__(self, nom, boisson_favorite="l'eau", vie = 1):
        self.__nom = nom
        self.__boisson_favorite = boisson_favorite
        self.__vie = vie

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def boisson_favorite(self):
        return self.__boisson_favorite

    @boisson_favorite.setter
    def boisson_favorite(self, value):
        self.__boisson_favorite = value

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, value):
        self.__vie = value

    @abstractmethod
    def manger(self):
        pass

    @abstractmethod
    def mort(self):
        pass

    def quelEstTonNom(self):
        print(self.nom)

    def quelTaBoissonFavorite(self):
        print(self.__boisson_favorite)

    def presentation(self):
        print(f"Bonjour, je m'appelle {self.nom} et ma boisson préférée est {self.boisson_favorite}.")

    def boire(self):
        print(f"Ah ! Un bon verre de {self.boisson_favorite} ! GLOUPS !")

# ________________________________________Partie 2___________________________________________________________________________
class Dame(Humain):
    def __init__(self, nom, boisson_favorite, couleur_robe, vie=1, etat=True):
        super().__init__(nom, boisson_favorite, vie)
        self.__couleur_robe = couleur_robe
        self.__etat = etat

    @property
    def couleur_robe(self):
        return self.__couleur_robe

    @couleur_robe.setter
    def couleur_robe(self, value):
        self.__couleur_robe = value

    @property
    def etat(self):
        return self.__etat

    @etat.setter
    def etat(self, value):
        self.__etat = value

    def presentation(self):
        print(f"Je m'appelle {self.nom} et j'adore ma robe {self.couleur_robe}")

    def SeFaitKidnapper(self):
        reponse = input("Est ce que la dame se fait kidnapper ? ")
        if reponse.lower() == "oui":
            print("Ahhhhhhhh")

    def SeFaitLiberer(self, Cowboy):
        if self.__etat == True:
            print(f"Merci de m'avoir sauvé {Cowboy.nom}")

    def quelEstTonNom(self):
        print(f"Miss {self.nom}")

    def verre(self, Barman):
        question = input("Voulez vous un verre ?")
        if question.lower() == "oui":
            Barman.servir_dame(self)
            Humain.boire(self)

    def mort(self):
        if self.vie == 0:
            print(f"{self.nom} meurt de faim")

    def manger(self):
        didi = input("Voulez vous manger ?")
        if didi.lower() == "oui":
            self.vie += 1
            print(f"{self.nom} mange un plat gastronomique, elle savoure son plat !")
        else :
            self.vie -= 1
            self.mort()
class Brigand(Humain):

    def __init__(self, nom, boisson_favorite, vie=1, look="méchant", prime=100, prison=True, nb_dame_enleve=0):
        super().__init__(nom, boisson_favorite, vie)
        self.__look = look
        self.__prime = prime
        self.__prison = prison
        self.__nb_dame_enleve = nb_dame_enleve

    @property
    def look(self):
        return self.__look

    @look.setter
    def look(self, value):
        self.__look = value

    @property
    def prime(self):
        return self.__prime

    @prime.setter
    def prime(self, value):
        self.__prime = value

    @property
    def prison(self):
        return self.__prison

    @prison.setter
    def prison(self, value):
        self.__prison = value

    def presentation(self):
        print(f"Bonjour, je suis {self.nom} et j'aime {self.boisson_favorite}.")
        print(f"J'ais l'air {self.look} et j'ais déjà kidnappé {self.__nb_dame_enleve} Dame !")
        print(f"Ma tête est mise à prix à {self.prime}$ !")

    def augmenter_nb_dame_enleve(self):
        self.__nb_dame_enleve += 1

    def baisser_nb_dame_enleve(self):
        self.__nb_dame_enleve -= 1
    def kidnapping(self, Dame):
        kidnappage = input("Voulez-vous kidnapper une dame ? ")
        if kidnappage.lower() == "oui" and Dame.etat:
            print(f"Ah ah ! {Dame.nom}, tu es miennes désormais !")
            Dame.etat = False
            self.augmenter_nb_dame_enleve()
            self.__prime += 100

    def quelEstTonNom(self):
        print(f"{self.nom} {self.look}")

    def verre(self, Barman):
        question = input("Voulez vous un verre ?")
        if question.lower() == "oui":
            Barman.servir_brigand(self)
            Humain.boire(self)

    def mort(self):
        if self.vie == 0:
            print(f"{self.nom} meurt de faim")

    def manger(self):
        didi = input("Voulez vous manger ?")
        if didi.lower() == "oui":
            self.vie += 1
            print(f"{self.nom} mange sauvagement de la viande cru !")
        else :
            self.vie -= 1
            self.mort()

class Cowboy(Humain):
    def __init__(self, nom, boisson_favorite, vie=1, popularite=0, caracteristique="vaillant"):
        super().__init__(nom, boisson_favorite, vie)
        self.__popularite = popularite
        self.__caracteristique = caracteristique

    @property
    def popularite(self):
        return self.__popularite

    @popularite.setter
    def popularite(self, value):
        self._popularite = value

    @property
    def caracteristique(self):
        return self.__caracteristique

    @caracteristique.setter
    def caracteristique(self, value):
        self.__caracteristique = value

    def presentation(self):
        print(f"Moi c'est {self.nom} les gens font que dire de moi que je suis {self.caracteristique}")

    def sauver(self, Dame, Brigand):
        sauvetage = input("Voulez-vous sauver une dame ? ")
        if sauvetage.lower() == "oui" and not Dame.etat:
            print(f"Je viens te sauver {Dame.nom} ! ")
            self.__popularite += 1
            Brigand.baisser_nb_dame_enleve()
            return True
        return False

    def quelEstTonNom(self):
        print(f"{self.nom}")

    def verre(self, Barman):
        question = input("Voulez vous un verre ?")
        if question.lower() == "oui":
            Barman.servir_cowboy(self)
            Humain.boire(self)

    def mort(self):
        if self.vie == 0:
            print(f"{self.nom} meurt de faim")

    def manger(self):
        didi = input("Voulez vous manger ?")
        if didi.lower() == "oui":
            self.vie += 1
            print(f"{self.nom} mange un plat steak frite, il avait vraiment besoin de manger !")
        else :
            self.vie -= 1
            self.mort()

class Barman(Humain):
    def __init__(self, nom, nom_bar, vie=1, boisson_favorite="Vin", fin_phrase="Coco"):
        super().__init__(nom, boisson_favorite, vie)
        self.__fin_phrase = fin_phrase
        self.__nom_bar = nom_bar

    @property
    def fin_phrase(self):
        return self.__fin_phrase

    @fin_phrase.setter
    def fin_phrase(self, value):
        self.__fin_phrase = value

    @property
    def nom_bar(self):
        return self.__nom_bar

    @nom_bar.setter
    def nom_bar(self, value):
        self.__nom_bar = value

    def presentation(self):
        print(f"Je m'appelle {self.nom} et mon bar s'appelle {self.nom_bar} {self.fin_phrase}")

    def servir_brigand(self, Brigand):
        print(f"Voilà du {Brigand.boisson_favorite} sale bandit {self.fin_phrase}!")

    def servir_dame(self, Dame):
        print(f"Voici votre {Dame.boisson_favorite} très chers {self.fin_phrase}!")

    def servir_cowboy(self, Cowboy):
        print(f"Voici votre {Cowboy.boisson_favorite} et merci d'assurer la sécurité au sein du {self.nom} {self.fin_phrase}")

    def servir_sherif(self, Sherif):
        print(f"Voici votre {Sherif.boisson_favorite} {Sherif.nom}")

    def mort(self):
        if self.vie == 0:
            print(f"{self.nom} meurt de faim")

    def manger(self):
        didi = input("Voulez vous manger ?")
        if didi.lower() == "oui":
            self.vie += 1
            print(f"{self.nom} mange dans la reserve de {self.nom_bar}, son verre de {self.boisson_favorite} lui manque !")
        else :
            self.vie -= 1
            self.mort()

class Sherif(Cowboy):
    def __init__(self,boisson_favorite, vie=1, nom="Sherif", brigand_capture=0):
        super().__init__(nom, boisson_favorite, vie)
        self.__brigand_capture = brigand_capture

    @property
    def brigand_capture(self):
        return self.__brigand_capture

    @brigand_capture.setter
    def brigand_capture(self, value):
        self.__brigand_capture = value

    def presentation(self):
        print(f"Je suis le {self.nom}")

    def arrestation(self, Brigand):
        if Brigand.prison:
            dede = input(f"Voulez-vous arrêter {Brigand.nom} ?")
            if dede.lower() == "oui":
                print(f"Au nom de la loi, je vous arrête {Brigand.nom} !")
                Brigand.prison = False

    def recherche(self, Brigand):
        didi = input("Voulez vous recherchez un Brigand ?")
        if didi.lower() == "oui" and Brigand.prison:
            print(f"OYEZ OYEZ BRAVE GENS!! {Brigand.prime}$ à qui arrêtera {Brigand.nom} le brigand mort ou vif !")
            self.arrestation(brigant1)
    def verre(self, Barman):
        question = input("Voulez vous un verre ?")
        if question.lower() == "oui":
            Barman.servir_sherif(self)
            Humain.boire(self)

    def mort(self):
        if self.vie == 0:
            print(f"{self.nom} meurt de faim")

    def manger(self):
        didi = input("Voulez vous manger ?")
        if didi.lower() == "oui":
            self.vie += 1
            print(f"{self.nom} mange sans s'arrêter !")
        else :
            self.vie -= 1
            self.mort()

brigant1 = Brigand("Yannis", "Coca")
dame1 = Dame("Rayan", "Coca", couleur_robe="Rouge")
cowboy1 = Cowboy("Antoine", "Ice tea", caracteristique="hypocrite")
barman1 = Barman("Ricard", nom_bar="Chez Ricard")
sherif1 = Sherif(boisson_favorite="Bière")
brigant1.quelEstTonNom()
brigant1.presentation()
brigant1.verre(barman1)
brigant1.kidnapping(dame1)
brigant1.manger()
dame1.quelEstTonNom()
dame1.presentation()
dame1.verre(barman1)
dame1.SeFaitKidnapper()
cowboy1.presentation()
cowboy1.verre(barman1)
if cowboy1.sauver(dame1, brigant1):
    dame1.SeFaitLiberer(cowboy1)
cowboy1.manger()
barman1.presentation()
barman1.manger()
sherif1.presentation()
sherif1.verre(barman1)
sherif1.recherche(brigant1)
sherif1.manger()