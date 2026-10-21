import os, re, shutil, html

HERE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://zeroonemany.com"
CONTACT_REV = "moc.ynamenoorez@tcatnoc"   # contact address, stored reversed on purpose (anti scraping)
LINKEDIN = "https://www.linkedin.com/in/rigaudnicolas"
BOOKING = "https://meetings-eu1.hubspot.com/rigaud"   # HubSpot scheduling page; empty = placeholder
SHOW_PRICES = False                   # prices hidden for now
SHOW_LEGAL = False                    # legal notice pages paused for now
PHOTO = os.path.join(HERE, "assets", "nicolas.jpg")


def nb(s):
    """French typography: non-breaking space before : ; % € ! ? and inside guillemets."""
    s = re.sub(r" ([:;%€!?])", r"&nbsp;\1", s)
    s = s.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
    return s


def todo(s):
    return ("TODO", s)


FR = dict(
    lang="fr",
    title="Nicolas Rigaud, consultant marketing et ops B2B | Zero One Many",
    desc="Consultant marketing et ops B2B pour la tech et l'industrie : positionnement, création de la demande, CRM, automatisation, pilotage. Diagnostic, mission ou direction à temps partagé. Paris et à distance.",
    job="Consultant marketing et ops B2B",
    skip="Aller au contenu",
    nav=[("#expertises", "Expertises"), ("#offres", "Offres"), ("#partenaires", "Agences et fonds"), ("#resultats", "Résultats"), ("#contact", "Contact")],
    other_label="EN", other_name="English",
    eyebrow="consultant Marketing et Ops B2B pour tech et industrie",
    h1="Un moteur commercial qui tourne, de la demande au pilotage.",
    lede="J'aide les dirigeants et les équipes commerciales et marketing d'entreprises B2B à générer un pipeline régulier et à piloter leur chiffre d'affaires.",
    cta="Réserver un appel de 30 min", cta2="Voir les offres",
    figs_h="Résultats obtenus en poste",
    figs=[("1 M€", "d'ARR ajouté", "Bonitasoft"),
          ("3 M€", "d'ARR sur de nouveaux segments", "Streamdata.io"),
          ("90 à 30 jours", "durée du cycle de vente", "United Robotics Group"),
          ("50 000", "membres dans la communauté", "SoftBank Robotics Europe")],
    figs_more="Le détail",
    exp_h="Ce sur quoi j'interviens",
    exp=[
        ("Stratégie", ["Positionnement et message", "Segmentation, cible et offre", "Passage du PLG au SLG", "Plan marketing et commercial"]),
        ("Création de la demande", ["Campagnes et contenus", "Inbound : signaux d'intention, SEO", "Webinars et événements physiques", "Salons professionnels", "Partner enablement et co-marketing"]),
        ("Opérations et pilotage", ["Alignement marketing, ventes et customer success", "CRM et entonnoir commun", "Scoring, prévisions et tableaux de bord", "Automatisation et IA"]),
    ],
    offers_h="Travailler ensemble",
    offers_intro="Si vous ne savez pas par où commencer, commencez par le diagnostic.",
    inc_label="Inclus",
    book_short="Réserver un appel",
    offers=[
        dict(name="Diagnostic", tag="Un regard extérieur sur votre moteur commercial, et par quoi commencer.",
             price=("TODO", "À partir de … € HT"),
             inc=["Entretiens avec le marketing, les ventes et le customer success",
                  "Revue du CRM, de l'entonnoir et des chiffres",
                  "Lecture du positionnement face aux alternatives",
                  "Plan d'action priorisé, présenté à la direction"]),
        dict(name="Mission", tag="Un chantier précis, construit avec vos équipes et adopté par elles.",
             price=("TODO", "À partir de … € HT"),
             inc=["Reprise ou refonte d'un portail HubSpot",
                  "Passage du PLG au SLG",
                  "Programme de webinars, salon ou événement",
                  "Formation des équipes et passation"]),
        dict(name="Direction marketing et ops à temps partagé", tag="Je pilote et j'exécute avec vos équipes, sans recrutement à temps plein.",
             price=("TODO", "À partir de … € HT par mois"),
             inc=["Diagnostic de départ",
                  "Stratégie, plan et budget",
                  "Exécution : CRM, campagnes, événements",
                  "Pilotage des équipes et des prestataires",
                  "Un point chaque semaine, un rapport chaque mois"]),
    ],
    part_h="Agences, fonds et incubateurs",
    part_intro="Je travaille aussi avec ceux qui accompagnent les entreprises B2B.",
    part=[
        ("Agences", "Vos clients vous demandent de la stratégie, du RevOps ou de l'événementiel que vous n'avez pas en interne.",
         ["Renfort senior sur vos comptes, en sous-traitance", "Cadrage stratégique, CRM et automatisation, dispositifs terrain", "Avec vos équipes, sous votre pilotage"]),
        ("Fonds d'investissement", "Vos participations ont un bon produit et bloquent sur la vente.",
         ["Diagnostic du moteur commercial de vos participations", "Accompagnement en mission ou à temps partagé", "Un même interlocuteur pour plusieurs sociétés du portefeuille"]),
        ("Incubateurs et accélérateurs", "Vos startups doivent trouver leurs premiers clients, vite.",
         ["Ateliers collectifs : positionnement, premiers canaux, CRM", "Sessions individuelles avec les fondateurs", "Un programme adapté au stade de chaque startup"]),
    ],
    part_cta="Parlons-en",
    proof_h="Ce que j'ai déjà construit",
    proof=[
        dict(co="United Robotics Group", role="Senior Director Sales & Marketing Operations", per="2022 à 2026",
             what="Neuf entreprises de robotique rachetées en Europe et aux États-Unis, aucune infrastructure commerciale commune. Alignement du marketing, des ventes et du customer success, digitalisation de l'acquisition en ligne et hors ligne, scoring, méthode de prévision, automatisation et tableaux de bord, sur une seule instance HubSpot pour plus de 60 personnes.",
             res=[("3 jours à 4 heures", "délai de réponse aux leads"), ("+800 %", "conversion MQL vers pipeline"), ("90 à 30 jours", "durée du cycle de vente")]),
        dict(co="Bonitasoft", role="Demand Generation Director", per="2019 à 2022",
             what="Une communauté open source forte, mais peu de contrats entreprise. Un dispositif de création de la demande sans publicité : signaux d'intention d'achat, SEO technique, webinaire sectoriel chaque semaine, partner enablement et co-marketing, automatisation.",
             res=[("1 M€", "d'ARR ajouté"), ("+130 %", "pipeline entrant")]),
        dict(co="Streamdata.io", role="VP Marketing & Partners", per="2017 à 2018",
             what="Seul responsable marketing, rattaché au CEO. Repositionnement d'un outil développeur en libre service vers une vente entreprise, et distribution via les marketplaces AWS, Google Cloud et Azure.",
             res=[("3 M€", "d'ARR sur de nouveaux segments"), ("+120 %", "revenu des canaux")]),
        dict(co="SoftBank Robotics Europe", role="Head of Developer Marketing", per="2012 à 2017",
             what="Faire de NAO et Pepper des plateformes sur lesquelles des développeurs bâtissent des usages métiers : plus de 80 conférences et ateliers sur trois continents.",
             res=[("50 000", "membres dans la communauté"), ("50+", "applications commerciales")]),
    ],
    method_h="Comment je construis un moteur commercial",
    method_order="L'ordre compte : on n'automatise pas un processus que personne n'a adopté.",
    method=[
        ("Des processus clairs, que les équipes adoptent.", "chacun sait quoi faire à chaque étape, et le fait."),
        ("Un langage commun entre marketing, ventes et customer success.", "un lead, une opportunité, un client veulent dire la même chose pour tous."),
        ("Des actions digitalisées, sur des outils qui soutiennent les processus.", "des données analysables, qui montrent où ça marche et où ça casse."),
        ("De l'automatisation et de l'IA pour remplacer les tâches à faible valeur ajoutée.", "un rythme plus rapide, et du temps rendu aux équipes pour ce qui demande du jugement."),
    ],
    method_for="Pour vous : ",
    about_h="À propos de moi",
    about=[
        "Quinze ans dans des entreprises où le mode d'emploi commercial n'existait pas encore : logiciel, robotique, outils pour développeurs. J'y ai dirigé le marketing, la génération de demande et les opérations commerciales, de la startup en amorçage au groupe industriel aux multiples entreprises et marchés.",
        "Je construis moi-même ce que je recommande, dans le CRM comme dans les process. Depuis Paris, sur place ou à distance, en français et en anglais.",
    ],
    linkedin="Profil LinkedIn (en anglais)",
    photo_alt="Nicolas Rigaud",
    contact_h="Parlons de votre situation.",
    contact_note="Un premier appel de 30 minutes, gratuit, en visio. Vous me dites où vous en êtes, je vous dis si je peux aider et sous quelle forme.",
    book="Réserver un appel",
    book_todo="Lien de réservation à créer",
    reveal="Afficher l'adresse e-mail", copy="Copier", copied="Copié",
    mail_subject="Prise de contact",
    noscript="contact [at] zeroonemany [point] com",
    legal="Mentions légales", legal_file="mentions-legales.html",
    rights="© 2026 Nicolas Rigaud",
)

