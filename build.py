"""Generates the static pages of cp.tecknologiks.com (EN at the root, FR in fr/)."""
import pathlib, sys

OUT = pathlib.Path(sys.argv[1])
APP_ID = "1579357995"
STORE = f"https://apps.apple.com/app/id{APP_ID}"
MAIL = "support@tecknologiks.com"
DOMAIN = "https://cp.tecknologiks.com/"
# Price of the one-time Premium purchase: change it here only (the App Store shows the real price per country).
PRICE = {"en": "$2.99", "fr": "2,99 €"}
UPDATED = {"en": "November 19, 2026", "fr": "19 novembre 2026"}

PAGES = {
    "en": {"home": "index.html", "privacy": "privacy.html", "support": "support.html", "legal": "legal.html"},
    "fr": {"home": "index.html", "privacy": "confidentialite.html", "support": "support.html", "legal": "mentions-legales.html"},
}
LABELS = {
    "en": {"home": "Home", "privacy": "Privacy", "support": "Support", "legal": "Legal notice", "privacy_long": "Privacy policy"},
    "fr": {"home": "Accueil", "privacy": "Confidentialité", "support": "Support", "legal": "Mentions légales", "privacy_long": "Politique de confidentialité"},
}


def href(lang, page, from_lang):
    """Link from a page in from_lang to page in lang."""
    if lang == from_lang:
        return PAGES[lang][page] if page != "home" else "./"
    if lang == "fr":
        return "fr/" + (PAGES["fr"][page] if page != "home" else "")
    return "../" + (PAGES["en"][page] if page != "home" else "")


def render(lang, page, title, description, body):
    pre = "" if lang == "en" else "../"
    other = "fr" if lang == "en" else "en"
    L = LABELS[lang]
    current = ' aria-current="page"'
    nav = "\n".join(
        f'        <a href="{href(lang, p, lang)}"{current if p == page else ""}>{L[p]}</a>'
        for p in ("support", "privacy"))
    foot = "\n".join(f'        <a href="{href(lang, p, lang)}">{L["privacy_long"] if p == "privacy" else L[p]}</a>'
                     for p in ("home", "support", "privacy", "legal"))
    alt_en = DOMAIN + (PAGES["en"][page] if page != "home" else "")
    alt_fr = DOMAIN + "fr/" + (PAGES["fr"][page] if page != "home" else "")
    trademarks = ("App Store and Apple Maps are trademarks of Apple Inc. Google, Google Maps and AdMob are trademarks of Google LLC. Waze is a trademark of Waze Ltd. Code Postal is not affiliated with these companies."
                  if lang == "en" else
                  "App Store et Plans sont des marques d’Apple Inc. Google, Google Maps et AdMob sont des marques de Google LLC. Waze est une marque de Waze Ltd. Code Postal n’est pas affilié à ces sociétés.")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#2445a8">
  <meta name="apple-itunes-app" content="app-id={APP_ID}">
  <link rel="icon" href="{pre}assets/icon-64.png" type="image/png">
  <link rel="apple-touch-icon" href="{pre}assets/icon-180.png">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="fr" href="{alt_fr}">
  <link rel="alternate" hreflang="x-default" href="{alt_en}">
  <link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
  <div class="wrap">
    <header class="site">
      <a class="brand" href="./">Code Postal</a>
      <nav class="site" aria-label="{'Navigation' if lang == 'en' else 'Navigation'}">
{nav}
        <a href="{href(other, page, lang)}" hreflang="{other}" lang="{other}">{other.upper()}</a>
      </nav>
    </header>

{body}

    <footer class="site">
      <nav aria-label="{'Legal links' if lang == 'en' else 'Liens légaux'}">
{foot}
      </nav>
      <p>{trademarks}</p>
      <p>© 2026 <a href="https://tecknologiks.com/">TecKnologikS</a></p>
    </footer>
  </div>
