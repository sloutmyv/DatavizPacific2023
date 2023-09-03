# DatavizPacific2023

## Langage de programation
Installer le langage [Python](https://www.python.org/downloads/)
## Editeur de texte
Installer l'éditeur [Visual studio](https://code.visualstudio.com/) 

Install pip package for vs studio extensions : 
```
pip install autopep8 
pip install pylint
pip install django-pylint
```

Install VS Code extensions : 
- Python/Pylance
- SQlite
- Django
- PowerShell
- Markdown Preview Enhancer

## Github
Pour chaque nouveau projet créer un répertoire directement depuis le [GitHub](https://github.com/)
### Les commandes à connaitre 
Pour cloner un répertoire existant depuis github : 
```
git clone <url>
```
Pour afficher la liste des fichiers/dossiers modifiés : 
```
git status
```
Pour ajouter des fichiers/dossiers non inclus : 
```
git add <fichier/dossier>
git add .
```
Pour créer un commit : 
```
git commit -m “description du commit”
```
Pour uploader les modifications sur github (sur la branche master) : 
```
git push origin master
```
Pour extraire mettre à jour le dossier depuis githup : 
```
git fetch origin
```
Pour fusionner depuis github : 
```
git pull
```
Pour lister les commits (taper q pour quitter) : 
```
git log 
```

### Le fichier ".gitignore"
Il est créé à la racine du projet pour indiquer les fichier à ne pas upload sur le répertoire github en ligne, à inclure (pour un projet Django):
```
# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
db.sqlite3-journal
media/
static/

# python-decouple
settings.ini

# Data
data/
```

## Environnement virtuel
Installer le package d’environnement virtuel : 
```
pip install virtualenv
```
Creer l’environnement virtuel : 
```
python -m venv <virtual-environnement-name>
```
Activer l’environnement virtuel : 
- Linux/Mac :
```
source <virtual-environnement-name>/bin/activate
```
- Windows :
```
Set-ExecutionPolicy Unrestricted -Scope Process (si fontionne pas)
env\Scripts\activate
```
Désactiver l’environnement virtuel :
``` 
deactivate
```

## Installer les Packages : 
```
pip install <some-dependance>
```
Lister les dépendances : 
```
pip freeze
```
Ajouter les dépendances à un fichier “requirement.txt”
```
pip freeze > requirement.txt
```
Installer les dépendances présentes dans un fichier “requirement.txt” : 
```
pip install -r requirement.txt
```

## Simple data analysis

Sets of data : 
- SPC :
    - TRADE FOOD
    - FOOD SECURITY
- OPENDATANC : 
    - FRUITS ET LEGUMES (2 jeux)
    - PRIX PRODUITS ALIMENTAIRE 2012 --> 2023 (11 jeux)

### TRADE FOOD

N'est considéré comme pays de provenance que le groupe Australie/Nouvelle zélande

**Données/graphique 1 : qté totale importée par pays sur la période 1995 --> 2018 (23 ans)**
Notes : 
- 80% de la qté importée par 3 des 18 pays étudiés

**Données/graphique 2 : qté totale importée par type sur la période 1995 --> 2018 (23 ans)**
Notes : 
- +50% de la qté importée concerne les céréales 
- Il faudrait voir si la tendance se vérifie par pays