EN = dict(
    lang="en",
    title="Nicolas Rigaud, B2B marketing and ops consultant | Zero One Many",
    desc="B2B marketing and ops consultant for tech and industry: positioning, demand creation, CRM, automation, revenue steering. Assessment, project or fractional marketing and ops lead. Paris and remote.",
    job="B2B marketing and ops consultant",
    skip="Skip to content",
    nav=[("#expertise", "Expertise"), ("#offers", "Offers"), ("#partners", "Agencies and funds"), ("#results", "Results"), ("#contact", "Contact")],
    other_label="FR", other_name="Français",
    eyebrow="B2B Marketing and Ops consultant for tech and industry",
    h1="A revenue engine that runs, from demand to forecast.",
    lede="I help leaders and sales and marketing teams at B2B companies build a steady pipeline and steer their revenue.",
    cta="Book a 30 min call", cta2="See the offers",
    figs_h="Results delivered in house",
    figs=[("€1M", "ARR added", "Bonitasoft"),
          ("€3M", "ARR from new segments", "Streamdata.io"),
          ("90 to 30 days", "sales cycle length", "United Robotics Group"),
          ("50,000", "community members", "SoftBank Robotics Europe")],
    figs_more="The detail",
    exp_h="What I work on",
    exp=[
        ("Strategy", ["Positioning and messaging", "Segmentation, target and offer", "Move from PLG to SLG", "Marketing and sales plan"]),
        ("Demand creation", ["Campaigns and content", "Inbound: intent signals, SEO", "Webinars and physical events", "Trade shows", "Partner enablement and co-marketing"]),
        ("Operations and steering", ["Marketing, sales and customer success alignment", "CRM and shared funnel", "Scoring, forecasting and dashboards", "Automation and AI"]),
    ],
    offers_h="Work together",
    offers_intro="If you don't know where to start, start with the assessment.",
    inc_label="Includes",
    book_short="Book a call",
    offers=[
        dict(name="Assessment", tag="An outside look at your revenue engine, and where to start.",
             price=("TODO", "Starting at … € excl. VAT"),
             inc=["Interviews with marketing, sales and customer success",
                  "Review of the CRM, the funnel and the numbers",
                  "Read of your positioning against the alternatives",
                  "Prioritized action plan, presented to leadership"]),
        dict(name="Project", tag="One defined build, done with your teams and adopted by them.",
             price=("TODO", "Starting at … € excl. VAT"),
             inc=["HubSpot portal takeover or rebuild",
                  "Move from PLG to SLG",
                  "Webinar program, trade show or event",
                  "Team training and handover"]),
        dict(name="Fractional marketing and ops lead", tag="I lead and execute with your teams, without a full time hire.",
             price=("TODO", "Starting at … € excl. VAT per month"),
             inc=["Initial assessment",
                  "Strategy, plan and budget",
                  "Execution: CRM, campaigns, events",
                  "Steering of teams and vendors",
                  "A weekly check in, a monthly report"]),
    ],
    part_h="Agencies, funds and incubators",
    part_intro="I also work with those who support B2B companies.",
    part=[
        ("Agencies", "Your clients ask for strategy, RevOps or events you don't have in house.",
         ["Senior backup on your accounts, as a subcontractor", "Strategy framing, CRM and automation, field programs", "With your teams, under your lead"]),
        ("Investment funds", "Your portfolio companies have a good product and get stuck on sales.",
         ["Revenue engine assessment of your portfolio companies", "Support as a project or fractional lead", "One contact for several portfolio companies"]),
        ("Incubators and accelerators", "Your startups need their first customers, fast.",
         ["Group workshops: positioning, first channels, CRM", "One to one sessions with founders", "A program fitted to each startup's stage"]),
    ],
    part_cta="Let's talk",
    proof_h="What I have already built",
    proof=[
        dict(co="United Robotics Group", role="Senior Director Sales & Marketing Operations", per="2022 to 2026",
             what="Nine robotics companies acquired across Europe and the US, with no shared commercial infrastructure. Marketing, sales and customer success alignment, digitized acquisition online and offline, lead scoring, forecast method, automation and dashboards, on a single HubSpot instance for 60+ people.",
             res=[("3 days to 4 hours", "lead response time"), ("+800%", "MQL to pipeline conversion"), ("90 to 30 days", "sales cycle length")]),
        dict(co="Bonitasoft", role="Demand Generation Director", per="2019 to 2022",
             what="A strong open source community, but few enterprise contracts. A demand creation program with no ads: buying intent signals, technical SEO, a weekly industry webinar, partner enablement and co-marketing, automation.",
             res=[("€1M", "ARR added"), ("+130%", "inbound pipeline")]),
        dict(co="Streamdata.io", role="VP Marketing & Partners", per="2017 to 2018",
             what="Sole marketing leader, reporting to the CEO. Repositioned a self-serve developer tool toward enterprise sales, and drove distribution through the AWS, Google Cloud and Azure marketplaces.",
             res=[("€3M", "ARR from new market segments"), ("+120%", "channel revenue")]),
        dict(co="SoftBank Robotics Europe", role="Head of Developer Marketing", per="2012 to 2017",
             what="Turning NAO and Pepper into platforms where developers build business use cases: 80+ talks and workshops across three continents.",
             res=[("50,000", "community members"), ("50+", "commercial applications")]),
    ],
    method_h="How I build a revenue engine",
    method_order="Order matters: we don't automate a process nobody has adopted.",
    method=[
        ("Clear processes that teams actually adopt.", "everyone knows what to do at each step, and does it."),
        ("A common language across marketing, sales and customer success.", "a lead, an opportunity, a customer mean the same thing to everyone."),
        ("Digitized actions, on tools that support the processes.", "analyzable data that shows where it works and where it breaks."),
        ("Automation and AI to replace low-value tasks.", "a faster pace, and time given back to the team for what needs judgment."),
    ],
    method_for="For you: ",
    about_h="About me",
    about=[
        "Fifteen years in companies where the commercial playbook did not exist yet: software, robotics, developer tools. I led marketing, demand generation and sales operations there, from a seed stage startup to an industrial group spanning many companies and markets.",
        "I build what I recommend myself, in the CRM as much as in the processes. Based in Paris, on site or remote, in French and English.",
    ],
    linkedin="LinkedIn profile",
    photo_alt="Nicolas Rigaud",
    contact_h="Let's talk about where you are.",
    contact_note="A first 30 minute video call, free. You tell me where you are, I tell you whether I can help and in what form.",
    book="Book a call",
    book_todo="Booking link to create",
    reveal="Show email address", copy="Copy", copied="Copied",
    mail_subject="Getting in touch",
    noscript="contact [at] zeroonemany [dot] com",
    legal="Legal notice", legal_file="legal-notice.html",
    rights="© 2026 Nicolas Rigaud",
)

