# Disc Profiler

Application Flask pour le profilage DISC.

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python run.py
```

## Configuration

L'application utilise les variables d'environnement suivantes :
- `FLASK_DEBUG`: Mode debug (False en production)
- `PORT`: Port d'écoute (défaut: 8080)

# Application d'Évaluation du Profil DISC

Cette application web responsive permet d'identifier le profil DISC d'un utilisateur à partir d'un questionnaire de 10 questions. Elle détermine les deux dominantes parmi les quatre profils de couleur (Rouge, Jaune, Vert et Bleu).

## Optimisé pour Cursor

Ce projet est optimisé pour être utilisé avec [Cursor](https://cursor.com/), un éditeur de code basé sur VSCode avec des fonctionnalités d'IA intégrées.

### Fonctionnalités spécifiques pour Cursor

- **Configuration VSCode préconfigurée** : Le dossier `.vscode` contient des paramètres optimisés pour le développement Python et Flask
- **Commentaires enrichis** : Docstrings détaillées et commentaires explicatifs pour faciliter la compréhension par l'IA
- **Extensions recommandées** : Liste d'extensions utiles pour le développement Python
- **Configuration de débogage** : Paramètres préconfigurés pour déboguer l'application Flask

### Utilisation avec Cursor

1. **Ouvrir le projet dans Cursor**
   - Lancez Cursor
   - Sélectionnez "Open Folder" et naviguez vers le dossier du projet

2. **Explorer le code avec l'IA**
   - Utilisez la commande `/explain` pour obtenir des explications sur n'importe quelle partie du code
   - Essayez `/edit` pour suggérer des modifications ou améliorations

3. **Déboguer l'application**
   - Appuyez sur F5 ou utilisez le menu de débogage pour lancer l'application avec le débogueur
   - Les points d'arrêt peuvent être définis en cliquant sur la marge gauche

4. **Utiliser les extensions recommandées**
   - Cursor vous proposera d'installer les extensions recommandées dans le fichier `.vscode/extensions.json`

## Installation standard

1. **Prérequis**
   - Python 3.8 ou supérieur
   - pip (gestionnaire de paquets Python)

2. **Étapes d'installation**
   - Décompressez l'archive `disc_profiler.zip` dans un dossier de votre choix
   - Ouvrez un terminal et naviguez vers le dossier extrait
   - Installez les dépendances requises :
     ```
     pip install -r requirements.txt
     ```

## Lancement de l'application

1. **Démarrer le serveur**
   - Dans le terminal, toujours dans le dossier de l'application, exécutez :
     ```
     python run.py
     ```
   - Le serveur démarrera et sera accessible à l'adresse : http://127.0.0.1:5000

2. **Accéder à l'application**
   - Ouvrez votre navigateur web
   - Accédez à l'URL : http://127.0.0.1:5000
   - L'application se chargera et vous pourrez commencer à l'utiliser

## Utilisation de l'application

1. **Page d'accueil**
   - Vous trouverez une brève introduction au modèle DISC
   - Cliquez sur le bouton "Commencer le questionnaire" pour débuter l'évaluation

2. **Questionnaire**
   - Répondez aux 10 questions en sélectionnant l'option qui vous correspond le mieux
   - Chaque question propose 4 réponses possibles, correspondant aux 4 profils DISC
   - Soyez spontané dans vos réponses pour obtenir un résultat plus précis
   - Une fois toutes les questions répondues, cliquez sur "Voir mes résultats"

3. **Page de résultats**
   - Vous découvrirez vos deux profils dominants parmi les quatre couleurs :
     - Rouge (D - Dominant) : déterminé, direct, orienté résultats
     - Jaune (I - Influent) : sociable, enthousiaste, expressif
     - Vert (S - Stable) : fiable, empathique, patient
     - Bleu (C - Consciencieux) : précis, analytique, méticuleux
   - Pour chaque profil dominant, vous obtiendrez une description détaillée
   - Vous pourrez également voir la répartition de vos réponses entre les quatre profils

## Structure du projet

- `app/` : Contient le code principal de l'application
  - `main/` : Contient les routes, formulaires et la logique DISC
  - `static/` : Fichiers CSS, JavaScript et images
  - `templates/` : Fichiers HTML pour l'interface utilisateur
- `questions/` : Documentation sur les questions du questionnaire
- `.vscode/` : Configuration pour VSCode/Cursor
- `config.py` : Configuration de l'application
- `run.py` : Point d'entrée pour démarrer l'application

## Personnalisation

Si vous souhaitez modifier l'application :

1. **Modification des questions**
   - Les questions sont définies dans `app/main/forms.py`
   - La logique d'évaluation est dans `app/main/disc_logic.py`

2. **Personnalisation de l'interface**
   - Modifiez les fichiers CSS dans `app/static/css/`
   - Adaptez les templates HTML dans `app/templates/`
