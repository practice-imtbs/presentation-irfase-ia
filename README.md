# Prise en main des outils IA · IRFASE, 20 novembre 2026

Diaporama de l'intervention de Julien MORICE (service PracTice, IMT Business School) devant l'Executive Master de l'IRFASE (Évry-Courcouronnes), vendredi 20/11/2026, 14 h 30 - 15 h 30. Créé le 19/11/2026.

Fil rouge : la direction d'une association du secteur social et médico-social (300 salarié·es, Essonne) prépare pour son conseil d'administration un dossier sur l'attractivité et la fidélisation des professionnel·les. Plan « l'escalier » : quatre marches (chercher, exploiter, faire faire, fabriquer) et deux paliers (le regard du manager, où vont mes données ?).

**Publication prévue (après accord de Julien seulement) :** https://practice-imtbs.github.io/presentation-irfase-ia/ (le QR code de la dernière slide pointe déjà vers cette adresse).

## Commandes

| Touche | Action |
|---|---|
| `→` `espace` / `←` | slide suivante / précédente |
| `S` (ou clic sur le numéro de slide) | sommaire cliquable, avec l'heure de début de chaque séquence |
| `N` | notes de l'orateur : séquence, heure de fin visée, horloge |
| `F` | plein écran |
| `L` | toutes les vidéos en copie locale (mémorisé dans le navigateur), et retour |
| `Début` / `Fin` | première / dernière slide |

Sur tablette : glisser à gauche ou à droite, ou utiliser les boutons en bas à droite.

## Minutage (60 minutes)

| Séquence | Slides | Début | Fin visée | Durée | Cumul |
|---|---|---|---|---|---|
| Ouverture | 1 à 5 | 14 h 30 | 14 h 35 | 5 min | 5 min |
| Marche 1 · Chercher (ChatGPT) | 6 à 10 | 14 h 35 | 14 h 47 | 12 min | 17 min |
| Marche 2 · Exploiter (Gemini Notebook) | 11 à 13 | 14 h 47 | 14 h 56 | 9 min | 26 min |
| Marche 3 · Faire faire (Claude Cowork) | 14 à 16 | 14 h 56 | 15 h 06 | 10 min | 36 min |
| Palier · le regard du manager | 17 et 18 | 15 h 06 | 15 h 13 | 7 min | 43 min |
| Palier · où vont mes données ? | 19 et 20 | 15 h 13 | 15 h 19 | 6 min | 49 min |
| Marche 4 · Fabriquer (PracTice Store) | 21 à 24 | 15 h 19 | 15 h 26 | 7 min | 56 min |
| Clôture | 25 et 26 | 15 h 26 | 15 h 30 | 4 min | 60 min |

Les notes donnent un temps par slide ; leur somme fait 57 min 30, soit 2 min 30 de marge, surtout dans la marche 1. Vidéos passées en entier : Gemini Notebook (6 min 05 pour 5 min prévues) et Cowork (3 min 59 pour 3 min 30) dépassent d'1 min 30 au total, absorbées par la marge. Le vrai risque, ce sont les démos en direct (recherche approfondie, carnet, Cowork) : si l'une traîne, basculer sur la vidéo.

## Vidéos

Toutes les vidéos sont déclarées dans **un seul bloc `window.VIDEOS`, en tête de `index.html`**. Pour remplacer une vidéo (par exemple une démo enregistrée sur le cas fil rouge), changer `permalien`, `local` et `duree` de la ligne concernée.

| Clé | Slide | Vidéo retenue | Durée | Copie locale |
|---|---|---|---|---|
| `recherche` | 9 | Atelier de rentrée, « La recherche approfondie » (v126d57857dbe4dfgqv8) | 1 min 41 | oui |
| `notebook` | 13 | Atelier de rentrée, « Apprendre avec Gemini Notebook » (v126d5785c9402wscekx) | 6 min 05 | oui |
| `cowork` | 16 | « Le pipeline vidéo avec Claude Cowork » (v126d3f9f9e01qh3478o) | 3 min 59 | oui |
| `compterendu` | 18 | « Le compte rendu à la main, avec un harnais » (v126d5d121f03i66a3ar) | 3 min 51 | oui |
| `application` | 23 | IMT Smart Minutes (v126d62234168kcpdlyv) | 1 min 53 | oui |

