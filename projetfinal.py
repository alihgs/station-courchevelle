######################## IMPORT ########################
import heapq
from tkinter import *
import datetime
import random as rd
###################### Graphe ######################
graphe = {
    'CHANROSSA' : [('CREUX', 25, 'Prenez le téléski Chanrossa'), ('x1', 10, 'Prenez la télécabine Roc Merlet')],
    'x1' : [('CHANROSSA', 10, 'Prenez la télécabine Roc Merlet'), ('BEL-AIR', 15, 'Descendre la piste bleue des Pyramide')],
    'BEL-AIR' : [('x1', 15, 'Descendre la piste bleue des Pyramide'), ('SIGNAL', 12, 'Descendre la piste bleue de la Grande Bosses'),
                 ('BOSSES', 12, 'Descendre la piste verte de la Praline'), ('x2', 5, 'Descendre la piste verte de la Praline')],
    'x2' : [('BEL-AIR', 5, 'Descendre la piste verte de la Praline'), ('BOSSES', 5, 'Descendre la piste verte de la Praline'),
            ('PRAMERUEL', 7, 'Descendre la piste bleue des Gravelles')],
    'SIGNAL' : [('BEL-AIR', 12, 'Descendre la piste bleue de la Grande Bosses'), ('BOSSES', 10, 'Prenez le téléphérique à Signal')],
    'BOSSES' : [('BEL-AIR', 12, 'Descendre la piste verte de la Praline'), ('x2', 5, 'Descendre la piste verte de la Praline'),
                ('SIGNAL', 10, 'Prenez le téléphérique à Signal')],
    'CREUX' : [('CHANROSSA', 25, 'Prenez le téléski Chanrossa'), ('VIZELLE', 25, 'Prenez le téléphérique à Marmottes'),
               ('PRAMERUEL', 14, 'Descendre la piste bleue des Creux')],
    'PRAMERUEL' : [('x2', 7, 'Descendre la piste bleue des gravelles'), ('CREUX', 14, 'Descendre la piste bleue des Creux')],
    'VIZELLE' : [('CREUX', 25, 'Prenez le téléphérique à Marmottes'), ('VERDONS', 13, 'Prenez le télésiège à Vizelle')],
    'VERDONS' : [('VIZELLE', 13, 'Prenez le télésiège à Vizelle'), ('PRALONG', 12, 'Descendre la piste bleue de Biollay')],
    'PRALONG' : [('VERDONS', 12, 'Descendre la piste bleue de Biollay'),('LAC', 13, 'Descendre la piste verte lac')],
    'LAC' : [('PRALONG', 13, 'Descendre la piste verte ???'), ('CHENUS', 20, 'Prenez le télésiège à Coqs')],
    'CHENUS' : [('LAC', 20, 'Prenez le télésiège à Coqs'), ('x3', 13, 'Prenez le télésiège à Col de la loze'),
                ('LOZE', 7, 'Descendre la piste bleue des Crêtes')],
    'x3' : [('CHENUS', 13, 'Prenez le télésiège à Col de la loze'), ('PRAZ JUGET', 16, 'Prenez le télésiège à Dou des lanches')],
    'PRAZ JUGET' : [('x3', 16, 'Prenez le télésiège à Dou des lanches')],
    'LOZE' : [('CHENUS', 7, 'Descendre la piste bleue des Crêtes')]
    } 

###################### CONSTANTES #######################
options = [i for i in graphe if i != "x1" and i != "x2" and i != "x3"]
experience = ['Débutant', 'Expériementé']
###################### FONCTIONS #######################
def dijkstra(s, graphe):
    """
    Effectue l'algorithme de Dijkstra pour trouver les distances les plus courtes 
    et les chemins optimaux à partir d'un nœud source dans un graphe pondéré.
    Args:
        s (sommet): Le nœud source à partir duquel les distances sont calculées.
        graphe (dict): Le graphe pondéré représenté sous forme de dictionnaire, 
                       avec les sommets comme clés et les voisins avec les distances et les arcs comme valeurs.
    Returns:
        tuple: Un tuple contenant deux dictionnaires. 
        Le premier dictionnaire contient les distances minimales de chaque sommet au nœud source. 
        Le deuxième dictionnaire contient les chemins optimaux de chaque sommet au nœud source.
    """
    # Initialiser une liste vide pour suivre les nœuds visités
    visites = []
    # Initialiser un dictionnaire des distances avec tous les nœuds du graphe, en fixant les distances initiales à l'infini
    distances = {sommet: float('inf') for sommet in graphe.keys()}
    # Définir la distance du nœud source à 0
    distances[s] = 0
    # Créer une file de priorité avec les distances et les sommets correspondants pour tous les sommets du graphe
    file = [(distances[sommet], sommet) for sommet in graphe]
    # Organiser la file de priorité sous forme de tas
    heapq.heapify(file)
    # Initialiser un dictionnaire des chemins avec tous les sommets du graphe, en fixant les chemins initiaux à une liste vide
    chemins = {sommet: [] for sommet in graphe.keys()}
    # Définir le chemin du nœud source comme étant [s]
    chemins[s] = [s]
    # Tant que la file de priorité n'est pas vide
    while file != []:
        # Extraire le sommet avec la distance minimale de la file de priorité
        distance_min, sommet_min = heapq.heappop(file)
        # Si le sommet extrait n'a pas encore été visité
        if sommet_min not in visites: 
            # Ajouter le sommet à la liste des sommets visités
            visites.append(sommet_min)
        # Pour chaque voisin du sommet extrait, ainsi que la distance et l'arc correspondants
        for voisin, distance_voisin, arc in graphe[sommet_min]:
            # Si la distance actuelle + distance_voisin est inférieure à la distance enregistrée du voisin
            if distance_min + distance_voisin < distances[voisin]:
                # Mettre à jour la distance du voisin
                distances[voisin] = distance_min + distance_voisin
                # Mettre à jour le chemin du voisin en ajoutant le voisin au chemin du sommet extrait
                chemins[voisin] = chemins[sommet_min] + [voisin]
                # Ajouter le voisin avec sa nouvelle distance à la file de priorité
                heapq.heappush(file, (distances[voisin], voisin))
            # Si le voisin n'a pas encore été visité
            if voisin not in visites: 
                # Ajouter le voisin à la liste des sommets visités
                visites.append(voisin)
    # Retourner les distances et les chemins calculés
    return distances, chemins


