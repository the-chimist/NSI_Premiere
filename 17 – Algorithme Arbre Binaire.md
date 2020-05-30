# 17 – Algorithme Arbre Binaire

## 1-	Hauteur d'un arbre (maximum de profondeur pour les nœuds de l'arbre) 

```pseudocode
VARIABLE
T : arbre
x : noeud

DEBUT
HAUTEUR(arbre) :
  si arbre ≠ arbre_nul :
	noeud ← arbre.racine
	ssarbre_g = noeud.gauche
	ssarbre_d = nœud.droit
    renvoyer 1 + max(HAUTEUR(ssarbre_g), HAUTEUR(ssarbre_d))
  sinon :
    renvoyer 0
  fin si
FIN
```

## 2-	Taille d'un arbre (nombre de nœuds de l'arbre)

```pseudocode
VARIABLE
T : arbre
x : noeud

DEBUT
TAILLE(arbre) :
  si arbre ≠ arbre_vide :
    noeud ← arbre.racine
    renvoyer (1 + TAILLE(sousarbre.gauche) + TAILLE(sousarbre.droit))
  sinon :
    renvoyer 0
  fin si
FIN
```
## 3-	Parcours ordre infixe

```pseudocode
VARIABLE
T : arbre
x : noeud

DEBUT
PARCOURS-INFIXE(T) :
  si T ≠ NIL :
    x ← T.racine
    PARCOURS-INFIXE(x.gauche)
    affiche x.clé
    PARCOURS-INFIXE(x.droit)
  fin si
FIN
```
## 4-	Parcours ordre prefixe
```pseudocode
VARIABLE
T : arbre
x : noeud

DEBUT
PARCOURS-PREFIXE(T) :
  si T ≠ NIL :
    x ← T.racine
    affiche x.clé
    PARCOURS-PREFIXE(x.gauche)
    PARCOURS-PREFIXE(x.droit)
  fin si
FIN
```