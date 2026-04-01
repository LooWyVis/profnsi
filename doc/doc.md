#Profnsi
Documentation des commandes — générée le 2026-04-01 16:53

# Présentation

**Un package pour les enseignants de NSI, pour afficher des structures de données facilement, des opérations binaires, du code, ...**

**Inclus un système d'auto template de document, avec gestion automatique de version éléves/prof**

```tex
\documentclass[11pt]{exam}

\usepackage[a4paper,margin={.1\paperheight,.1\paperwidth},marginratio=1:1]{geometry}

\usepackage[french]{babel}

\usepackage[T1]{fontenc}

% Choix des options et des infos d’en-tête
\usepackage[cours,eleve]{profnsi}
\profnsisetup{
niveau=Première,
matiere=NSI,
titre=Représentation des données,
chapitre=3
}

\begin{document}
\creerDoc
ecrire votre document
\end{document}
```

# Listes des commandes

## \activerSommaireParties
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=s`  
**Description** :

Afficher le sommaire dans le document :
- non étoilée : active + imprime le sommaire + saute de page
- étoilée : active seulement (pas d'impression)

**Exemple** :

```tex
\activerSommaireParties
```

## \addition
**Type** : `newcommand`  
**Arguments** : `num=2`  
**Description** :

Pose une addition sous différentes bases

**Exemple** :

```tex
\addition{8475}{6520}, \addition[Base=bin]{1111}{111}, \addition[Base=hex,AffEgal=false,Offset=0pt]{ABCD}{FE}, \addition[Base=bin,AffRetenues=false]{1111}{111}
```

## \affichermatrice
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Représenter une matrice d'adjacence (brute : pas en écriture mathématique)

**Exemple** :

```tex
\affichermatrice{0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0}
```

## \application
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=o m g`  
**Description** :

Commande \application Creer une boite d'application

**Exemple** :

```tex
\application{Contenu}{<nb lignes>} - \application[Titre perso]{Contenu}{<nb lignes>}
```

## \arbre
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Affiche un arbre

**Exemple** :

```tex
\arbre{[A [B] [C [E] [F]] [D]]}, \arbre{[/ [bin] [users [louis] [jean]] [dev]]}
```

## \code
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m m`  
**Description** :

Code inline : \code{<langage>}{<code>}

**Exemple** :

```tex
\code{SQL}{SELECT * FROM livres;}
```

## \complexite
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Mets en forme un compléxité

**Exemple** :

```tex
\complexite{111}
```

## \correction
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Correction affichée (en rouge) en mode prof, ignorée en mode élève

**Exemple** :

```tex
\correction{Ma correction}
```

## \courbecomplexite
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=O{} m`  
**Description** :

Affiche une courbe schématique de complexité dans un repère orthonormé

**Exemple** :

```tex
\courbecomplexite{n2}, \courbecomplexite[couleur=red,titre=Tri fusion]{nlogn}
```

## \creerDoc
**Type** : `newcommand`  
**Arguments** : _aucun_  
**Description** :

Creer le template du document

**Exemple** :

```tex
\creerDoc
```

## \division
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Pose une suite de divisions (conversion) sous différentes bases (conversion dec to bin par défaut)

**Exemple** :

```tex
\division{128}, \division[3]{98}
```

## \dossier
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Mets en forme un chemin de dossier

**Exemple** :

```tex
\dossier{Documents/exercices}
```

## \doublebar
**Type** : `providecommand`  
**Arguments** : _aucun_  
**Description** :

\doublebar au cas où elle n'existe pas

**Exemple** :

```tex
\doublebar
```

## \exercice
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=s o m`  
**Description** :

Creer un exercice

**Exemple** :

```tex
\exercice{Binaire vers hexadécimal}, \exercice*{Exo non numéroté}
```

## \fichier
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Mets en forme un nom de fichier

**Exemple** :

```tex
\fichier{Documents/exercices}
```

## \file
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m`  
**Description** :

Représenter une file

**Exemple** :

```tex
\file{[A, V, P, Z, H]}
```

## \img
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Affiche une image (centrée), option pour rétrécir

**Exemple** :

```tex
\img{img/image.jpg}, \img[0.2]{img/image.jpg}
```