SCRIPT = """<script>
(function(){
  var box=document.getElementById('mail-box'),btn=document.getElementById('reveal');
  if(!box||!btn)return;
  var s=box.getAttribute('data-p').split('').reverse().join('');
  btn.hidden=false;
  function sel(el){var r=document.createRange();r.selectNodeContents(el);var g=window.getSelection();g.removeAllRanges();g.addRange(r);}
  btn.addEventListener('click',function(){
    var a=document.createElement('a');a.className='mail';a.href='mailto:'+s+'?subject='+encodeURIComponent(box.getAttribute('data-s'));a.textContent=s;
    var c=document.createElement('button');c.type='button';c.className='copy';c.textContent=box.getAttribute('data-copy');
    c.addEventListener('click',function(){
      var done=function(){c.textContent=box.getAttribute('data-copied');};
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(s).then(done,function(){sel(a);});}else{sel(a);}
    });
    box.textContent='';box.appendChild(a);box.appendChild(c);a.focus();
  });
})();
</script>"""


def page(c, is_en, suffix):
    pre = "../" if is_en else ""
    t0 = (lambda s: s) if is_en else nb

    def t(s):
        if isinstance(s, tuple):
            return f'<span class="todo">{t0(s[1])}</span>'
        return t0(s)

    canon = f"{DOMAIN}/en/" if is_en else f"{DOMAIN}/"
    other_href = ("../" + suffix if suffix else "../") if is_en else "en/" + suffix
    home_href = "index.html" if suffix else "./"
    ids = [h[1:] for h, _ in c["nav"]]  # expertises, offres, partenaires, resultats, contact
    nav = "".join(f'<a href="{h}">{html.escape(l)}</a>' for h, l in c["nav"][:-1])
    nav += f'<a class="nav-contact" href="{c["nav"][-1][0]}">{c["nav"][-1][1]}</a>'
    nav += (f'<a class="lang" href="{other_href}" hreflang="{"fr" if is_en else "en"}" '
            f'lang="{"fr" if is_en else "en"}" title="{c["other_name"]}">{c["other_label"]}</a>')

    book_href = BOOKING or "#contact"
    ext = ' rel="noopener"' if BOOKING else ""

    figs = "".join(f'<li><span class="fig">{t(f)}</span><span class="fig-l">{t(l)}</span><span class="fig-co">{co}</span></li>'
                   for f, l, co in c["figs"])

    exp = "".join(f'<li class="exp-col"><h3>{t(h)}</h3><ul class="ticks">' + "".join(f"<li>{t(x)}</li>" for x in items) + "</ul></li>"
                  for h, items in c["exp"])

    offers = ""
    for o in c["offers"]:
        inc = "".join(f"<li>{t(x)}</li>" for x in o["inc"])
        offers += (f'<li class="offer"><h3>{t(o["name"])}</h3><p class="offer-tag">{t(o["tag"])}</p>'
                   + (f'<p class="price">{t(o["price"])}</p>' if SHOW_PRICES else '') +
                   f'<p class="lbl">{t(c["inc_label"])}</p><ul class="ticks">{inc}</ul>'
                   f'<a class="btn offer-cta" href="{book_href}"{ext}>{c["book_short"]}</a></li>')

    part = "".join(f'<li class="part-col"><h3>{t(h)}</h3><p class="part-pain">{t(p)}</p><ul class="ticks">'
                   + "".join(f"<li>{t(x)}</li>" for x in items) + "</ul></li>"
                   for h, p, items in c["part"])

    rows = ""
    for r in c["proof"]:
        res = "".join(f'<li><span class="fig">{t(f)}</span><span>{t(l)}</span></li>' for f, l in r["res"])
        rows += (f'<li class="row"><div class="who"><h3>{r["co"]}</h3><p>{r["role"]}<br>{r["per"]}</p></div>'
                 f'<p class="what">{t(r["what"])}</p><ul class="res">{res}</ul></li>')

    steps = "".join(f'<li><strong>{t(h)}</strong><span>{c["method_for"]}{t(p)}</span></li>' for h, p in c["method"])
    about = "".join(f"<p>{t(p)}</p>" for p in c["about"])
    portrait = ""
    if os.path.exists(PHOTO):
        portrait = f'<figure class="portrait"><img src="{pre}assets/nicolas.jpg" alt="{c["photo_alt"]}" width="320" height="400"></figure>'
    rev = CONTACT_REV
    legal_link = f'<a href="{c["legal_file"]}">{c["legal"]}</a>' if SHOW_LEGAL else ""
    book_note = "" if BOOKING else f' <span class="todo">{c["book_todo"]}</span>'

    return f"""<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(c['title'])}</title>
<meta name="description" content="{html.escape(c['desc'])}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="fr" href="{DOMAIN}/">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(c['title'])}">
<meta property="og:description" content="{html.escape(c['desc'])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/assets/og.png">
<meta property="og:locale" content="{'en_GB' if is_en else 'fr_FR'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#111111">
<link rel="icon" href="{pre}favicon.ico" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="{pre}assets/mark.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{pre}assets/apple-touch-icon.png">
<link rel="preload" href="{pre}assets/fonts/InterDisplay-SemiBold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pre}assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Person","name":"Nicolas Rigaud","url":"{canon}","jobTitle":"{c['job']}","sameAs":["{LINKEDIN}"],"address":{{"@type":"PostalAddress","addressLocality":"Paris","addressCountry":"FR"}}}}</script>
</head>
<body>
<a class="skip" href="#main">{c['skip']}</a>
<header class="wrap site-header">
  <a class="brand" href="{home_href}"><img src="{pre}assets/mark.svg" alt="" width="40" height="40"><span>Zero One Many</span></a>
  <nav class="nav" aria-label="Navigation">{nav}</nav>
</header>
<main id="main">
  <section class="wrap hero">
    <span class="bar" aria-hidden="true"></span>
    <p class="eyebrow"><strong>Nicolas Rigaud</strong>, {t(c['eyebrow'])}</p>
    <h1>{t(c['h1'])}</h1>
    <p class="lede">{t(c['lede'])}</p>
    <div class="cta-row">
      <a class="btn" href="{book_href}"{ext}>{c['cta']}</a>
      <a class="link" href="#{ids[1]}">{c['cta2']}</a>
    </div>
  </section>

  <section class="wrap figs-band" aria-label="{c['figs_h']}">
    <p class="figs-h">{t(c['figs_h'])} <a class="link" href="#{ids[3]}">{c['figs_more']}</a></p>
    <ul class="figs">{figs}</ul>
  </section>

  <section class="section sep" id="{ids[0]}">
    <div class="wrap">
      <h2>{t(c['exp_h'])}</h2>
      <ul class="exp">{exp}</ul>
    </div>
  </section>

  <section class="section sep" id="{ids[1]}">
    <div class="wrap">
      <h2>{t(c['offers_h'])}</h2>
      <p class="intro">{t(c['offers_intro'])}</p>
      <ul class="offers">{offers}</ul>
    </div>
  </section>

  <section class="section partners" id="{ids[2]}">
    <div class="wrap">
      <h2>{t(c['part_h'])}</h2>
      <p class="intro">{t(c['part_intro'])}</p>
      <ul class="part">{part}</ul>
      <p class="part-cta"><a class="link" href="#{ids[4]}">{c['part_cta']}</a></p>
    </div>
  </section>

  <section class="section proof" id="{ids[3]}">
    <div class="wrap">
      <h2>{t(c['proof_h'])}</h2>
      <ul class="ledger">{rows}</ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap method">
      <div class="method-head">
        <h2>{t(c['method_h'])}</h2>
        <p class="order">{t(c['method_order'])}</p>
      </div>
      <ol class="steps">{steps}</ol>
    </div>
  </section>

  <section class="section sep">
    <div class="wrap about-grid">
      <div class="about-head"><h2>{t(c['about_h'])}</h2>{portrait}</div>
      <div class="about-text">{about}<p class="also"><a class="link" href="{LINKEDIN}" rel="noopener">{c['linkedin']}</a></p></div>
    </div>
  </section>

  <section class="section contact" id="{ids[4]}">
    <div class="wrap">
      <h2>{t(c['contact_h'])}</h2>
      <p class="note">{t(c['contact_note'])}</p>
      <div class="contact-actions">
        <p><a class="btn" href="{book_href}"{ext}>{c['book']}</a>{book_note}</p>
        <div id="mail-box" class="mail-box" data-p="{rev}" data-s="{html.escape(c['mail_subject'])}" data-copy="{c['copy']}" data-copied="{c['copied']}">
          <button id="reveal" class="ghost" type="button" hidden>{c['reveal']}</button>
          <noscript><p class="ns">{c['noscript']}</p></noscript>
        </div>
      </div>
    </div>
  </section>
</main>
<footer class="site-footer"><div class="wrap foot">
  <span>{c['rights']}</span>
  <nav aria-label="Footer"><a href="{LINKEDIN}" rel="noopener">LinkedIn</a>{legal_link}<a href="{other_href}" hreflang="{"fr" if is_en else "en"}">{c['other_name']}</a></nav>
</div></footer>
{SCRIPT}
</body>
</html>
"""


