# NLP Narrative Game

## Présentation

Projet de NLP réalisé en groupe de 6 dans le cadre du mini-projet 2 : Agent conversationnel.

L'objectif est de développer un agent IA jouant le rôle de **Game Master** dans un jeu narratif interactif. L'agent décrit les situations, propose des actions au joueur et raconte les conséquences de ses choix, tout en respectant les règles et la cohérence de l'univers.

Le projet s'appuie sur **Qwen2.5-1.5B-Instruct**, avec une baseline conversationnelle puis une adaptation du modèle à l'aide de LoRA/QLoRA.

## Prérequis

- Git
- Python 3.12 ou une version compatible avec `pyproject.toml`
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Une connexion Internet pour installer les dépendances et télécharger le modèle
- Une machine disposant de ressources suffisantes pour exécuter le modèle et, le cas échéant, effectuer l'entraînement

## Installation

Cloner le dépôt :

```bash
git clone <URL_DU_DEPOT>
cd NLP_narrative-game
```

Installer les dépendances à partir du fichier de verrouillage :

```bash
uv sync --locked
```

## Lancer les notebooks

Démarrer JupyterLab :

```bash
uv run jupyter lab
```

Ouvrir ensuite le notebook situé dans le dossier `notebooks/`.

Dans VS Code, sélectionner le kernel Python correspondant à l'environnement `.venv` du projet.

## Lancer l'application

Lorsque le point d'entrée de l'application sera disponible, exécuter :

```bash
uv run python app.py
```

Si l'application utilise Gradio, l'adresse locale sera affichée dans le terminal au démarrage.

Exemple, pour lancer le model Qwen2.5-1.5B-Instruct avec comme contenue de système "Tu es le Game Master d'un jeu narratif."

```bash
uv run .\models\model.py
```

## Modèle et données

- **Modèle de base :** `Qwen/Qwen2.5-1.5B-Instruct`
- **Adaptation prévue :** LoRA/QLoRA
- **Données :** dialogues conçus et vérifiés par le groupe, selon les règles et les scénarios du jeu.

Consulter le dossier `data/` pour connaître la provenance des données et les instructions nécessaires à leur préparation.

## Reproductibilité

Le fichier `uv.lock` fixe les versions des dépendances Python afin de faciliter la reproduction de l'environnement de travail.

Les poids du modèle ne sont pas inclus dans le dépôt : ils sont téléchargés séparément lors de leur première utilisation.

## Équipe

Projet réalisé par un groupe de 6 étudiants de CY Tech, en 2026.