## \lignes
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Commande : \lignes{<nombre>}, fais des lignes pour ecrire

**Exemple** :

```tex
\lignes{4}
```

## \listechainee
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Représenter une liste chainée

**Exemple** :

```tex
\listechainee{2, 4, 3, 9}
```

## \matrice
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Représenter une matrice d'adjacence

**Exemple** :

```tex
\matrice{0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0}
```

## \matriceadj
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Représenter une matrice d'adjacence avec son nom

**Exemple** :

```tex
\matriceadj[G]{0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0}
```

## \multiplication
**Type** : `newcommand`  
**Arguments** : `num=2`  
**Description** :

Pose une multiplication sous différentes bases

**Exemple** :

```tex
\multiplication[Base=hex]{ABCD}{FAFD}, \multiplication[Base=bin]{11}{11}
```

## \partie
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=s o m`  
**Description** :

Début d'une partie

**Exemple** :

```tex
\partie{Le système binaire}
```

## \pile
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m`  
**Description** :

Représenter une pile

**Exemple** :

```tex
\pile{[2, 4, 3, 9, 5]}
```

## \pointilles
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=O{\linewidth}`  
**Description** :

Affiche des pointillés pour une certaine largeur

**Exemple** :

```tex
\pointilles[6cm]
```

## \pointillestrou
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m O{\linewidth}`  
**Description** :

En version prof : affiche le texte ; en version élève : affiche des pointillés

**Exemple** :

```tex
\pointillestrou{Réponse}[6cm]
```

## \profnsisetup
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Initialiser les paramètres du document

**Exemple** :

```tex
\profnsisetup{niveau=Première,matiere=NSI,titre=Représentation des données,chapitre=3}
```

## \qcmchoice
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m`  
**Description** :

Choix de réponse dans un QCM

**Exemple** :

```tex
\qcmchoice{$x^3$}
```

## \qcmcorrectchoice
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m`  
**Description** :

Choix de réponse correct, mis en rouge en mode prof

**Exemple** :

```tex
\qcmcorrectchoice{$2x$}
```

## \qcmfreequestion
**Type** : `NewDocumentEnvironment`  
**Arguments** : `spec=m O{} O{}`  
**Description** :

Question ouverte de QCM (avec correction et nombre de lignes)

**Exemple** :

```tex
\begin{qcmfreequestion}{Résoudre $x^2-5x+6=0$}[Les racines sont $x=2$ et $x=3$.][5]
```

## \qcmsolution
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=m`  
**Description** :

Explications de réponse de QCM (affichées seulement en version prof)

**Exemple** :

```tex
\qcmsolution{On a $(x^2)'=2x$.}
```

## \remarque
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=o m`  
**Description** :

Creer une boite de remarque

**Exemple** :

```tex
\remarque{Contenu}
```

## \sortie
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Simule une sortie python

**Exemple** :

```tex
\sortie{111}
```

## \souspartie
**Type** : `NewDocumentCommand`  
**Arguments** : `spec=s o m`  
**Description** :

Sous partie

**Exemple** :

```tex
\souspartie{Conversions}
```

## \soustraction
**Type** : `newcommand`  
**Arguments** : `num=2`  
**Description** :

Pose une soustraction sous différentes bases

**Exemple** :

```tex
\soustraction[Base=bin]{10000}{111}
```

## \tableau
**Type** : `newcommand`  
**Arguments** : `num=2`  
**Description** :

Affiche un tableau

**Exemple** :

```tex
\tableau{Décimal|Binaire}{4|100 ; 5|101 ; 6|110}, \tableau[.5\linewidth]{Tour|i|compteur}{0|0|0 ;1|1|1 ;10|2|2}
```

## \touche
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Mets en forme une touche de clavier

**Exemple** :

```tex
\touche{Echap}
```

## \trou
**Type** : `newcommand`  
**Arguments** : `num=2`  
**Description** :

En version prof : texte normal, en version élève : pointillés occupant l'espace texte

**Exemple** :

```tex
\trou{Réponse attendue}{4}
```

## \variable
**Type** : `newcommand`  
**Arguments** : `num=1`  
**Description** :

Affiche une variable

**Exemple** :

```tex
\variable{temp}
```
