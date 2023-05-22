# Utiliser une image Docker officielle de Python comme base
FROM python:3.9

# Rendre le stdout et stderr non bloquants pour améliorer les logs de Docker
ENV PYTHONUNBUFFERED=1

# Installer les dépendances
# Copier le fichier requirements.txt de votre projet Django dans le conteneur
COPY requirements.txt /

# Exécuter pip pour installer les dépendances
RUN pip install -r /requirements.txt

# Créer un répertoire pour le code de l'application dans le conteneur
WORKDIR /app

# Copier le reste du code de l'application dans le conteneur
COPY . /app

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Définir la commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
