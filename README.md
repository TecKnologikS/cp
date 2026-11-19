# cp

Site de Code Postal (cp.tecknologiks.com) : présentation, politique de confidentialité, support et mentions légales, en anglais (racine) et en français (`fr/`).

Site statique publié avec GitHub Pages (workflow `.github/workflows/pages.yml`, à chaque push sur `main`). Réglage à faire une fois sur GitHub : Settings → Pages → Source : « GitHub Actions ». Le domaine est donné par `CNAME` (enregistrement DNS `cp` à créer côté domaine).

Les pages sont générées par `build.py` (textes et gabarit communs) : modifier `build.py`, puis lancer `python3 build.py .` et committer les HTML. Le prix de Premium est la constante `PRICE` de `build.py`.

| Page | Rôle | URL à déclarer |
| --- | --- | --- |
| `index.html`, `fr/index.html` | Présentation, lien App Store, Smart App Banner | App Store Connect → *Marketing URL* |
| `privacy.html`, `fr/confidentialite.html` | Politique de confidentialité (AdMob, UMP, ATT, localisation, achat Premium) | App Store Connect → *Privacy Policy URL* ; AdMob → message RGPD |
| `support.html`, `fr/support.html` | Contact et FAQ | App Store Connect → *Support URL* |
| `legal.html`, `fr/mentions-legales.html` | Mentions légales | — |

Polices Barlow Condensed auto-hébergées (`assets/fonts`, licence OFL incluse) : aucune ressource externe, aucun cookie.

## À garder à jour

La politique de confidentialité décrit le fonctionnement réel de l'app (consentement UMP puis ATT, bannière de l'onglet Rechercher, onglet Autour de moi et API Géo, libellés « Options de confidentialité », « Sans pub », « Restaurer les achats »). Toute évolution qui touche aux données (nouveau SDK, analytics, compte, synchronisation des favoris, autre achat…) doit être reportée ici avant sa mise en ligne, ainsi que dans la fiche « Confidentialité » d'App Store Connect. Le prix (`PRICE`) et la date `UPDATED` aussi.

Icône : `assets/icon-*.png`, redimensionnée depuis `iosApp/iosApp/Assets.xcassets/AppIcon.appiconset/AppIcon.png` du dépôt de l'app (générée par `tools/icon/generate_icon.py`). À faire : badge officiel « Download on the App Store » (absent des sites modèles : lien texte).

Ces textes ne remplacent pas un avis juridique.
