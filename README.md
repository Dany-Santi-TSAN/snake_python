# 🐍 Snake Game - Web Deploy

Un jeu Snake classique développé avec Pygame et déployé sur le web avec Pygbag.

## 🎮 Fonctionnalités

**Gameplay classique** : Mangez les pommes, grandissez, évitez les murs et votre queue

**Vitesse progressive** : Le jeu s'accélère tous les 5 points

**Effets sonores** : Sons pour manger, accélérer et game over

**Compatible Web** : Fonctionne dans tous les navigateurs modernes

**Déploiement automatique** : CI/CD avec GitHub Actions

## 🚀 Déploiement

Automatique (GitHub Pages)

Push ton code sur la branche main

GitHub Actions build et déploie automatiquement

Jeu accessible sur https://tonusername.github.io/snake-game

## ➡️ Docs officielles lues et suivies :

https://pygame-web.github.io/wiki/publishing/github.io/

https://pygame-web.github.io/

## Local

### Installer les dépendances
pip install pygbag pygame

### Rendre le script exécutable
chmod +x build.sh

### Builder le jeu
./build.sh

### Tester localement
cd dist && python -m http.server 8000
## Ouvrir http://localhost:8000

## 📁 Structure

snake-game/

├── main.py               # Point d'entrée principal

├── audio_manager.py      # Classe AudioManager

├── game_logic/           # Logique du jeu

│       ├── snake.py          # Classe Snake

│       ├── food.py           # Classe Food

│       └── display.py        # Affichage et UI

├── sounds/               # Fichiers audio (.ogg)

│       ├── apple_bite-pygbag.ogg

│       ├── f1_sound-pygbag.ogg

│       └── crash-pygbag.ogg

├── sprite/               # Images et sprites

│       └── apple_sprite.png

├── .github/workflows/    # CI/CD

│       └── deploy.yml

├── build.sh              # Script de build local

├── pyproject.toml        # Configuration

└── README.md

## 🎯 Contrôles

Flèches directionnelles : Déplacer le serpent

R : Redémarrer après un game over

Fermer : Quitter le jeu

## 🔧 Corrections apportées

Problèmes résolus :

**Audio WebAssembly** : Gestion d'erreurs et fallbacks

**Boucle Pygbag** : Utilisation correcte de pygbag.aio.run()

**Chargement assets** : Vérification d'existence des fichiers

**Compatibilité navigateur** : Paramètres mixer optimisés (non résolu)

## Améliorations :


Détection automatique de l'environnement (local vs web)

Configuration Pygbag optimisée

CI/CD automatique avec GitHub Actions

## 🛠️ Développement

### Modifier les sons

Au cas où si vous arrivez à modifier le son :
💀 Le son fonctionne en local.
🕳️ Mais dès que je le déploie, le silence se fait.
J’ai lu 3 docs, consulté 3 IA, parlé à 2 navigateurs.
Rien. Que le vide.
…
Bref, bienvenue dans le monde merveilleux de WebAssembly et des navigateurs capricieux.

Mais théoriquement il faut faire ça :

Ajouter tes fichiers .ogg dans sounds/

Modifier les références dans main.py

Rebuild avec ./build.sh

### Modifier le gameplay

**Snake** : game_logic/snake.py

**Food** : game_logic/food.py

**Affichage** : game_logic/display.py

**Logique principale** : main.py

**Audio** : audio_manager.py

### Ajouter des sprites

Placer les images dans sprite/

Modifier food.py pour utiliser l'image

Décommenter les lignes d'image dans la classe Food

## 🐛 Dépannage

Le jeu ne se lance pas en local

### Vérifier l'installation
pip list | grep pygbag
pip list | grep pygame

### Réinstaller si nécessaire
pip install --upgrade pygbag pygame

Écran noir après déploiement

Vérifier que les assets sont bien inclus

Consulter la console navigateur pour les erreurs

S'assurer que les chemins de fichiers sont corrects

### Audio ne fonctionne pas

Le navigateur peut bloquer l'audio au début

Cliquer une fois sur la page pour activer l'audio

Vérifier que les fichiers .ogg sont présents dans sounds/

Certains navigateurs (notamment Chrome et Firefox) ont des restrictions strictes

Le son fonctionne en local mais pas en ligne, malgré tous les correctifs connus (bug lié à WebAssembly ou Pygbag encore non résolu)

### 🚨 TL;DR : Le son, c’est comme les serpents… ça glisse entre les doigts quand on pense le contrôler.

## 📈 Suggestions futures

Ajouter un GIF de démo pour illustrer le gameplay

Intégrer un badge GitHub Actions pour montrer l'état du build

**TODO List pour les features à venir** :

Skins customisés pour le serpent

Leaderboard avec meilleurs scores

Mode hardcore (vitesses plus rapides, murs mortels)

Niveau bonus, ou power-ups ?

## 📜 Licence

Projet libre - Utilise et modifie comme tu veux !

**Développé avec ❤️, beaucoup de café ☕, et un soupçon de désespoir sonore 🎷**
