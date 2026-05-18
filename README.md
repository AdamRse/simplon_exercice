# mysql-python-docker

Projet Python de test pour se connecter à un serveur MySQL, exécuter des requêtes et afficher les résultats. Conteneurisé avec Docker et géré via Dockge.

## Structure

```
.
├── src/
│   ├── main.py        # Script principal
│   └── db.py          # Module de connexion MySQL
├── .env.example       # Modèle des variables d'environnement
├── .gitignore
├── docker-compose.yml # Compatible Dockge
├── Dockerfile
├── requirements.txt
└── README.md
```

## Mise en place

### 1. Cloner le dépôt et créer le `.env`

```bash
git clone <url-du-repo>
cd mysql-python-docker
cp .env.example .env
```

Édite `.env` avec tes vraies valeurs :

```env
MYSQL_HOST=host.docker.internal   # si MySQL est sur l'hôte KubuUbuntu
MYSQL_PORT=3306
MYSQL_USER=ton_utilisateur
MYSQL_PASSWORD=ton_mot_de_passe
MYSQL_DATABASE=ta_base_de_donnees
```

> **Note :** Si ton serveur MySQL tourne directement sur KubuUbuntu (hors Docker), utilise `host.docker.internal` comme `MYSQL_HOST`. Le `docker-compose.yml` est déjà configuré pour ça.

### 2. Lancer avec Dockge

Dans Dockge, crée un nouveau stack en pointant vers ce dossier. Le `.env` sera automatiquement chargé par `env_file`.

### 3. Lancer manuellement (sans Dockge)

```bash
docker compose up --build
```

## Développement local (sans Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # puis remplis le .env
python src/main.py
```

## Ajouter des requêtes

Édite `src/main.py` dans la fonction `run()` pour ajouter tes propres requêtes SQL.
