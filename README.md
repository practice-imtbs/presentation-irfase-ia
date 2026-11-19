# Prise en main des outils IA · IRFASE, 20 novembre 2026

Diaporama (31 slides) de l'intervention de Julien MORICE (service PracTice, IMT Business School) devant l'Executive Master de l'IRFASE (Évry-Courcouronnes), vendredi 20/11/2026, 14 h 30 - 15 h 30. Créé le 19/11/2026.

Fil rouge : la direction d'une association du secteur social et médico-social (300 salarié·es, Essonne) prépare pour son conseil d'administration un dossier sur l'attractivité et la fidélisation des professionnel·les. Plan « l'escalier » : quatre marches (chercher, exploiter, faire faire, fabriquer) et deux paliers (le regard du manager, où vont mes données ?).

**En ligne depuis le 19/11/2026 (accord de Julien) :** https://practice-imtbs.github.io/presentation-irfase-ia/ (dépôt public https://github.com/practice-imtbs/presentation-irfase-ia, GitHub Pages sur `main`, racine ; le QR code de la dernière slide pointe vers cette adresse).

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
| Marche 1 · Chercher (ChatGPT) | 6 à 12 | 14 h 35 | 14 h 47 | 12 min | 17 min |
| Marche 2 · Exploiter (Gemini Notebook) | 13 à 17 | 14 h 47 | 14 h 56 | 9 min | 26 min |
| Marche 3 · Faire faire (Claude Cowork) | 18 à 20 | 14 h 56 | 15 h 06 | 10 min | 36 min |
| Palier · le regard du manager | 21 et 22 | 15 h 06 | 15 h 13 | 7 min | 43 min |
| Palier · où vont mes données ? | 23 et 24 | 15 h 13 | 15 h 19 | 6 min | 49 min |
| Marche 4 · Fabriquer (PracTice Store) | 25 à 28 | 15 h 19 | 15 h 26 | 7 min | 56 min |
| Clôture | 29 et 30 | 15 h 26 | 15 h 30 | 4 min | 60 min |

Les notes donnent un temps par slide ; leur somme fait 59 min, soit 1 min de marge (la marche 1 tient pile en 12 min avec ses trois nouvelles slides). Les deux médias Gemini ne se passent pas en entier : 45 secondes du résumé audio (15 min 18) et 2 minutes de la vidéo (6 min 22). La vidéo Cowork passée en entier (3 min 59 pour 3 min 30) reste dans la marge. Le vrai risque, ce sont les démos en direct (recherche approfondie, carnet, Cowork) : si l'une traîne, basculer sur la vidéo.

## Vidéos

Toutes les vidéos sont déclarées dans **un seul bloc `window.VIDEOS`, en tête de `index.html`**. Pour remplacer une vidéo (par exemple une démo enregistrée sur le cas fil rouge), changer `permalien`, `local` et `duree` de la ligne concernée.

| Clé | Slide | Vidéo retenue | Durée | Copie locale |
|---|---|---|---|---|
| `recherche` | 9 | Atelier de rentrée, « La recherche approfondie » (v126d57857dbe4dfgqv8) | 1 min 41 | oui |
| `podcast` | 15 | Résumé audio Gemini Notebook sur les trois rapports, « Stopper l'hémorragie dans le médico-social » (v126d68cf011cqe8ydae, audio M4A) | 15 min 18 | oui |
| `videogemini` | 16 | Vidéo Gemini Notebook sur les trois rapports, « Stratégies RH décodées » (v126d68cf011al793ap1) | 6 min 22 | oui |
| `contexte` | 20 | « Context engineering avec Claude Code : du dossier aux trois livrables », démo muette du cas fil rouge de bout en bout, avec sept étapes minutées à côté (v126d68cf57ef0dhuepk, déposée le 19/11/2026) | 2 min 48 | oui |
| `cowork` | 21 | « Le pipeline vidéo avec Claude Cowork » (v126d3f9f9e01qh3478o) | 3 min 59 | oui |
| `compterendu` | 23 | « Le compte rendu à la main, avec un harnais » (v126d5d121f03i66a3ar) | 3 min 51 | oui |
| `application` | 28 | IMT Smart Minutes (v126d62234168kcpdlyv) | 1 min 53 | oui |

