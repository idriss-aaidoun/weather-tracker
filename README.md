# 🌤️ Weather Tracker AI

> Application Python qui combine une **REST API météo** et une **IA générative** (cloud ou locale) pour afficher et analyser les conditions météorologiques en langage naturel.

---

## 📋 Table des matières

- [🌤️ Weather Tracker AI](#️-weather-tracker-ai)
  - [📋 Table des matières](#-table-des-matières)
  - [📌 Aperçu du projet](#-aperçu-du-projet)
  - [🏗️ Architecture](#️-architecture)
  - [🛠️ Technologies utilisées](#️-technologies-utilisées)
  - [✨ Fonctionnalités](#-fonctionnalités)
    - [1. Météo d'une ville avec analyse IA](#1-météo-dune-ville-avec-analyse-ia)
    - [2. Comparaison multi-villes](#2-comparaison-multi-villes)
    - [3. IA Cloud vs IA Locale](#3-ia-cloud-vs-ia-locale)
  - [⚙️ Installation](#️-installation)
    - [Prérequis](#prérequis)
    - [Étapes](#étapes)
  - [🔑 Configuration](#-configuration)
    - [Obtenir les clés API](#obtenir-les-clés-api)
  - [🚀 Utilisation](#-utilisation)
  - [📁 Structure du projet](#-structure-du-projet)
  - [🧠 Concepts appris](#-concepts-appris)
    - [REST API](#rest-api)
    - [Sécurité](#sécurité)
    - [Intelligence Artificielle](#intelligence-artificielle)
    - [Bonnes pratiques](#bonnes-pratiques)
  - [📈 Évolutions possibles](#-évolutions-possibles)
  - [📄 Licence](#-licence)

---

## 📌 Aperçu du projet

Weather Tracker AI est un projet d'apprentissage qui illustre comment intégrer plusieurs APIs dans une application Python. L'utilisateur entre le nom d'une ville et obtient :

- Les **données météo en temps réel** via l'API OpenWeatherMap
- Une **analyse en langage naturel** générée par un LLM (Groq cloud ou Ollama en local)
- La possibilité de **comparer plusieurs villes** dans un tableau

Ce projet a été construit pour comprendre le fonctionnement des REST APIs, des LLMs, et la différence entre une IA hébergée dans le cloud et une IA tournant en local sur sa propre machine.

---

## 🏗️ Architecture

```
Utilisateur
    │
    ▼
main.py  ──────────────────────────────────────────┐
    │                                               │
    ▼                                               ▼
weather.py                                  ai_analysis.py / ai_local.py
    │                                               │
    ▼                                               ▼
API OpenWeatherMap                         Groq API (cloud)
(REST API externe)                    OU   Ollama (localhost:11434)
    │                                               │
    └───────────────────┬───────────────────────────┘
                        ▼
              Résultat affiché dans le terminal
```

**Flux de données :**
1. L'utilisateur entre une ville
2. `weather.py` appelle l'API OpenWeatherMap → reçoit température, humidité, vent, etc.
3. Ces données sont envoyées comme **contexte** au LLM via un prompt
4. Le LLM génère une analyse en français en langage naturel
5. Le résultat est affiché dans le terminal

---

## 🛠️ Technologies utilisées

| Technologie | Rôle | Type |
|---|---|---|
| Python 3.x | Langage principal | - |
| OpenWeatherMap API | Source des données météo | REST API externe |
| Groq API | LLM cloud (LLaMA 70B) | REST API externe |
| Ollama | LLM local (LLaMA 3.2) | REST API locale |
| `requests` | Appels HTTP vers les APIs | Bibliothèque Python |
| `python-dotenv` | Gestion des variables d'environnement | Bibliothèque Python |
| `groq` | Client officiel Groq | Bibliothèque Python |
| Git / GitHub | Versioning et collaboration | Outil |

---

## ✨ Fonctionnalités

### 1. Météo d'une ville avec analyse IA
Entrer le nom d'une ville et obtenir les données météo complètes accompagnées d'une analyse générée par intelligence artificielle.

```
=== WEATHER TRACKER ===
1 — Météo d'une ville (Groq)
2 — Météo d'une ville (Ollama local)
3 — Comparer plusieurs villes

Ton choix : 1
Ville : Rabat

 Recherche météo pour : Rabat
----------------------------------------
Ville       : Rabat, MA
Température : 22.5°C
Ressenti    : 21.8°C
Humidité    : 68%
Ciel        : ciel dégagé
Vent        : 3.2 m/s

 Analyse IA :
----------------------------------------
Le temps à Rabat est agréable aujourd'hui avec une température
douce de 22°C et un ciel bien dégagé. Je te conseille une tenue
légère mais prévois peut-être une veste légère pour la soirée.
C'est une excellente journée pour sortir se promener !
```

### 2. Comparaison multi-villes
Afficher un tableau comparatif de plusieurs villes côte à côte.

```
Ville                Temp   Humidité     Vent
--------------------------------------------------
Rabat               22.5°C       68%   3.2 m/s
Paris               14.0°C       80%   5.1 m/s
Tokyo               18.3°C       72%   2.8 m/s
```

### 3. IA Cloud vs IA Locale
Choisir entre deux moteurs d'IA :
- **Groq** → LLaMA 70B sur serveurs distants, rapide et précis
- **Ollama** → LLaMA 3.2 sur ta propre machine, 100% privé, sans internet

---

## ⚙️ Installation

### Prérequis
- Python 3.8 ou supérieur
- pip
- Git
- Ollama installé (optionnel, pour le mode local)

### Étapes

**1. Cloner le repository**
```bash
git clone https://github.com/TON-USERNAME/weather-tracker.git
cd weather-tracker
```

**2. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3. Créer le fichier `.env`**
```bash
cp .env.example .env
# Puis édite .env avec tes propres clés API
```

**4. (Optionnel) Installer un modèle Ollama**
```bash
ollama pull llama3.2
```

---

## 🔑 Configuration

Crée un fichier `.env` à la racine du projet avec les variables suivantes :

```env
OPENWEATHER_API_KEY=ta_clé_openweathermap
GROQ_API_KEY=ta_clé_groq
```

### Obtenir les clés API

| Service | Lien | Coût |
|---|---|---|
| OpenWeatherMap | [openweathermap.org](https://openweathermap.org/api) | Gratuit |
| Groq | [console.groq.com](https://console.groq.com) | Gratuit |
| Ollama | [ollama.com](https://ollama.com) | Gratuit (local) |

> ⚠️ **Important** : Ne commite jamais ton fichier `.env` sur GitHub. Il est déjà listé dans `.gitignore`.

---

## 🚀 Utilisation

```bash
python main.py
```

Le menu s'affiche :

```
=== WEATHER TRACKER ===
1 — Météo d'une ville (Groq)
2 — Météo d'une ville (Ollama local)
3 — Comparer plusieurs villes
```

Pour le mode comparaison, entrer les villes séparées par une virgule :
```
Entre les villes séparées par une virgule : Rabat, Paris, Tokyo
```

---

## 📁 Structure du projet

```
weather-tracker/
│
├── main.py              # Point d'entrée — menu et orchestration
├── weather.py           # Appel REST API OpenWeatherMap
├── ai_analysis.py       # Analyse IA via Groq (cloud)
├── ai_local.py          # Analyse IA via Ollama (local)
│
├── requirements.txt     # Dépendances Python
├── .env                 # Variables d'environnement (non commité)
├── .env.example         # Template du fichier .env
├── .gitignore           # Fichiers ignorés par Git
└── README.md            # Documentation du projet
```

---

## 🧠 Concepts appris

Ce projet couvre les concepts fondamentaux du développement moderne :

### REST API
- Anatomie d'une requête HTTP : méthode, URL, headers, body
- Codes de statut HTTP (200, 401, 404, 500)
- Pourquoi on utilise `POST` pour les LLMs et `GET` pour la météo
- Différence entre API externe (cloud) et API locale (Ollama)

### Sécurité
- Gestion des clés API avec `.env` et `python-dotenv`
- Rôle du `.gitignore` pour protéger les secrets
- Pourquoi on ne code jamais une clé API en dur dans le code

### Intelligence Artificielle
- Différence entre LLM cloud (Groq) et LLM local (Ollama)
- Concept de prompt engineering : envoyer des données comme contexte
- Différence entre Open Source et Open Weights pour les modèles IA
- Pourquoi Groq est plus rapide (LPU vs CPU grand public)

### Bonnes pratiques
- Séparation des responsabilités (un fichier = une responsabilité)
- Workflow Git : `add` → `commit` → `push`
- Convention de nommage des commits (`feat:`, `fix:`, `docs:`)

---

## 📈 Évolutions possibles

- [ ] Historique des recherches en JSON
- [ ] Alertes météo personnalisées (seuil de température)
- [ ] Prévisions sur 5 jours via endpoint `/forecast`
- [ ] Interface web avec Flask
- [ ] Base de données SQLite pour sauvegarder l'historique
- [ ] Dashboard avec graphiques

---

## 📄 Licence

Ce projet est open source — libre d'utilisation pour l'apprentissage.

---

*Projet réalisé dans le cadre d'un apprentissage des APIs REST et de l'intégration de modèles LLM en Python.*