LEGAL = {
    "fr": dict(
        lang="fr", title="Mentions légales | Nicolas Rigaud", h1="Mentions légales", back="Retour au site",
        blocks=[
            ("Éditeur du site", "Nicolas Rigaud, consultant indépendant. Pour le contacter, voir la section Contact de la page d'accueil."),
            ("Statut et adresse", "<span class='todo'>À COMPLÉTER : société de portage (raison sociale, forme, siège, SIREN) ou adresse de l'éditeur, selon ce que valide la société de portage. Téléphone à confirmer.</span>"),
            ("Directeur de la publication", "Nicolas Rigaud."),
            ("Hébergeur", "GitHub, Inc., service GitHub Pages. <span class='todo'>À COMPLÉTER : adresse postale à vérifier sur le site de GitHub.</span>"),
            ("Données personnelles", "Ce site n'utilise ni cookies ni outil de mesure d'audience. Si vous m'écrivez par e-mail, votre message est utilisé uniquement pour vous répondre."),
        ]),
    "en": dict(
        lang="en", title="Legal notice | Nicolas Rigaud", h1="Legal notice", back="Back to the site",
        blocks=[
            ("Publisher", "Nicolas Rigaud, independent consultant. To contact him, see the Contact section of the home page."),
            ("Status and address", "<span class='todo'>TO COMPLETE: umbrella company (name, legal form, registered office, SIREN) or publisher address, as validated with the umbrella company. Phone number to confirm.</span>"),
            ("Publication director", "Nicolas Rigaud."),
            ("Hosting", "GitHub, Inc., GitHub Pages service. <span class='todo'>TO COMPLETE: postal address to check on GitHub's website.</span>"),
            ("Personal data", "This site uses no cookies and no analytics. If you email me, your message is used only to reply to you."),
        ]),
}