Toutes sont muettes ou presque (captures d'écran à commenter), sauf l'extrait du résumé audio dans Gemini Notebook (vers 3 min 40). Les autres vidéos fournies sont téléchargées dans `assets/videos/` et listées en commentaire dans le bloc, prêtes à servir : démo Cytiva muette (2 min 11), Gemini Notebook Cytiva (9 min 28), « Articuler plusieurs outils IA » (2 min, sur la création d'un visuel : écartée), PracTice Store public (7 min 57), espaces privés (2 min 32), LearnyBot (3 min 03), trailer du PracTice Store (55 s, sans permalien).

Slide 20 (ajoutée le 19/11/2026) : à passer en 2 à 3 min, ou en relais de la démo en direct si elle traîne ; elle n'entre pas dans le minutage de 59 min, la prendre sur la marge ou sur la démo.

Point de vigilance : la vidéo du compte rendu (slide 23) montre un vrai compte rendu interne avec des noms ; elle a déjà été diffusée aux Jeudis de l'IA, mais avancer vite sur le document final.

### Mode hors ligne

- Copies locales dans `assets/videos/` (546 Mo, **exclues de git**), téléchargées depuis le Médiaserveur par son API le 19/11/2026, sans recompression (1080p, 16 à 113 Mo chacune).
- Sur chaque slide vidéo, le lecteur en ligne a 8 secondes pour répondre (il le signale par `postMessage`). Sinon, ou si le navigateur est hors ligne, la copie locale prend le relais avec un bandeau jaune. Le bouton « Passer à la copie locale » et la touche `L` forcent la copie locale.
- Le lien « Ouvrir la vidéo dans un onglet » pointe vers le Médiaserveur, ou vers le fichier local en mode copie locale.
- Testé le 19/11/2026 dans le navigateur (1920 × 1080) : lecteur en ligne chargé sur les cinq slides vidéo, bascule automatique avec un hôte injoignable, lecture de la copie locale en mode forcé. La coupure réelle du wifi n'a pas pu être simulée : à vérifier sur le Mac avant de partir (couper le wifi, ouvrir `index.html` en double-cliquant, aller sur la slide 9).
- En salle : ouvrir `index.html` depuis ce dossier (ou la version autonome, posée à côté de `assets/`). Si le wifi est mauvais, appuyer sur `L` dès le début.

## Productions Gemini Notebook sur le cas fil rouge (ajoutées le 19/11/2026)

Slides 15 à 17, à partir des trois rapports mis en sources dans Gemini Notebook :
- **Résumé audio** « Stopper l'hémorragie dans le médico-social » (15 min 18) et **vidéo** « Stratégies RH décodées » (6 min 22), déposés par Julien sur le Médiaserveur (chaîne « Embed public »), avec copies locales `Gemini_Podcast_Medico_Social.m4a` et `Gemini_Video_Strategies_RH.mp4` dans `assets/videos/` (originaux dans `_Projets/Ubiscast/videosAImporterDansEmbedPublic/Deposees/`).
- **Rapport** « Vaincre la crise d'attractivité : attirer et fidéliser dans le secteur social et médico-social » (fonction « Rapport », format leçon interactive, cinq parties) : lien court **https://is.gd/kwysbi** (créé le 19/11/2026 sur is.gd, sans compte, vérifié) et QR code `assets/img/qr_rapport_gemini.png`. Sur la slide, le lien affiché est le lien court mais il pointe directement vers l'adresse complète, qui marche même si is.gd tombe : https://notebook.google.com/notebook/f7570436-d31e-4c6a-86fa-313412261b63/artifact/ea391416-37a0-4d74-87cd-34538eba417c
- La vidéo « Apprendre avec Gemini Notebook » de l'atelier de rentrée sort du diaporama (gardée en commentaire dans `window.VIDEOS`) pour rester à deux vidéos dans la marche 2.

## Rapports et prompts (ajoutés le 19/11/2026 après-midi)

Les trois rapports de recherche approfondie déposés par Julien dans `../recherchesApprofondies/` sont copiés dans `assets/rapports/` (Rapport_1_Etat_des_lieux.pdf, Rapport_2_Leviers_Essonne.pdf, Rapport_3_Management_Gouvernance.pdf) et s'ouvrent depuis la slide 12. Le bouton « Lire le prompt » affiche le prompt complet de chaque recherche (textes de `../Prompts_Recherches_Approfondies.md`), Échap pour fermer.

- **Slide 10, trois chiffres** : 4,5 % de postes vacants et 24,4 % de turnover dans les ESMS (CNSA, données 2023, cités par les rapports 1 et 3), « une éducatrice spécialisée sur deux a quitté le métier neuf ans après » (DREES, mars 2025, rapport 2), et 68,4 % de recrutements difficiles d'éducateur·rices spécialisé·es en Essonne (France Travail, BMO 2026, rapport 2). La page de la CNSA n'a pas pu être relue le 19/11 (certificat refusé) : à ouvrir une fois avant la séance.
- **Slide 11, le piège** : le rapport 1 cite la même source DREES pour deux salaires, 2 090 € et 1 395 €. Vérification du 19/11 : 2 090 € figure bien dans la publication DREES du 29/09/2025, 1 395 € est introuvable. Ses renvois de sources sont aussi restés illisibles à l'export (【66†L107】) : exemple vivant du « travail délégué ».
- **Écarté** : les chiffres des formations sociales du rapport 1 (57 300 inscrits en 2023, −11,2 % en première année depuis 2010) n'ont pas été retrouvés à la DREES, dont la dernière publication porte sur 2025 (55 900 inscrits, −2,3 %).
- **Encore à compléter** (cadres jaunes) : slide 19, captures de la note au CA, du support et du tableau de bord produits par Claude Cowork. Slide 8 : les questions de clarification affichées sont un exemple type.

## Fichiers

- `index.html` : la présentation (moteur repris de la présentation CODOFO du 04/11/2026, sommaire et commandes tactiles de l'atelier de rentrée).
- `assets/rapports/` : les trois rapports en PDF (publiés avec la présentation).
- `assets/img/` : logo IMT-BS, photo, capture du PracTice Store, QR codes de la présentation, du rapport Gemini et du profil LinkedIn (slides 2 et 30).
- `assets/videos/` : copies locales des vidéos (hors git).
- `construire_versions.py` : génère `Presentation_IRFASE_Outils_IA_20261120_autonome.html` (images intégrées, vidéos en lien relatif vers `assets/videos/`).
- Dépôt git publié sur https://github.com/practice-imtbs/presentation-irfase-ia (public).

## Mise à jour en ligne

Après une modification : `python3 construire_versions.py`, puis `git add -A && git commit -m "…" && git push`. GitHub Pages republie en une minute environ. Le dépôt appartient au compte GitHub `practice-imtbs` (`gh auth switch -u practice-imtbs` avant de pousser si `gh` est sur un autre compte).

Les vidéos ne partent pas sur GitHub (exclues par `.gitignore`) : en ligne, seuls les lecteurs du Médiaserveur servent, et la copie locale n'existe que sur le Mac.