Toutes sont muettes ou presque (captures d'écran à commenter), sauf l'extrait du résumé audio dans Gemini Notebook (vers 3 min 40). Les autres vidéos fournies sont téléchargées dans `assets/videos/` et listées en commentaire dans le bloc, prêtes à servir : démo Cytiva muette (2 min 11), Gemini Notebook Cytiva (9 min 28), « Articuler plusieurs outils IA » (2 min, sur la création d'un visuel : écartée), PracTice Store public (7 min 57), espaces privés (2 min 32), LearnyBot (3 min 03), trailer du PracTice Store (55 s, sans permalien).

Point de vigilance : la vidéo du compte rendu (slide 18) montre un vrai compte rendu interne avec des noms ; elle a déjà été diffusée aux Jeudis de l'IA, mais avancer vite sur le document final.

### Mode hors ligne

- Copies locales dans `assets/videos/` (546 Mo, **exclues de git**), téléchargées depuis le Médiaserveur par son API le 19/11/2026, sans recompression (1080p, 16 à 113 Mo chacune).
- Sur chaque slide vidéo, le lecteur en ligne a 8 secondes pour répondre (il le signale par `postMessage`). Sinon, ou si le navigateur est hors ligne, la copie locale prend le relais avec un bandeau jaune. Le bouton « Passer à la copie locale » et la touche `L` forcent la copie locale.
- Le lien « Ouvrir la vidéo dans un onglet » pointe vers le Médiaserveur, ou vers le fichier local en mode copie locale.
- Testé le 19/11/2026 dans le navigateur (1920 × 1080) : lecteur en ligne chargé sur les cinq slides vidéo, bascule automatique avec un hôte injoignable, lecture de la copie locale en mode forcé. La coupure réelle du wifi n'a pas pu être simulée : à vérifier sur le Mac avant de partir (couper le wifi, ouvrir `index.html` en double-cliquant, aller sur la slide 9).
- En salle : ouvrir `index.html` depuis ce dossier (ou la version autonome, posée à côté de `assets/`). Si le wifi est mauvais, appuyer sur `L` dès le début.

## Emplacements « à compléter »

Cadres jaunes en pointillés, à remplir quand les rapports seront dans `../Rapports/` (aucun chiffre sur le secteur n'est inventé) :

- Slide 10 : trois chiffres clés du rapport 1 (postes vacants, turnover, candidatures en formation) et la capture du tableau des chiffres clés.
- Slide 15 : captures de la note au CA, du support et du tableau de bord produits par Claude Cowork.
- Slide 8 : les questions de clarification affichées sont un exemple type ; les vraies questions de ChatGPT se lisent en direct.

## Fichiers

- `index.html` : la présentation (moteur repris de la présentation CODOFO du 04/11/2026, sommaire et commandes tactiles de l'atelier de rentrée).
- `assets/img/` : logo IMT-BS, photo, capture du PracTice Store, QR code de la présentation.
- `assets/videos/` : copies locales des vidéos (hors git).
- `construire_versions.py` : génère `Presentation_IRFASE_Outils_IA_20261120_autonome.html` (images intégrées, vidéos en lien relatif vers `assets/videos/`).
- Dépôt git local, sans dépôt distant tant que la publication n'est pas validée.

## Publication (après accord)

1. Créer le dépôt `practice-imtbs/presentation-irfase-ia` sur GitHub et activer GitHub Pages (branche `main`, racine).
2. `git remote add origin https://github.com/practice-imtbs/presentation-irfase-ia.git` puis `git push -u origin main`.
3. Les vidéos ne partent pas sur GitHub : en ligne, seuls les lecteurs du Médiaserveur servent.
