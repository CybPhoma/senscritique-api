# **Test technique DevOPS**

Durée : **2 h** 

Contexte : Vous travaillez pour SensCritique en tant que DevOps et nous souhaitons mettre en place la stack technique d'un nouveau projet.

### **API**

Le projet est simple, vous devez réaliser une API Python qui permet de voir la note SensCritique d'un film ou d'une série. Vous devrez utiliser Python comme langage pour cette API (obligatoire). L'API doit comporter les endpoint suivants :

 `GET /product/<id>` - Récupération des informations d'un film ou série (titre, note, genre etc) depuis Redis. 

`POST /product/<id>` - Création des informations d'un film ou série et persistence dans Redis.

Cette API doit fonctionner sur une stack locale sous Docker.

### **Stack locale**

- Docker et/ou docker-compose
- Redis pour stocker la donnée

### **Commandes**

Vous devrez ajouter une commande pour permettre de supprimer les produits (films/séries) qui sont déjà enregistrés dans Redis.

## **Contraintes**

- **Docker** pour la stack et Python pour l'API, pour le reste, à vous de voir.
- **Redis** pour le système de cache.
- Votre **API doit être accessible en se connectant sur `http://test.senscritique.local`** depuis votre machine hôte.
- Votre **test-technique doit être hébergé sur Github ou Gitlab** puis être **accessible en public**.
