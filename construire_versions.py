"""Construit la version autonome de la présentation IRFASE.

- Presentation_IRFASE_Outils_IA_20261120_autonome.html : un seul fichier HTML, images intégrées.
  Les vidéos restent des liens relatifs vers assets/videos/ (trop lourdes pour être intégrées) :
  garder ce fichier à côté du dossier assets/ pour que le mode hors ligne fonctionne.

Usage : python3 construire_versions.py
"""
import base64
import re
from pathlib import Path

ICI = Path(__file__).parent
SOURCE = ICI / "index.html"
AUTONOME = ICI / "Presentation_IRFASE_Outils_IA_20261120_autonome.html"

TYPES = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".svg": "image/svg+xml"}


def integrer_images(texte):
    def remplacer(m):
        chemin = ICI / m.group(1)
        mime = TYPES.get(chemin.suffix.lower(), "application/octet-stream")
        return 'src="data:%s;base64,%s"' % (mime, base64.b64encode(chemin.read_bytes()).decode())
    return re.sub(r'src="(assets/img/[^"]+)"', remplacer, texte)


AUTONOME.write_text(integrer_images(SOURCE.read_text()))
print("Version autonome construite :", AUTONOME.name, "(%d Ko)" % (AUTONOME.stat().st_size // 1024))
