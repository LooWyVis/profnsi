# Profnsi

`profnsi` est une bibliothèque **LaTeX** pour simplifier la rédaction de documents liés à l'enseignement (cours, TD, évaluations, etc.) en **LaTeX**.

Elle utilise pour la partie mathématique la bibliothèque Latex `ProfSio` de monsieur Cédric Pierquet. [Lien vers le dépot git de cette dernière](https://forge.apps.education.fr/pierquetcedric/packages-latex/-/tree/5049854056dec7108171d884674e089e11fce047/profsio).


Le dépôt contient notamment :

* `sty/` : les fichiers de style (`profnsi.sty`, `ProfSio.sty`)
* `autocomplete/` : un fichier d’autocomplétion LaTeX (`profnsi.cwl`)
* `exemples/` : des exemples complets (`cours`, `exercices`, `evaluation`)
* `doc/` : documentation et script de génération (`doc.md`, `gen_doc.py`)
* `tests/` : fichiers de test (pour vérifier compilation et compatibilité)

---

## Setup

### Où mettre cette bibliothèque ?

Tu as plusieurs façons d’installer/utiliser la librairie.

#### Option A — Utilisation “locale” dans un projet (simple et portable)

Copie le fichier `sty/profnsi.sty` (et `sty/ProfSio.sty` si nécessaire) **dans le même dossier** que ton `.tex`.

Ensuite, dans ton document :

```tex
\usepackage{profnsi}
```

---

#### Option B — Installation dans ton arbre TeX (recommandé si tu l’utilises souvent)

Installe dans ton **arbre local texmf** (TEXMFHOME). Typiquement :

* Linux : `~/texmf/tex/latex/profnsi/`
* macOS : `~/Library/texmf/tex/latex/profnsi/` (souvent) ou `~/texmf/tex/latex/profnsi/`
* Windows (MiKTeX/TeX Live) : un répertoire `texmf` utilisateur (varie selon distribution)

Exemple (Linux) :

```bash
mkdir -p ~/texmf/tex/latex/profnsi
cp sty/profnsi.sty sty/ProfSio.sty ~/texmf/tex/latex/profnsi/
```

Puis rafraîchis l’index si besoin :

* TeX Live : `texhash ~/texmf` (souvent automatique)
* MiKTeX : “Refresh FNDB” via l’interface MiKTeX Console

Ensuite dans tes `.tex` :

```tex
\usepackage{profnsi}
```

---

### Mise en place de l'autocompletion

Le dépôt fournit un fichier `autocomplete/profnsi.cwl`.

#### TeXstudio (recommandé)

1. Ouvre **Options** → **Configurer TeXstudio**
2. Onglet **Completion**
3. Dans **User Completion Files** (ou équivalent selon version), ajoute :

   * `autocomplete/profnsi.cwl`

Redémarre TeXstudio si nécessaire.

---

#### Autres éditeurs

* Certains éditeurs LaTeX acceptent des fichiers `.cwl` (format proche de TeXstudio).
* Si ton éditeur ne supporte pas `.cwl`, tu peux quand même utiliser la lib sans autocomplétion : seule l’aide à la saisie est perdue.

---

## Utilisation

### Syntaxe

Dans ton préambule :

```tex
\usepackage[cours,eleve]{profnsi}
```
Ici, le document est de type cours, tu peux mettre `exercices` ou `ds`, cela change la présentation automatiquement.

Pour changer entre la version eleve et prof, remplace `eleve` par `prof`. Ainsi, les corrections (`\correction{...}`) seront cachèes en mode élève, et affichées en rouge en mode prof.

Pour setup le document :

```tex
\profnsisetup{
	niveau=Première,
	matiere=NSI,
	titre=Types construits,
	chapitre=4
}
```

Renseigne les bonnes informations.

Puis dans juste après le début du document :

```tex
\begin{document}
	\creerDoc
```

Puis utilise les commandes/environnements fournis par le style.

📌 La liste détaillée des commandes est dans la documentation :

* `doc/doc.md`

---

### Exemples de documents

Des exemples complets (source `.tex` + rendu `.pdf`) sont fournis dans `exemples/` :

* **Cours** : `exemples/cours/cours.tex` (rendu : `cours.pdf`)
* **TD / Exercices** : `exemples/exercices/td.tex` (rendu : `td.pdf`)
* **Évaluation / Sujet** : `exemples/evaluation/sujet.tex` (rendu : `sujet.pdf`)

Tu peux t’en servir comme “templates” de départ.

---

## Resources disponibles

### Documentation

* Documentation : `doc/doc.md`

### Fichiers de style

* `sty/profnsi.sty` : style principal
* `sty/ProfSio.sty` : dépendance/complément (selon usage)

### Autocomplétion

* `autocomplete/profnsi.cwl`

### Tests

Le dossier `tests/` contient des documents de test permettant de vérifier la compilation :

* `tests/cours/`
* `tests/ds/`

---

## Développement

Structure du dépôt :

```text
autocomplete/  -> fichiers d'autocomplétion
doc/           -> documentation + script de génération
exemples/      -> exemples prêts à compiler
sty/           -> fichiers .sty
tests/         -> documents de test
```
