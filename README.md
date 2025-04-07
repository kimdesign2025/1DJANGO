# Présentation de Produits

Bienvenue dans le projet **Présentation de Produits**, une application web construite avec Django qui permet aux utilisateurs de visualiser et de créer des produits dans une boutique en ligne. 

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licences](#licences)
- [Auteurs](#auteurs)

## Fonctionnalités

- Affichage d'une liste de produits.
- Création de nouveaux produits avec des détails tels que le nom, la description, le prix et l'image.
- Interface utilisateur responsive pour une meilleure expérience sur mobile et bureau.

## Technologies utilisées

- **Python** - Langage de programmation.
- **Django** - Framework web.
- **HTML/CSS/JavaScript** - Technologies front-end.
- **SQLite** - Base de données (ou d'autres bases de données comme PostgreSQL).
- **Bootstrap** - Pour le style et la mise en page.

## Installation

Pour installer et exécuter ce projet sur votre machine locale, suivez les étapes ci-dessous :

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/nom_utilisateur/nom_depot.git
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd nom_depot
    ```

3. Créez un environnement virtuel :

    ```bash
    python -m venv venv
    ```

4. Activez l'environnement virtuel :

    - Sur Windows :

      ```bash
      .\venv\Scripts\activate
      ```

    - Sur macOS/Linux :

      ```bash
      source venv/bin/activate
      ```

5. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

6. Exécutez les migrations de la base de données :

    ```bash
    python manage.py migrate
    ```

7. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

8. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000` pour voir l'application en action.

## Utilisation

- Pour afficher la liste des produits, accédez à la page d'accueil.
- Pour créer un nouveau produit, cliquez sur le bouton approprié pour accéder au formulaire de création de produit.

## Contribuer

Les contributions sont les bienvenues ! Si vous souhaitez contribuer, veuillez suivre ces étapes :

1. Forkez ce projet.
2. Créez une nouvelle branche (`git checkout -b feature/votre-nou
