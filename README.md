Calculateur d'Itinéraire Optimal

Ce projet calcule l'itinéraire de voyage optimal entre les villes en fonction des coûts de transport. Le programme récupère les données d'une base PostgreSQL mais prend également en charge une option de secours basée sur un fichier CSV.

Exigences

1. Installer les dépendances Python

Assurez-vous que Python est installé. Ensuite, installez les packages requis :

pip install psycopg2 networkx

2. Configuration de la Base de Données (Recommandé)

Si vous avez PostgreSQL installé, suivez ces étapes :

Créez une nouvelle base de données :

createdb tourism

Exécutez le script SQL pour créer les tables et insérer des données d'exemple :

psql -U your_user -d tourism -f setup.sql

Mettez à jour optimal_route.py avec vos identifiants de base de données.

3. Exécution du Programme

Exécutez le script :

python optimal_route.py

Fichiers dans ce Répertoire

optimal_route.py – Le script principal qui calcule les itinéraires optimaux

setup.sql – Script SQL pour configurer la base de données

README.md – Ce fichier

Remarques

Assurez-vous que PostgreSQL est en cours d'exécution avant d'exécuter les commandes liées à la base de données.

Si vous utilisez la base de données, mettez à jour optimal_route.py avec vos identifiants.