</body>
</html>
"""


def app_icon(pre):
    """Icône de l'app (générée dans le dépôt de l'app : tools/icon)."""
    return f'        <img class="app-icon" src="{pre}assets/icon-512.png" width="160" height="160" alt="">'


def store_button(lang):
    return f'<a class="button" href="{STORE}">{"Download on the App Store" if lang == "en" else "Télécharger sur l’App Store"}</a>'


HOME = {
    "en": f"""    <main>
      <section class="hero">
{app_icon("")}
        <h1>Every commune,<br>its postal code.</h1>
        <p class="lead">Search any French commune by name, postal code or INSEE code. Get its postal code to copy or share, and the facts that go with it. On iPhone and iPad.</p>
        {store_button('en')}
        <p class="price-note">Free, with a small ad banner. One purchase of {PRICE['en']} removes it.</p>
      </section>

      <section class="features" aria-label="Features">
        <div class="feature"><h3>Search</h3><p>Type a commune name, a postal code or an INSEE code. Recent searches stay one tap away.</p></div>
        <div class="feature"><h3>The commune sheet</h3><p>Postal code to copy or share, population, area, altitude, department, region and a mini map.</p></div>
        <div class="feature"><h3>Explore</h3><p>Browse by region, then department, then communes, without typing anything.</p></div>
        <div class="feature"><h3>Around me</h3><p>Find the commune you are in, and its postal code, from your position.</p></div>
        <div class="feature"><h3>Favorites and history</h3><p>Keep the communes you use often and see the ones you viewed lately. Everything stays on your device.</p></div>
        <div class="feature"><h3>Open in your maps app</h3><p>Send the commune to Apple Maps, Google Maps or Waze in one tap.</p></div>
      </section>

      <section class="pricing" aria-labelledby="pricing-title">
        <h2 id="pricing-title">Free, or ad-free</h2>
        <ul>
          <li><strong>Free:</strong> the whole app, with a single ad banner in the Search tab.</li>
          <li><strong>Premium:</strong> {PRICE['en']}, one-time purchase, no subscription. It removes the ad for good.</li>
          <li>The purchase is handled by the App Store and can be restored at any time from the Premium screen.</li>
        </ul>
      </section>
    </main>""",
    "fr": f"""    <main>
      <section class="hero">
{app_icon("../")}
        <h1>Chaque commune,<br>son code postal.</h1>
        <p class="lead">Recherche n’importe quelle commune française par nom, code postal ou code INSEE. Récupère son code postal à copier ou à partager, avec les informations qui vont avec. Sur iPhone et iPad.</p>
        {store_button('fr')}
        <p class="price-note">Gratuite, avec une petite bannière de pub. Un achat unique à {PRICE['fr']} la retire.</p>
      </section>

      <section class="features" aria-label="Fonctionnalités">
        <div class="feature"><h3>Rechercher</h3><p>Saisis un nom de commune, un code postal ou un code INSEE. Tes recherches récentes restent à portée de main.</p></div>
        <div class="feature"><h3>La fiche de la commune</h3><p>Code postal à copier ou à partager, population, superficie, altitude, département, région et mini-carte.</p></div>
        <div class="feature"><h3>Explorer</h3><p>Parcours par région, puis département, puis communes, sans rien taper.</p></div>
        <div class="feature"><h3>Autour de moi</h3><p>Trouve la commune où tu te trouves, et son code postal, à partir de ta position.</p></div>
        <div class="feature"><h3>Favoris et historique</h3><p>Garde les communes que tu utilises souvent et retrouve celles consultées récemment. Tout reste sur ton appareil.</p></div>
        <div class="feature"><h3>Ouvrir dans ton app de plans</h3><p>Envoie la commune vers Plans, Google Maps ou Waze d’une touche.</p></div>
      </section>

      <section class="pricing" aria-labelledby="pricing-title">
        <h2 id="pricing-title">Gratuite, ou sans pub</h2>
        <ul>
          <li><strong>Gratuit :</strong> toute l’app, avec une seule bannière de pub dans l’onglet Rechercher.</li>
          <li><strong>Premium :</strong> {PRICE['fr']}, achat unique, sans abonnement. Il retire la pub pour de bon.</li>
          <li>L’achat est géré par l’App Store et peut être restauré à tout moment depuis l’écran Premium.</li>
        </ul>
      </section>
    </main>""",
}

ADMOB_ROWS_EN = [
    ("Approximate location (from your IP address)", "Third-party advertising, analytics"),
    ("Device identifiers (advertising identifier, if you allow it, or an app-scoped identifier)", "Third-party advertising, analytics"),
    ("Product interactions (app launches, taps, ad views)", "Third-party advertising, analytics"),
    ("Advertising data (ads you have seen)", "Third-party advertising, analytics"),
    ("Crash logs and performance data", "Diagnostics, analytics"),
]
ADMOB_ROWS_FR = [
    ("Localisation approximative (à partir de l’adresse IP)", "Publicité tierce, mesure d’audience"),
    ("Identifiants de l’appareil (identifiant publicitaire si tu l’autorises, ou un identifiant propre à l’app)", "Publicité tierce, mesure d’audience"),
    ("Interactions (lancements de l’app, touches, annonces vues)", "Publicité tierce, mesure d’audience"),
    ("Données publicitaires (annonces vues)", "Publicité tierce, mesure d’audience"),
    ("Rapports de plantage et données de performance", "Diagnostic, mesure d’audience"),
]


def table(head, rows):
    r = "\n".join(f"          <tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows)
    return f"""<div class="table-wrap"><table>
        <thead><tr><th>{head[0]}</th><th>{head[1]}</th></tr></thead>
        <tbody>
{r}
        </tbody>
      </table></div>"""


PRIVACY = {
    "en": f"""    <main class="doc">
      <h1>Privacy policy</h1>
      <p class="updated">Last updated: {UPDATED['en']}</p>
      <p class="summary"><strong>In short:</strong> Code Postal has no account and no server of its own. Your favorites and history stay on your device, and the commune data is built into the app. The free version shows one ad banner through Google AdMob, which collects data to serve and measure ads, and personalises them only if you agree; Premium users see no ad and no advertising SDK is started for them. The “Around me” tab uses your position only when you open it, does not keep it, and, when online, sends it to the French government’s Géo API to confirm the commune.</p>

      <h2>1. Who is responsible</h2>
      <p>Code Postal and this website are published by TecKnologikS, data controller under the General Data Protection Regulation (GDPR). Contact for any question about your data: <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Data stored on your device</h2>
      <p>Your favorites and your history of viewed communes are stored only on your device, in the app. There is no account, and TecKnologikS has no server that receives them. You can clear the history from the Favorites screen; deleting the app erases everything.</p>

      <h2>3. Commune data</h2>
      <p>The commune data (names, postal codes, INSEE codes, population, area, altitude, departments, regions) is embedded in the app: searching and exploring work without sending anything. It comes from public sources: the postal code database of La Poste, the official geographic code (COG) of INSEE and the Géo API.</p>

      <h2>4. Location (“Around me” tab)</h2>
      <ul>
        <li>The app asks for permission to use your location while you use it. It is used only to find your commune and its postal code.</li>
        <li>Your position is requested once when you open the “Around me” tab, and again if you tap “Locate again”. The app does not track you continuously.</li>
        <li>The position is not stored. A first answer is computed on your device from the embedded data.</li>
        <li>When you are online, your position (latitude and longitude) is then sent to the <a href="https://geo.api.gouv.fr">Géo API</a> of the French State (<code>geo.api.gouv.fr</code>) to confirm the commune and its postal code, and the service receives the technical data of any web request, such as your IP address. If you are offline, nothing is sent. No other service receives your position from the app.</li>
        <li>You can refuse or withdraw the permission in iOS Settings → Privacy &amp; Security → Location Services → Code Postal. Search by name or postal code keeps working.</li>
      </ul>

      <h2>5. Advertising (Google AdMob)</h2>
      <p>The free version shows a single banner, in the Search tab, provided by Google AdMob through the Google Mobile Ads SDK. Premium users see no ad, and for them the consent step and the advertising SDK are not started. The SDK collects the following data:</p>
      {table(('Data', 'Purpose'), ADMOB_ROWS_EN)}
      <p>This data may be used to track you across apps and websites of other companies, only with your permission (see below). Learn more in <a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and in <a href="https://policies.google.com/privacy">Google’s privacy policy</a>.</p>

      <h3>Your consent</h3>
      <ul>
        <li><strong>Where Google’s consent platform requires it (in particular the European Economic Area, the United Kingdom and Switzerland)</strong>, a consent form (Google User Messaging Platform) is shown at launch. You can accept, refuse or choose by purpose. If you refuse, ads may still be shown, without personalisation.</li>
        <li><strong>On iOS</strong>, once ads are allowed, the system asks whether the app may use your advertising identifier (App Tracking Transparency). If you refuse, the advertising identifier is not shared.</li>
      </ul>

      <h2>6. Premium purchase</h2>
      <p>Premium is a one-time purchase handled by Apple (App Store, StoreKit). The payment is processed by Apple under <a href="https://www.apple.com/legal/privacy/">its own privacy policy</a>: the app and TecKnologikS receive no payment data. The app only checks with the App Store whether Premium is active on your Apple Account.</p>

      <h2>7. Service providers</h2>
      {table(('Provider', 'Role'), [
          ("Google LLC / Google Ireland Ltd", "Ads (AdMob) and the consent form (User Messaging Platform), free version only"),
          ("Apple Inc.", "App Store, purchase of Premium, App Tracking Transparency"),
          ("French State (DINUM), Géo API", "Confirmation of the commune from your position (“Around me” tab), only when you are online"),
          ("GitHub, Inc. (United States)", "Hosting of this website (technical connection data such as your IP address)"),
      ])}
      <p>Some providers are located outside the European Union. These transfers are covered by the safeguards provided by the GDPR (in particular the EU–US Data Privacy Framework or standard contractual clauses).</p>

      <h2>8. Legal bases</h2>
      <ul>
        <li>Your consent: personalised ads, the advertising identifier, storing or reading information on your device for advertising, and the use of your position.</li>
        <li>Our legitimate interest: showing non-personalised ads that keep the app free, and measuring and protecting them against fraud.</li>
        <li>The performance of the contract: handling your Premium purchase through Apple.</li>
      </ul>

      <h2>9. How long</h2>
      <ul>
        <li>Favorites and history: on your device, until you remove them or delete the app.</li>
        <li>Position: not kept by the app.</li>
        <li>Advertising data: kept by Google under its own retention rules.</li>
        <li>Data received by the Géo API or by Apple: kept under their own rules.</li>
      </ul>

      <h2 id="changing">10. Changing your choices and deleting your data</h2>
      <ul>
        <li><strong>Consent for ads:</strong> open the Premium screen (tap “Ad-free” under the banner, or the plane button at the top left of the Favorites tab), then tap “Privacy options” to open the consent form again and change or withdraw your choice at any time. This button appears only where Google’s consent platform requires it, and only in the free version.</li>
        <li><strong>Advertising identifier:</strong> iOS Settings → Privacy &amp; Security → Tracking, then turn off Code Postal.</li>
        <li><strong>Location:</strong> iOS Settings → Privacy &amp; Security → Location Services → Code Postal.</li>
        <li><strong>Favorites and history:</strong> remove them in the app, or delete the app.</li>
      </ul>
      <p>TecKnologikS has no account and no user database, so there is nothing else to delete on our side.</p>

      <h2>11. Your rights</h2>
      <p>You have the right to access, rectify, erase, object to, restrict and port your data, and to withdraw your consent. To exercise them, write to <a href="mailto:{MAIL}">{MAIL}</a>. For data held by Google, Apple or the Géo API, you can also contact them directly. You can lodge a complaint with your data protection authority (in France, the CNIL: <a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

      <h2>12. Children</h2>
      <p>TecKnologikS does not knowingly collect personal data from children. Parents can turn off tracking in iOS Settings and refuse personalised ads in the consent form.</p>

      <h2>13. This website</h2>
      <p>This website sets no cookies and loads no third-party resources.</p>

      <h2>14. Changes</h2>
      <p>If this policy changes, the date at the top of the page will be updated.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Politique de confidentialité</h1>
      <p class="updated">Dernière mise à jour : {UPDATED['fr']}</p>
      <p class="summary"><strong>En bref :</strong> Code Postal n’a ni compte ni serveur à lui. Tes favoris et ton historique restent sur ton appareil, et les données des communes sont embarquées dans l’app. La version gratuite affiche une bannière de pub via Google AdMob, qui collecte des données pour diffuser et mesurer les annonces, et ne les personnalise que si tu es d’accord ; avec Premium, aucune pub et aucun SDK publicitaire n’est démarré. L’onglet « Autour de moi » utilise ta position seulement quand tu l’ouvres, ne la conserve pas et, en ligne, l’envoie à l’API Géo de l’État pour confirmer la commune.</p>

      <h2>1. Responsable du traitement</h2>
      <p>Code Postal et ce site sont édités par TecKnologikS, responsable du traitement au sens du Règlement général sur la protection des données (RGPD). Contact pour toute question sur tes données : <a href="mailto:{MAIL}">{MAIL}</a>.</p>

      <h2>2. Données stockées sur ton appareil</h2>
      <p>Tes favoris et ton historique de communes consultées sont stockés uniquement sur ton appareil, dans l’app. Il n’y a pas de compte, et TecKnologikS n’a aucun serveur qui les reçoive. Tu peux vider l’historique depuis l’écran Favoris ; supprimer l’app efface tout.</p>

      <h2>3. Données des communes</h2>
      <p>Les données des communes (noms, codes postaux, codes INSEE, population, superficie, altitude, départements, régions) sont embarquées dans l’app : la recherche et l’exploration fonctionnent sans rien envoyer. Elles proviennent de sources publiques : la base des codes postaux de La Poste, le code officiel géographique (COG) de l’INSEE et l’API Géo.</p>

      <h2>4. Localisation (onglet « Autour de moi »)</h2>
      <ul>
        <li>L’app demande l’autorisation d’utiliser ta position pendant que tu l’utilises. Elle sert uniquement à trouver ta commune et son code postal.</li>
        <li>Ta position est demandée une fois à l’ouverture de l’onglet « Autour de moi », et de nouveau si tu touches « Relancer la localisation ». L’app ne te suit pas en continu.</li>
        <li>La position n’est pas enregistrée. Une première réponse est calculée sur ton appareil à partir des données embarquées.</li>
        <li>Quand tu es en ligne, ta position (latitude et longitude) est ensuite envoyée à l’<a href="https://geo.api.gouv.fr">API Géo</a> de l’État (<code>geo.api.gouv.fr</code>) pour confirmer la commune et son code postal, et ce service reçoit les données techniques de toute requête web, comme ton adresse IP. Hors ligne, rien n’est envoyé. Aucun autre service ne reçoit ta position depuis l’app.</li>
        <li>Tu peux refuser ou retirer l’autorisation dans Réglages iOS → Confidentialité et sécurité → Service de localisation → Code Postal. La recherche par nom ou code postal continue de fonctionner.</li>
      </ul>

      <h2>5. Publicité (Google AdMob)</h2>
      <p>La version gratuite affiche une seule bannière, dans l’onglet Rechercher, fournie par Google AdMob via le SDK Google Mobile Ads. Avec Premium, aucune pub n’est affichée, et ni l’étape de consentement ni le SDK publicitaire ne sont démarrés. Le SDK collecte les données suivantes :</p>
      {table(('Donnée', 'Finalité'), ADMOB_ROWS_FR)}
      <p>Ces données peuvent servir à te suivre sur les apps et sites d’autres sociétés, uniquement avec ton accord (voir ci-dessous). Pour en savoir plus : <a href="https://policies.google.com/technologies/partner-sites?hl=fr">Comment Google utilise les informations des sites ou applications qui utilisent ses services</a> et <a href="https://policies.google.com/privacy?hl=fr">les règles de confidentialité de Google</a>.</p>

      <h3>Ton consentement</h3>
      <ul>
        <li><strong>Là où la plateforme de consentement de Google l’exige (notamment l’Espace économique européen, le Royaume-Uni et la Suisse)</strong>, un formulaire de consentement (Google User Messaging Platform) s’affiche au lancement. Tu peux accepter, refuser ou choisir finalité par finalité. Si tu refuses, des pubs peuvent quand même s’afficher, sans personnalisation.</li>
        <li><strong>Sur iOS</strong>, une fois les pubs autorisées, le système demande si l’app peut utiliser ton identifiant publicitaire (App Tracking Transparency). Si tu refuses, l’identifiant publicitaire n’est pas partagé.</li>
      </ul>

      <h2>6. Achat Premium</h2>
      <p>Premium est un achat unique géré par Apple (App Store, StoreKit). Le paiement est traité par Apple selon <a href="https://www.apple.com/fr/legal/privacy/">sa propre politique de confidentialité</a> : l’app et TecKnologikS ne reçoivent aucune donnée de paiement. L’app vérifie seulement auprès de l’App Store si Premium est actif sur ton compte Apple.</p>

      <h2>7. Prestataires</h2>
      {table(('Prestataire', 'Rôle'), [
          ("Google LLC / Google Ireland Ltd", "Publicité (AdMob) et formulaire de consentement (User Messaging Platform), version gratuite uniquement"),
          ("Apple Inc.", "App Store, achat de Premium, App Tracking Transparency"),
          ("État français (DINUM), API Géo", "Confirmation de la commune à partir de ta position (onglet « Autour de moi »), seulement en ligne"),
          ("GitHub, Inc. (États-Unis)", "Hébergement de ce site (données techniques de connexion, comme l’adresse IP)"),
      ])}
      <p>Certains prestataires sont situés hors de l’Union européenne. Ces transferts sont encadrés par les garanties prévues par le RGPD (notamment le Data Privacy Framework UE–États-Unis ou des clauses contractuelles types).</p>

      <h2>8. Bases légales</h2>
      <ul>
        <li>Ton consentement : publicité personnalisée, identifiant publicitaire, stockage ou lecture d’informations sur ton appareil à des fins publicitaires, et utilisation de ta position.</li>
        <li>Notre intérêt légitime : afficher des pubs non personnalisées qui gardent l’app gratuite, les mesurer et les protéger contre la fraude.</li>
        <li>L’exécution du contrat : traiter ton achat Premium via Apple.</li>
      </ul>

      <h2>9. Durées de conservation</h2>
      <ul>
        <li>Favoris et historique : sur ton appareil, jusqu’à ce que tu les retires ou supprimes l’app.</li>
        <li>Position : non conservée par l’app.</li>
        <li>Données publicitaires : conservées par Google selon ses propres règles.</li>
        <li>Données reçues par l’API Géo ou par Apple : conservées selon leurs propres règles.</li>
      </ul>

      <h2 id="changer">10. Changer tes choix et supprimer tes données</h2>
      <ul>
        <li><strong>Consentement pour la publicité :</strong> ouvre l’écran Premium (touche « Sans pub » sous la bannière, ou le bouton en forme d’avion en haut à gauche de l’onglet Favoris), puis touche « Options de confidentialité » pour rouvrir le formulaire et modifier ou retirer ton choix à tout moment. Ce bouton n’apparaît que là où la plateforme de consentement de Google l’exige, et seulement dans la version gratuite.</li>
        <li><strong>Identifiant publicitaire :</strong> Réglages iOS → Confidentialité et sécurité → Suivi, puis désactive Code Postal.</li>
        <li><strong>Localisation :</strong> Réglages iOS → Confidentialité et sécurité → Service de localisation → Code Postal.</li>
        <li><strong>Favoris et historique :</strong> retire-les dans l’app, ou supprime l’app.</li>
      </ul>
      <p>TecKnologikS n’a ni compte ni base d’utilisateurs : il n’y a rien d’autre à supprimer de notre côté.</p>

      <h2>11. Tes droits</h2>
      <p>Tu disposes d’un droit d’accès, de rectification, d’effacement, d’opposition, de limitation et de portabilité, ainsi que du droit de retirer ton consentement. Pour les exercer, écris à <a href="mailto:{MAIL}">{MAIL}</a>. Pour les données détenues par Google, Apple ou l’API Géo, tu peux aussi les contacter directement. Tu peux introduire une réclamation auprès de la CNIL : <a href="https://www.cnil.fr">www.cnil.fr</a>.</p>

      <h2>12. Enfants</h2>
      <p>TecKnologikS ne collecte sciemment aucune donnée personnelle d’enfants. Les parents peuvent désactiver le suivi dans les Réglages iOS et refuser la publicité personnalisée dans le formulaire de consentement.</p>

      <h2>13. Ce site</h2>
      <p>Ce site ne dépose aucun cookie et ne charge aucune ressource tierce.</p>

      <h2>14. Modifications</h2>
      <p>Si cette politique change, la date en haut de la page sera mise à jour.</p>
    </main>""",
}

SUPPORT = {
    "en": f"""    <main class="doc">
      <h1>Support</h1>
      <p>A question, a bug, a wrong postal code? Write to <a href="mailto:{MAIL}">{MAIL}</a>. Tell us your iPhone or iPad model and iOS version if something goes wrong.</p>

      <h2>Frequently asked questions</h2>
      <h3>How do I restore my Premium purchase?</h3>
      <p>Open the Premium screen (tap “Ad-free” under the banner, or the plane button at the top left of the Favorites tab) and tap “Restore purchases”, signed in with the same Apple Account as for the purchase. Premium also restores on your other devices signed in with that account.</p>
      <h3>How do I change or withdraw my ad consent?</h3>
      <p>On the Premium screen, tap “Privacy options” to open the consent form again. The button appears only where Google’s consent platform requires it (in particular in the European Economic Area, the United Kingdom and Switzerland). To turn off ad tracking, go to iOS Settings → Privacy &amp; Security → Tracking. See also <a href="privacy.html#changing">“Changing your choices” in the privacy policy</a>.</p>
      <h3>“Around me” says Location is off</h3>
      <p>Allow Code Postal to use your location: tap “Open Settings” in the app, or go to iOS Settings → Privacy &amp; Security → Location Services → Code Postal. Searching by name or postal code works without it. If your position cannot be determined, check that Location Services are on, then try again.</p>
      <h3>A commune, a postal code or a figure looks wrong</h3>
      <p>The commune data is built into the app from public sources (La Poste, INSEE, Géo API) and is updated with new versions of the app. To report an error, write to <a href="mailto:{MAIL}">{MAIL}</a> with the commune name, its INSEE code if you know it, and what you expected.</p>
      <h3>Where are my favorites?</h3>
      <p>Favorites and history are stored only on your device. They are not synchronised and not transferred to a new device.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Support</h1>
      <p>Une question, un bug, un code postal erroné ? Écris à <a href="mailto:{MAIL}">{MAIL}</a>. Si quelque chose ne marche pas, indique ton modèle d’iPhone ou d’iPad et ta version d’iOS.</p>

      <h2>Questions fréquentes</h2>
      <h3>Comment restaurer mon achat Premium ?</h3>
      <p>Ouvre l’écran Premium (touche « Sans pub » sous la bannière, ou le bouton en forme d’avion en haut à gauche de l’onglet Favoris) et touche « Restaurer les achats », avec le même compte Apple que pour l’achat. Premium se restaure aussi sur tes autres appareils connectés à ce compte.</p>
      <h3>Comment modifier ou retirer mon consentement pour les pubs ?</h3>
      <p>Sur l’écran Premium, touche « Options de confidentialité » pour rouvrir le formulaire de consentement. Le bouton n’apparaît que là où la plateforme de consentement de Google l’exige (notamment dans l’Espace économique européen, au Royaume-Uni et en Suisse). Pour désactiver le suivi publicitaire, va dans Réglages iOS → Confidentialité et sécurité → Suivi. Voir aussi <a href="confidentialite.html#changer">« Changer tes choix » dans la politique de confidentialité</a>.</p>
      <h3>« Autour de moi » indique Localisation désactivée</h3>
      <p>Autorise Code Postal à utiliser ta position : touche « Ouvrir les Réglages » dans l’app, ou va dans Réglages iOS → Confidentialité et sécurité → Service de localisation → Code Postal. La recherche par nom ou code postal fonctionne sans. Si ta position reste introuvable, vérifie que les services de localisation sont activés, puis réessaie.</p>
      <h3>Une commune, un code postal ou un chiffre semble faux</h3>
      <p>Les données des communes sont embarquées dans l’app à partir de sources publiques (La Poste, INSEE, API Géo) et mises à jour avec les nouvelles versions de l’app. Pour signaler une erreur, écris à <a href="mailto:{MAIL}">{MAIL}</a> avec le nom de la commune, son code INSEE si tu le connais, et ce que tu attendais.</p>
      <h3>Où sont mes favoris ?</h3>
      <p>Les favoris et l’historique sont stockés uniquement sur ton appareil. Ils ne sont pas synchronisés ni transférés sur un nouvel appareil.</p>
    </main>""",
}

LEGAL = {
    "en": f"""    <main class="doc">
      <h1>Legal notice</h1>
      <h2>Publisher</h2>
      <p>TecKnologikS<br>Contact: <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Publication director: TecKnologikS</p>
      <h2>Website hosting</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States — <a href="https://github.com">github.com</a>.</p>
      <h2>Intellectual property</h2>
      <p>The texts, visuals and code of Code Postal are the property of the publisher. The Barlow Condensed font is used under the SIL Open Font License 1.1.</p>
      <p>App Store and Apple Maps are trademarks of Apple Inc.; Google, Google Maps and AdMob are trademarks of Google LLC; Waze is a trademark of Waze Ltd. Code Postal is neither affiliated with nor endorsed by these companies.</p>
      <h2>Personal data</h2>
      <p>See the <a href="privacy.html">privacy policy</a>. This website sets no cookies.</p>
    </main>""",
    "fr": f"""    <main class="doc">
      <h1>Mentions légales</h1>
      <h2>Éditeur</h2>
      <p>TecKnologikS<br>Contact : <a href="mailto:{MAIL}">{MAIL}</a></p>
      <p>Directeur de la publication : TecKnologikS</p>
      <h2>Hébergement du site</h2>
      <p>GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — <a href="https://github.com">github.com</a>.</p>
      <h2>Propriété intellectuelle</h2>
      <p>Les textes, visuels et le code de Code Postal sont la propriété de l’éditeur. La police Barlow Condensed est utilisée sous licence SIL Open Font License 1.1.</p>
      <p>App Store et Plans sont des marques d’Apple Inc. ; Google, Google Maps et AdMob sont des marques de Google LLC ; Waze est une marque de Waze Ltd. Code Postal n’est ni affilié à ces sociétés ni approuvé par elles.</p>
      <h2>Données personnelles</h2>
      <p>Voir la <a href="confidentialite.html">politique de confidentialité</a>. Ce site ne dépose aucun cookie.</p>
    </main>""",
}

META = {
    "home": {"en": ("Code Postal — every French commune, its postal code", "Search any French commune by name, postal code or INSEE code. Postal code to copy or share, population, area, altitude, map. Free on iPhone and iPad."),
             "fr": ("Code Postal — chaque commune française, son code postal", "Recherche une commune française par nom, code postal ou code INSEE. Code postal à copier ou partager, population, superficie, altitude, carte. Gratuit sur iPhone et iPad.")},
    "privacy": {"en": ("Privacy policy — Code Postal", "How Code Postal handles your data: favorites on your device, Google AdMob ads and consent, location, Premium purchase."),
                "fr": ("Politique de confidentialité — Code Postal", "Comment Code Postal traite tes données : favoris sur ton appareil, pubs et consentement Google AdMob, localisation, achat Premium.")},
    "support": {"en": ("Support — Code Postal", "Contact and frequently asked questions."),
                "fr": ("Support — Code Postal", "Contact et questions fréquentes.")},
    "legal": {"en": ("Legal notice — Code Postal", "Publisher and hosting of the Code Postal website."),
              "fr": ("Mentions légales — Code Postal", "Éditeur et hébergeur du site de Code Postal.")},
}

BODIES = {"home": HOME, "privacy": PRIVACY, "support": SUPPORT, "legal": LEGAL}

(OUT / "fr").mkdir(parents=True, exist_ok=True)
for lang in ("en", "fr"):
    for page, bodies in BODIES.items():
        title, desc = META[page][lang]
        path = OUT / PAGES[lang][page] if lang == "en" else OUT / "fr" / PAGES[lang][page]
        path.write_text(render(lang, page, title, desc, bodies[lang]), encoding="utf-8")
        print("wrote", path.relative_to(OUT))