def legal(k, is_en, suffix):
    d = LEGAL[k]
    pre = "../" if is_en else ""
    back = (("../" + suffix) if suffix else "../") if is_en else ("index.html" if suffix else "./")
    body = "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in d["blocks"])
    return f"""<!doctype html>
<html lang="{d['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']}</title><meta name="robots" content="noindex">
<link rel="icon" type="image/svg+xml" href="{pre}assets/mark.svg">
<link rel="stylesheet" href="{pre}assets/style.css"></head>
<body><div class="wrap legal"><p><a class="link" href="{back}">{d['back']}</a></p><h1>{d['h1']}</h1>{body}</div></body></html>
"""


def build(out, suffix):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "en"))
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(out, "assets"))
    shutil.copy(os.path.join(HERE, "assets", "favicon.ico"), os.path.join(out, "favicon.ico"))  # browsers ask /favicon.ico first
    w = lambda p, s: open(os.path.join(out, p), "w", encoding="utf-8").write(s)
    w("index.html", page(FR, False, suffix))
    w("en/index.html", page(EN, True, suffix))
    if SHOW_LEGAL:
        w("mentions-legales.html", legal("fr", False, suffix))
        w("en/legal-notice.html", legal("en", True, suffix))
    w("CNAME", "zeroonemany.com\n")
    w(".nojekyll", "")
    w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    w("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
      f'<url><loc>{DOMAIN}/</loc><xhtml:link rel="alternate" hreflang="fr" href="{DOMAIN}/"/><xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/"/></url>\n'
      f'<url><loc>{DOMAIN}/en/</loc><xhtml:link rel="alternate" hreflang="fr" href="{DOMAIN}/"/><xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/"/></url>\n</urlset>\n')


if __name__ == "__main__":
    build(os.path.join(HERE, "dist"), "")
    build(os.path.join(HERE, "preview"), "index.html")
    print("built v3")