def calcul_itineraire(itineraire, graphe, niveau):
    """
    Calcule l'itinéraire complet avec les temps de parcours et les instructions pour chaque arc.
    Args:
        itineraire (list): Liste des sommets constituant l'itinéraire.
        graphe (dict): Le graphe contenant les informations sur les arcs et les distances.
        niveau (str): Le niveau de ski (par exemple: "Débutant", "Expérimenté").
    Returns:
        list: Liste des arcs parcourus avec les instructions détaillées.
    """
    # Initialiser le temps total à 0
    temps = 0
    # Initialiser une liste vide pour stocker les arcs parcourus
    l_arc = []
    # Parcourir les sommets de l'itinéraire
    for i in range(len(itineraire)-1):
        # Récupérer le sommet actuel et le sommet suivant
        sommet_actuel = itineraire[i] 
        sommet_suivant = itineraire[i+1]
        # Calculer la distance entre le sommet actuel et le sommet suivant en utilisant la fonction dijkstra
        distance = dijkstra(sommet_actuel, graphe)[0][sommet_suivant]
        # Parcourir les voisins du sommet actuel
        for voisin, distance_voisin, arc in graphe[sommet_actuel]:
            # Générer un temps d'attente aléatoire entre 0 et 20 minutes
            temps_attente = rd.randint(0, 20)
            # Vérifier si le voisin correspond au sommet suivant et s'il s'agit d'un téléski
            if voisin == sommet_suivant and 'téléski' in arc:
                vitesse = 5
                # Calculer le temps de parcours en utilisant la distance et la vitesse
                temps += distance/vitesse
                # Vérifier s'il y a un temps d'attente
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            # Effectuer des vérifications similaires pour les autres types d'arc
            elif voisin == sommet_suivant and 'télésiège' in arc:
                vitesse = 7
                temps += distance/vitesse
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and 'télécabine' in arc:
                vitesse = 9
                temps += distance/vitesse
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and 'téléphérique' in arc:
                vitesse = 12
                temps += distance/vitesse
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and 'verte' in arc:
                vitesse = 60
                temps += distance/vitesse
                if niveau == 'Expérimenté':
                    temps //= 1.2
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and 'bleue' in arc:
                vitesse = 55
                temps += distance/vitesse
                if niveau == 'Expérimenté':
                    temps //= 2
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and'rouge' in arc:
                vitesse = 50
                temps += distance/vitesse
                if niveau == 'Expérimenté':
                    temps //= 3
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
            elif voisin == sommet_suivant and'noire' in arc:
                vitesse = 40
                temps += distance/vitesse
                if niveau == 'Expérimenté':
                    temps //= 4 
                if temps_attente > 0 :
                    temps += temps_attente
                    l_arc.append(f"- Attendre {temps_attente} minutes puis {arc}")
                else : l_arc.append(f"minutes puis {arc}")
                break
    l_arc.append(f"- Vous arrivez à {itineraire[-1]}\nLe trajet devrait vous prendre environs {datetime.timedelta(minutes=int(temps))}")
    return l_arc

def valider_itineraire():
    """
    Valide l'itinéraire entre le départ et l'arrivée, et affiche les instructions dans la zone de texte.
    """
    # Effacer le contenu précédent de la zone de texte d'instructions
    instruction_entry.delete('1.0', 'end')
    # Récupérer les valeurs sélectionnées pour le départ, l'arrivée et le niveau
    depart = depart_var.get()
    arrivee = arrivee_var.get()
    # Calculer l'itinéraire optimal en utilisant l'algorithme de Dijkstra
    itineraire = dijkstra(depart, graphe)[1][arrivee]
    # Calculer les instructions détaillées pour l'itinéraire avec le niveau spécifié
    l_it = calcul_itineraire(itineraire, graphe, niveau.get())
    # Afficher les instructions dans la zone de texte
    for it in l_it:
        instruction_entry.insert(END, it + "\n")


def bouton_clique(button_text):
    """
    Gère l'événement lorsqu'un bouton est cliqué et met à jour la variable correspondante en fonction du choix.
    Args:
        button_text (str): Le texte du bouton qui a été cliqué.
    """
    # Vérifier le choix actuel
    if choix.get() == "depart":
        # Mettre à jour la variable de départ avec le texte du bouton cliqué
        depart_var.set(button_text)
    elif choix.get() == "arrivee":
        # Mettre à jour la variable d'arrivée avec le texte du bouton cliqué
        arrivee_var.set(button_text)

        
######################## INTEFACE ########################
window = Tk()
window.attributes('-fullscreen', True)

# Charger l'image et afficher l'image
plan = PhotoImage(file="ski.png")
label = Label(window, image=plan)   
label.pack()

# Stock le choix de l'utilisateur pour le départ
depart_var = StringVar(window)
arrivee_var = StringVar(window)
niveau = StringVar(window)
choix = StringVar(window)
depart_var.set(options[0])
arrivee_var.set(options[0])
niveau.set(experience[0])
choix.set("depart")
# Ajouter le texte "Départ :"
depart_label = Label(window, text="Départ :")
arrivee_label = Label(window, text="Arrivée :")
niveau_label = Label(window, text="Niveau :")
depart_label.place(x=20, y=20)
arrivee_label.place(x=20, y=60)
niveau_label.place(x=20, y=90)

# Ajouter les zones de texte pour le départ, l'arrivée et le niveau
depart_zone = Entry(window, textvariable=depart_var, width=20)
arrivee_zone = Entry(window, textvariable=arrivee_var, width=20)
niveau_menu = OptionMenu(window, niveau, *experience)
depart_choix = Radiobutton(window, text="Modifier le départ", variable=choix, value="depart")
arrivee_choix = Radiobutton(window, text="Modifier l'arrivée", variable=choix, value="arrivee")
depart_zone.place(x=80, y=20)
arrivee_zone.place(x=80, y=60)
niveau_menu.place(x=80, y=90)
depart_choix.place(x=280, y=20)
arrivee_choix.place(x=280, y=60)

# Ajouter le bouton "Valider"
valider_button = Button(window, text="Valider", command=valider_itineraire)
valider_button.place(x=20, y=120)

# Ajouter une zone de texte pour afficher les instructions
instruction_entry = Text(window, width=80, height=40)
instruction_entry.place(x=window.winfo_screenheight(), y=window.winfo_screenheight()-200)

# Création des boutons 
chanrossa_btn = Button(window, text="CHANROSSA", command=lambda: bouton_clique("CHANROSSA"))
belair_btn = Button(window, text="BEL-AIR", command=lambda: bouton_clique("BEL-AIR"))
signal_btn = Button(window, text="SIGNAL", command=lambda: bouton_clique("SIGNAL"))
bosses_btn = Button(window, text="BOSSES", command=lambda: bouton_clique("BOSSES"))
creux_btn = Button(window, text="CREUX", command=lambda: bouton_clique("CREUX"))
prameruel_btn = Button(window, text="PRAMERUEL", command=lambda: bouton_clique("PRAMERUEL"))
vizelle_btn = Button(window, text="VIZELLE", command=lambda: bouton_clique("VIZELLE"))
pralong_btn = Button(window, text="PRALONG", command=lambda: bouton_clique("PRALONG"))
verdons_btn = Button(window, text="VERDONS", command=lambda: bouton_clique("VERDONS"))
lac_btn = Button(window, text="LAC", command=lambda: bouton_clique("LAC"))
chenus_btn = Button(window, text="CHENUS", command=lambda: bouton_clique("CHENUS"))
prazjuget_btn = Button(window, text="PRAZ JUGET", command=lambda: bouton_clique("PRAZ JUGET"))
loze_btn = Button(window, text="LOZE", command=lambda: bouton_clique("LOZE"))

# Placement des boutons 
chanrossa_btn.place(x=60, y=183)
belair_btn.place(x=204, y=408)
signal_btn.place(x=11, y=340)
bosses_btn.place(x=337, y=481)
creux_btn.place(x=322, y=292)
prameruel_btn.place(x=368, y=433)
vizelle_btn.place(x=634, y=166)
pralong_btn.place(x=531, y=475)
verdons_btn.place(x=643, y=342)
lac_btn.place(x=691, y=490)
chenus_btn.place(x=839, y=360)
prazjuget_btn.place(x=1055, y=467)
loze_btn.place(x=870, y=404)
window.mainloop()