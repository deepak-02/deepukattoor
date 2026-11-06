#!/usr/bin/env python3
"""Generates index.html (Malayalam) and en/index.html (English) from one source.

Run from the site root:  python _build/build.py
Edit SITE_URL once the domain is known, then run again.
Facebook / YouTube links and videos live in assets/js/config.js.
"""
import json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://YOUR-DOMAIN"          # e.g. https://deepukattoor.in  (no trailing slash)
FACEBOOK_URL = "https://www.facebook.com/share/19eUXActYM/"
YOUTUBE_URL = "https://www.youtube.com/@deepukattoor6805"
EMAIL = "deepukattoor75@gmail.com"
PHONE = "+919497259252"
PHONE_DISPLAY = "+91 94972 59252"
WHATSAPP = "https://wa.me/919497259252"
VERSION = "6"

# Where to buy — keyed by publication year of the book
SHOPS = {
  "2026": [
    ("amazon", "https://www.amazon.in/dp/B0HLDNJ4D1", "https://www.amazon.in/favicon.ico", "Amazon"),
    ("booklove", "https://www.booklove.co.in/product-page/pedagogiyil-prathipadikkatha-chilathu",
     "https://static.wixstatic.com/media/cc5b56_096dc37d54f44dab8252c66723025107%7Emv2.png/v1/fill/w_64%2Ch_64%2Clg_1%2Cusm_0.66_1.00_0.01/cc5b56_096dc37d54f44dab8252c66723025107%7Emv2.png", "BookLove"),
  ],
}

# YouTube videos, shown in this order (edit here, then run the build)
VIDEOS = [
  ("O4Xa52V6V5k", "ചെരുപ്പ് — ഹ്രസ്വചിത്രം", "Cheruppu — short film"),
  ("SOXmx7TgZzg", "കപാൽ — ഭാഗം 1", "Kapaal — Part 1"),
  ("PHhEsIt6kow", "കപാൽ — ഭാഗം 2", "Kapaal — Part 2"),
  ("tixmJTcneXM", "കപാൽ — ഭാഗം 3", "Kapaal — Part 3"),
  ("VuDY7qmmoNM", "എങ്കിലുമെൻ്റെ പിള്ളേച്ചാ — ഹ്രസ്വചിത്രം", "Enkilumente Pillechaa — short film"),
  ("fKNKuZrQRIA", "സി.ആർ.വി. 2 — ഹ്രസ്വചിത്രം", "CRV-2 — short film"),
  ("By4S4eKZM00", "ഉലകവല — ഹ്രസ്വചിത്രം", "Ulakavala — short film"),
  ("NxUAgEMrBKY", "അതിജീവനം — ഹ്രസ്വചിത്രം · കഥ, തിരക്കഥ: ദീപു കാട്ടൂർ · സംവിധാനം: അരുൺ ജെ.", "Athijeevanam — short film · story and screenplay by Deepu Kattoor, directed by Arun J."),
  ("9ErmwflnWQQ", "ഒരു ലോക്ക്ഡൗൺ കാലം", "Oru Lockdown Kalam"),
  ("1xCqA13ohTc", "അന്യം — ഹ്രസ്വചിത്രം", "Anyam — short film"),
  ("HcuflF_oais", "നക്ഷത്രക്കണ്ണുള്ള പെണ്ണേ — ഗാനം", "Nakshathrakannulla Penne — song"),
  ("zwv7tVms3qw", "അനുരാഗ മുരളി — സംഗീത ആൽബം · മധു കാവുങ്കൽ, രാജേഷ് ചേർത്തല", "Anuraga Murali — music album · Madhu Kavunkal, Rajesh Cherthala"),
  ("HWlL-S8cJeM", "വായനദിന സന്ദേശം — ദീപു കാട്ടൂർ", "Reading Day message — Deepu Kattoor"),
]

GALLERY = json.load(open(os.path.join(ROOT, "_build", "gallery.json"), encoding="utf-8"))

e = html.escape

C = {
"ml": {
  "html_lang": "ml",
  "title": "ദീപു കാട്ടൂർ — കഥാകൃത്ത്, തിരക്കഥാകൃത്ത്, സംവിധായകൻ",
  "desc": "ആലപ്പുഴ കാട്ടൂർ സ്വദേശിയായ കഥാകൃത്ത്, തിരക്കഥാകൃത്ത്, സംവിധായകൻ ദീപു കാട്ടൂരിന്റെ ഔദ്യോഗിക വെബ്സൈറ്റ്. പുസ്തകങ്ങൾ, ഹ്രസ്വചിത്രങ്ങൾ, പുരസ്കാരങ്ങൾ, ഗാലറി, ബന്ധപ്പെടാനുള്ള വിവരങ്ങൾ.",
  "og_locale": "ml_IN",
  "skip": "ഉള്ളടക്കത്തിലേക്ക്",
  "name": "ദീപു കാട്ടൂർ",
  "mark": "ദീ",
  "nav": [("bio", "ജീവചരിത്രം"), ("works", "കൃതികൾ"), ("gallery", "ഗാലറി"), ("contact", "ബന്ധപ്പെടുക")],
  "lang_label": "Read in English",
  "lang_short": "EN",
  "lang_other_href": "en/",
  "lang_other_code": "en",
  "theme": "തീം മാറ്റുക",
  "menu": "മെനു",
  "roles": ["കഥാകൃത്ത്", "തിരക്കഥാകൃത്ത്", "സംവിധായകൻ"],
  "lead": "ആലപ്പുഴ ജില്ലയിലെ കാട്ടൂരിൽ നിന്നുള്ള എഴുത്തുകാരനും ചലച്ചിത്രകാരനും. നാല് പുസ്തകങ്ങൾ, പത്ത് ഹ്രസ്വചിത്രങ്ങൾ, രണ്ട് സംഗീത ആൽബങ്ങൾ, ഒരു ഒ.ടി.ടി. സിനിമ. ചെറുകഥയ്ക്ക് സംസ്ഥാന തലത്തിൽ നിരവധി പുരസ്കാരങ്ങൾ.",
  "cta1": "ഗാലറി കാണുക",
  "cta2": "ബന്ധപ്പെടുക",
  "portrait_alt": "ദീപു കാട്ടൂർ — പോർട്രെയ്റ്റ്",
  "latest_label": "പുതിയ പുസ്തകം · 2026",
  "latest_title": "പെഡഗോഗിയിൽ പ്രതിപാദിക്കാത്ത ചിലത്",
  "stats": [(4, "", "പുസ്തകങ്ങൾ"), (10, "", "ഹ്രസ്വചിത്രങ്ങൾ"), (2, "", "സംഗീത ആൽബങ്ങൾ"), (1, "", "ഒ.ടി.ടി. സിനിമ"), (15, "+", "പുരസ്കാരങ്ങൾ")],
  "bio_eyebrow": "ജീവചരിത്രം",
  "bio_title": "എഴുത്തും സിനിമയും",
  "intro": [
    "ആലപ്പുഴ ജില്ലയിലെ കാട്ടൂരിൽ ജനിച്ചു. കാട്ടൂർ ഹോളിഫാമിലി ഹൈസ്ക്കൂൾ, ചേർത്തല എസ്.എൻ. കോളേജ്, നാഷണൽ കോളേജ് എന്നിവിടങ്ങളിലായിരുന്നു വിദ്യാഭ്യാസം. അക്കൗണ്ടിംഗിലും സഹകരണത്തിലും ബിരുദങ്ങൾ. സഹകരണ സംഘം, പൊതുമരാമത്ത് വകുപ്പ് എന്നിവിടങ്ങളിൽ ജോലി ചെയ്തു. നിലവിൽ റവന്യൂ വകുപ്പ് ഉദ്യോഗസ്ഥനാണ്.",
    "കഥാകൃത്ത്, തിരക്കഥാകൃത്ത്, സംവിധായകൻ. സാഹിത്യ സാംസ്കാരിക രംഗത്ത് പ്രവർത്തിക്കുന്നു. ചെറുകഥ, നോവൽ, ലേഖനം, ഹ്രസ്വചിത്രം, ആൽബം എന്നീ മേഖലകൾ. ആകാശവാണിയിലും ആനുകാലികങ്ങളിലും രചനകൾ അവതരിപ്പിക്കാറുണ്ട്.",
  ],
  "facts_title": "വിവരങ്ങൾ",
  "facts": [
    ("ജന്മസ്ഥലം", "കാട്ടൂർ, ആലപ്പുഴ"),
    ("വിദ്യാഭ്യാസം", "ഹോളിഫാമിലി ഹൈസ്ക്കൂൾ, കാട്ടൂർ · എസ്.എൻ. കോളേജ്, ചേർത്തല · നാഷണൽ കോളേജ്"),
    ("ബിരുദങ്ങൾ", "അക്കൗണ്ടിംഗ്, സഹകരണം"),
    ("ഔദ്യോഗികം", "റവന്യൂ വകുപ്പ് (നിലവിൽ) · പൊതുമരാമത്ത് വകുപ്പ് · സഹകരണ സംഘം"),
  ],
  "family_title": "കുടുംബം",
  "family": [("പിതാവ്", "എൻ.വി. പുരുഷോത്തമൻ"), ("മാതാവ്", "പി.വി. സരള"), ("ഭാര്യ", "കെ. പ്രിയ"), ("മക്കൾ", "നിരഞ്ജൻ, ശ്രീലക്ഷ്മി")],
  "heritage": "പുന്നപ്ര വയലാർ സമര സേനാനിയും തുമ്പോളി പുളിച്ചുവട് ക്യാമ്പിൻ്റെ കൺവീനറുമായിരുന്ന പി.കെ. വേലായുധൻ്റെ ചെറുമകനാണ്.",
  "books_title": "പുസ്തകങ്ങൾ",
  "books": [
    ("2026", "പെഡഗോഗിയിൽ പ്രതിപാദിക്കാത്ത ചിലത്", "കഥാസമാഹാരം"),
    ("2025", "റെഡ് ഡേറ്റാ ബുക്ക്", "നോവൽ"),
    ("2015", "മണപ്പാറ കനവുകൾ", "കഥാസമാഹാരം"),
    ("2009", "വെനീസിലെ ഓളങ്ങൾ", "കഥാസമാഹാരം"),
  ],
  "films_title": "സിനിമ",
  "works": [("10", "ഹ്രസ്വചിത്രങ്ങൾ"), ("2", "സംഗീത ആൽബങ്ങൾ"), ("1", "ഒ.ടി.ടി. സിനിമ")],
  "films_text": "പത്ത് ഹ്രസ്വചിത്രങ്ങൾ തിരക്കഥയെഴുതി സംവിധാനം ചെയ്തു. രണ്ട് സംഗീത ആൽബങ്ങൾക്ക് സംവിധാനം നിർവ്വഹിച്ചു. <strong>കപാൽ</strong> എന്ന ഒ.ടി.ടി. സിനിമയുടെ തിരക്കഥയും സംവിധാനവും നിർവ്വഹിച്ചു.",
  "awards_title": "പുരസ്കാരങ്ങൾ",
  "awards_story": "ചെറുകഥ",
  "awards_film": "സിനിമ, തിരക്കഥ",
  "awards": [
    ("പ്രതിച്ഛായ – കാരൂർ പുരസ്കാരം", ""),
    ("നിലമ്പൂർ പ്രതിഭാ പുരസ്കാരം", ""),
    ("അയ്മനം കരുണാകരൻകുട്ടി പുരസ്കാരം", ""),
    ("സെക്രട്ടറിയേറ്റ് എംപ്ലോയിസ് രചനാ പുരസ്കാരം", ""),
    ("എൻ.ജി.ഒ. യൂണിയൻ സംസ്ഥാന പുരസ്കാരം", "4 തവണ"),
    ("ജോയിൻ്റ് കൗൺസിൽ പുരസ്കാരം", ""),
    ("സംസ്കാര സാഹിതി പുരസ്കാരം", ""),
    ("ലൈബ്രറി കൗൺസിൽ പുരസ്കാരം", ""),
    ("പച്ചമഷി പുരസ്കാരം", ""),
    ("സർഗ്ഗ കൈരളി പുരസ്കാരം", ""),
    ("ഇന്ത്യൻ റൈറ്റേഴ്സ് ഫോറം ഒ.വി. വിജയൻ സ്മാരക മൈക്രോ കഥാ പുരസ്കാരം", ""),
  ],
  "awards_f": [
    ("ഭരതൻ സ്മാരക പുരസ്കാരം", "ഉലകവല"),
    ("ശാരംഗപാണി പുരസ്കാരം", "ചെരുപ്പ്"),
    ("നവകേരള സദസ് – അമ്പലപ്പുഴ ഫെസ്റ്റ് പുരസ്കാരം", "ചെരുപ്പ്"),
    ("പത്മരാജൻ പുരസ്കാരം നോമിനേഷൻ, സംസ്ഥാന യുവജനക്ഷേമ ബോർഡ്", "അതിജീവനം"),
  ],
  "band1": ["പെഡഗോഗിയിൽ പ്രതിപാദിക്കാത്ത ചിലത്", "റെഡ് ഡേറ്റാ ബുക്ക്", "മണപ്പാറ കനവുകൾ", "വെനീസിലെ ഓളങ്ങൾ"],
  "band2": ["കപാൽ", "ചെരുപ്പ്", "ഉലകവല", "അതിജീവനം", "സി.ആർ.വി. 2", "അന്യം", "അനുരാഗ മുരളി"],
  "watch": "യൂട്യൂബിൽ കാണുക",
  "buy_on": "{}-ൽ വാങ്ങുക",
  "no_embed": "ഈ വീഡിയോ ഇവിടെ പ്ലേ ചെയ്യാൻ ഉടമ അനുവദിച്ചിട്ടില്ല. യൂട്യൂബിൽ കാണാം.",
  "gallery_title": "ഗാലറി",
  "more": "എല്ലാം കാണുക",
  "folders": {
    "books": "പുസ്തകങ്ങൾ", "films": "ഹ്രസ്വചിത്രങ്ങൾ", "stories": "കഥകൾ",
    "news": "വാർത്തകൾ", "functions": "ചടങ്ങുകൾ", "photos": "ചിത്രങ്ങൾ", "videos": "വീഡിയോകൾ",
  },
  "caps": {
    "books": ["എന്റെ പുസ്തകങ്ങൾ", "പെഡഗോഗിയിൽ പ്രതിപാദിക്കാത്ത ചിലത് — കഥാസമാഹാരം, 2026", "റെഡ് ഡേറ്റാ ബുക്ക് — നോവൽ, 2025", "മണപ്പാറ കനവുകൾ — കഥാസമാഹാരം, 2015", "വെനീസിലെ ഓളങ്ങൾ — കഥാസമാഹാരം, 2009"],
    "films": ["ചെരുപ്പ് — ഹ്രസ്വചിത്രം", "കപാൽ — ഒ.ടി.ടി. സിനിമ", "അനുരാഗ മുരളി — സംഗീത ആൽബം", "എങ്കിലുമെൻ്റെ പിള്ളേച്ചാ — ഹ്രസ്വചിത്രം", "സി.ആർ.വി. 2 — ഹ്രസ്വചിത്രം"],
  },
  "cap_default": {"stories": "ആനുകാലികത്തിൽ പ്രസിദ്ധീകരിച്ച കഥ", "news": "പത്ര വാർത്ത", "functions": "സാഹിത്യ സാംസ്കാരിക ചടങ്ങ്", "photos": "ദീപു കാട്ടൂർ"},
  "contact_eyebrow": "ബന്ധപ്പെടുക",
  "contact_title": "സംസാരിക്കാം",
  "contact_lead": "പ്രസാധനം, ചലച്ചിത്രം, സാഹിത്യ ചടങ്ങുകൾ, അഭിമുഖങ്ങൾ എന്നിവയ്ക്ക് ഇമെയിൽ വഴിയോ വാട്സ്ആപ്പ് വഴിയോ ബന്ധപ്പെടാം.",
  "ch_whatsapp": "വാട്സ്ആപ്പ്", "ch_phone": "ഫോൺ", "ch_email": "ഇമെയിൽ",
  "ch_facebook": "ഫേസ്ബുക്ക്", "ch_youtube": "യൂട്യൂബ് ചാനൽ", "ch_address": "വിലാസം",
  "fb_value": "ദീപു കാട്ടൂർ", "yt_value": "@deepukattoor6805",
  "address": "ദീപു കാട്ടൂർ, നികർത്തിൽ<br>കാട്ടൂർ പി.ഒ., കലവൂർ<br>ആലപ്പുഴ 688522, കേരളം",
  "wa_text": "നമസ്കാരം, വെബ്സൈറ്റ് വഴിയാണ് ബന്ധപ്പെടുന്നത്.",
  "footer": "© 2026 ദീപു കാട്ടൂർ",
  "top": "മുകളിലേക്ക്",
  "close": "അടയ്ക്കുക", "prev": "മുമ്പത്തേത്", "next": "അടുത്തത്",
  "lb_label": "ഗാലറി കാഴ്ച",
},
"en": {
  "html_lang": "en",
  "title": "Deepu Kattoor — Malayalam writer, screenwriter and director",
  "desc": "Official website of Deepu Kattoor, a Malayalam short story writer, novelist, screenwriter and director from Kattoor, Alappuzha. Books, short films, awards, gallery and contact.",
  "og_locale": "en_IN",
  "skip": "Skip to content",
  "name": "Deepu Kattoor",
  "mark": "ദീ",
  "nav": [("bio", "Biography"), ("works", "Works"), ("gallery", "Gallery"), ("contact", "Contact")],
  "lang_label": "മലയാളത്തിൽ വായിക്കുക",
  "lang_short": "മ",
  "lang_other_href": "../",
  "lang_other_code": "ml",
  "theme": "Switch theme",
  "menu": "Menu",
  "roles": ["Writer", "Screenwriter", "Director"],
  "lead": "A writer and filmmaker from Kattoor in Alappuzha. Four books, ten short films, two music albums and one OTT feature, with many state-level awards for the short story.",
  "cta1": "View gallery",
  "cta2": "Get in touch",
  "portrait_alt": "Portrait of Deepu Kattoor",
  "latest_label": "Latest book · 2026",
  "latest_title": "Pedagogiyil Prathipadikkatha Chilathu",
  "stats": [(4, "", "Books"), (10, "", "Short films"), (2, "", "Music albums"), (1, "", "OTT feature"), (15, "+", "Awards")],
  "bio_eyebrow": "Biography",
  "bio_title": "Stories and cinema",
  "intro": [
    "Born in Kattoor, Alappuzha district. Studied at Holy Family High School, Kattoor, S.N. College, Cherthala and National College, and holds degrees in accounting and co-operation. He has worked at a co-operative society and in the Public Works Department, and is currently an officer in the Revenue Department.",
    "A short story writer, screenwriter and director active in Kerala's literary and cultural life. His work spans the short story, the novel, essays, short films and music albums, and his writing appears on All India Radio (Akashvani) and in Malayalam periodicals.",
  ],
  "facts_title": "At a glance",
  "facts": [
    ("Born", "Kattoor, Alappuzha"),
    ("Education", "Holy Family High School, Kattoor · S.N. College, Cherthala · National College"),
    ("Degrees", "Accounting, Co-operation"),
    ("Career", "Revenue Department (current) · Public Works Department · Co-operative society"),
  ],
  "family_title": "Family",
  "family": [("Father", "N.V. Purushothaman"), ("Mother", "P.V. Sarala"), ("Wife", "K. Priya"), ("Children", "Niranjan, Sreelakshmi")],
  "heritage": "Grandson of P.K. Velayudhan, a fighter of the Punnapra-Vayalar uprising and convener of the Thumpoly Pulichuvadu camp.",
  "books_title": "Books",
  "books": [
    ("2026", "Pedagogiyil Prathipadikkatha Chilathu", "Short story collection"),
    ("2025", "Red Data Book", "Novel"),
    ("2015", "Manappara Kanavukal", "Short story collection"),
    ("2009", "Venisile Olangal", "Short story collection"),
  ],
  "films_title": "Film",
  "works": [("10", "Short films"), ("2", "Music albums"), ("1", "OTT feature")],
  "films_text": "Wrote and directed ten short films, directed two music albums, and wrote and directed the OTT feature <strong>Kapaal</strong>.",
  "awards_title": "Awards",
  "awards_story": "Short story",
  "awards_film": "Film and screenplay",
  "awards": [
    ("Prathichaya – Karoor Award", ""),
    ("Nilambur Prathibha Award", ""),
    ("Aymanam Karunakaran Kutty Award", ""),
    ("Secretariat Employees' Rachana Award", ""),
    ("NGO Union State Award", "4 times"),
    ("Joint Council Award", ""),
    ("Samskara Sahithi Award", ""),
    ("Library Council Award", ""),
    ("Pachamashi Award", ""),
    ("Sarga Kairali Award", ""),
    ("Indian Writers Forum O.V. Vijayan Memorial Micro Story Award", ""),
  ],
  "awards_f": [
    ("Bharathan Memorial Award", "Ulakavala"),
    ("Sharangapani Award", "Cheruppu"),
    ("Navakerala Sadas – Ambalappuzha Fest Award", "Cheruppu"),
    ("Padmarajan Award nomination, Kerala State Youth Welfare Board", "Athijeevanam"),
  ],
  "band1": ["Pedagogiyil Prathipadikkatha Chilathu", "Red Data Book", "Manappara Kanavukal", "Venisile Olangal"],
  "band2": ["Kapaal", "Cheruppu", "Ulakavala", "Athijeevanam", "CRV-2", "Anyam", "Anuraga Murali"],
  "watch": "Watch on YouTube",
  "buy_on": "Buy on {}",
  "no_embed": "The owner doesn't allow this video to play on other sites. You can watch it on YouTube.",
  "gallery_title": "Gallery",
  "more": "Show all",
  "folders": {
    "books": "Books", "films": "Short films", "stories": "Stories",
    "news": "In the news", "functions": "Events", "photos": "Photos", "videos": "Videos",
  },
  "caps": {
    "books": ["My books", "Pedagogiyil Prathipadikkatha Chilathu — short stories, 2026", "Red Data Book — novel, 2025", "Manappara Kanavukal — short stories, 2015", "Venisile Olangal — short stories, 2009"],
    "films": ["Cheruppu — short film", "Kapaal — OTT feature", "Anuraga Murali — music album", "Enkilumente Pillechaa — short film", "CRV-2 — short film"],
  },
  "cap_default": {"stories": "Story published in a Malayalam periodical", "news": "Newspaper report", "functions": "Literary and cultural event", "photos": "Deepu Kattoor"},
  "contact_eyebrow": "Contact",
  "contact_title": "Get in touch",
  "contact_lead": "For publishing, film, literary events and interviews, reach out by email or WhatsApp.",
  "ch_whatsapp": "WhatsApp", "ch_phone": "Phone", "ch_email": "Email",
  "ch_facebook": "Facebook", "ch_youtube": "YouTube channel", "ch_address": "Address",
  "fb_value": "Deepu Kattoor", "yt_value": "@deepukattoor6805",
  "address": "Deepu Kattoor, Nikarthil<br>Kattoor P.O., Kalavoor<br>Alappuzha 688522, Kerala, India",
  "wa_text": "Hello, I'm reaching out through your website.",
  "footer": "© 2026 Deepu Kattoor",
  "top": "Back to top",
  "close": "Close", "prev": "Previous", "next": "Next",
  "lb_label": "Gallery viewer",
},
}

ICONS = {
  "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
  "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
  "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
  "x": '<path d="M18 6 6 18M6 6l12 12"/>',
  "left": '<path d="m15 18-6-6 6-6"/>',
  "right": '<path d="m9 18 6-6-6-6"/>',
  "up": '<path d="m5 12 7-7 7 7M12 19V5"/>',
  "arrow": '<path d="M7 7h10v10M7 17 17 7"/>',
  "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
  "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
  "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
  "facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
  "youtube": '<path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>',
  "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
  "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
  "film": '<rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 3v18M3 7.5h4M3 12h18M3 16.5h4M17 3v18M17 7.5h4M17 16.5h4"/>',
  "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
  "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
  "zoom": '<path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/>',
  "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
}
PLAY = '<symbol id="i-play" viewBox="0 0 24 24"><path d="M6 3l14 9-14 9z"/></symbol>'

def icon(n, cls=""):
    return f'<svg class="icon{(" " + cls) if cls else ""}" aria-hidden="true"><use href="#i-{n}"/></svg>'

WAVE = '<svg class="waterline" viewBox="0 0 96 10" aria-hidden="true"><path d="M1 5 Q7 1 13 5 T25 5 T37 5 T49 5 T61 5 T73 5 T85 5 T95 5"/></svg>'

FOLDER_ORDER = ["books", "films", "videos", "stories", "news", "functions", "photos"]

def lang_of(t):
    return t["html_lang"]

def gallery_html(t, P):
    tabs, panels = [], []
    for slug in FOLDER_ORDER:
        label = t["folders"][slug]
        if slug == "videos":
            cover = f'<span class="folder__cover folder__cover--video"><img src="https://i.ytimg.com/vi/{VIDEOS[0][0]}/mqdefault.jpg" width="40" height="40" alt="" loading="lazy" decoding="async"><span class="folder__play">{icon("play", "icon--fill")}</span></span>'
            count = f'<small class="num">{len(VIDEOS)}</small>'
        else:
            items = GALLERY[slug]
            n0 = items[0][0]
            cover = f'<span class="folder__cover"><img src="{P}Assets/img/{slug}/thumb/{n0}" width="40" height="40" alt="" loading="lazy" decoding="async"></span>'
            count = f'<small class="num">{len(items)}</small>'
        sel = "true" if slug == "books" else "false"
        tabs.append(f'<button type="button" class="folder" role="tab" id="tab-{slug}" aria-controls="panel-{slug}" aria-selected="{sel}" tabindex="{0 if slug=="books" else -1}">{cover}<span>{e(label)}{count}</span></button>')
        if slug == "videos":
            li = lang_of(t)
            vt = []
            for i, (vid, ml, en) in enumerate(VIDEOS):
                title = ml if li == "ml" else en
                extra = " is-extra" if i >= 6 else ""
                vt.append(f'<a class="tile video-tile{extra}" href="https://youtu.be/{vid}" data-yt="{vid}" data-cap="{e(title)}">'
                          f'<img src="https://i.ytimg.com/vi/{vid}/mqdefault.jpg" width="320" height="180" alt="{e(title)}" loading="lazy" decoding="async">'
                          f'<span class="idx">{i+1}</span><span class="play"><span>{icon("play", "icon--fill")}</span></span><figcaption>{e(title)}</figcaption></a>')
            more = f'<button type="button" class="btn btn--ghost more">{e(t["more"])} <span class="num">({len(vt)})</span></button>' if len(vt) > 6 else ""
            panels.append(f'<div class="panel" id="panel-videos" role="tabpanel" aria-labelledby="tab-videos" hidden><div class="grid grid--video">{"".join(vt)}</div>{more}</div>')
            continue
        tiles = []
        caps = t["caps"].get(slug)
        for i, (n, tw, th, fw, fh) in enumerate(GALLERY[slug]):
            cap = caps[i] if caps and i < len(caps) else f'{t["cap_default"][slug]} {i+1}'
            alt = f'{t["name"]} — {cap}' if slug != "photos" else cap + f" {i+1}"
            extra = " is-extra" if i >= 6 else ""
            tiles.append(
                f'<a class="tile{extra}" href="{P}Assets/img/{slug}/{n}" data-cap="{e(cap)}">'
                f'<img src="{P}Assets/img/{slug}/thumb/{n}" width="{tw}" height="{th}" alt="{e(alt)}" loading="lazy" decoding="async"><span class="zoom">{icon("zoom")}</span></a>')
        more = f'<button type="button" class="btn btn--ghost more">{e(t["more"])} <span class="num">({len(tiles)})</span></button>' if len(tiles) > 6 else ""
        hidden = "" if slug == "books" else " hidden"
        panels.append(f'<div class="panel" id="panel-{slug}" role="tabpanel" aria-labelledby="tab-{slug}"{hidden}><div class="grid">{"".join(tiles)}</div>{more}</div>')
    first = len(GALLERY["books"])
    return f'''
<section class="gallery reveal reveal--scale" id="gallery" aria-labelledby="gallery-title">
  <div class="gallery__head"><h2 id="gallery-title">{e(t["gallery_title"])}</h2><span class="gallery__count num">{first}</span></div>
  <div class="folders" role="tablist" aria-label="{e(t["gallery_title"])}">{"".join(tabs)}</div>
  <div class="gallery__scroll">{"".join(panels)}</div>
</section>'''

def jsonld(t, lang, url):
    same = [u for u in (FACEBOOK_URL, YOUTUBE_URL) if u]
    person = {
        "@type": "Person", "@id": SITE_URL + "/#person",
        "name": "Deepu Kattoor", "alternateName": "ദീപു കാട്ടൂർ",
        "url": SITE_URL + "/", "image": SITE_URL + "/Assets/img/portrait.webp",
        "jobTitle": ["Writer", "Screenwriter", "Film director"],
        "description": C["en"]["desc"],
        "email": "mailto:" + EMAIL, "telephone": PHONE,
        "birthPlace": {"@type": "Place", "name": "Kattoor, Alappuzha, Kerala"},
        "address": {"@type": "PostalAddress", "streetAddress": "Nikarthil, Kattoor P.O., Kalavoor", "addressLocality": "Alappuzha", "postalCode": "688522", "addressRegion": "Kerala", "addressCountry": "IN"},
        "alumniOf": [{"@type": "EducationalOrganization", "name": "S.N. College, Cherthala"}, {"@type": "EducationalOrganization", "name": "Holy Family High School, Kattoor"}],
        "knowsLanguage": ["ml", "en"],
        "award": [a for a, _ in C["en"]["awards"]] + [f"{a} ({w})" for a, w in C["en"]["awards_f"][:3]],
    }
    if same: person["sameAs"] = same
    books = [{"@type": "Book", "name": C["ml"]["books"][i][1], "alternateName": C["en"]["books"][i][1],
              "bookFormat": "https://schema.org/Paperback", "inLanguage": "ml",
              "genre": C["en"]["books"][i][2], "datePublished": C["en"]["books"][i][0],
              "author": {"@id": SITE_URL + "/#person"},
              **({"offers": [{"@type": "Offer", "url": u, "seller": {"@type": "Organization", "name": n}, "availability": "https://schema.org/InStock"} for _, u, _, n in SHOPS[C["en"]["books"][i][0]]]} if C["en"]["books"][i][0] in SHOPS else {})} for i in range(4)]
    film = {"@type": "Movie", "name": "Kapaal", "alternateName": "കപാൽ", "director": {"@id": SITE_URL + "/#person"}, "author": {"@id": SITE_URL + "/#person"}, "inLanguage": "ml"}
    site = {"@type": "WebSite", "@id": SITE_URL + "/#website", "url": SITE_URL + "/", "name": t["name"], "inLanguage": ["ml", "en"]}
    page = {"@type": "ProfilePage", "@id": url + "#page", "url": url, "name": t["title"], "inLanguage": lang, "isPartOf": {"@id": SITE_URL + "/#website"}, "mainEntity": {"@id": SITE_URL + "/#person"}}
    return json.dumps({"@context": "https://schema.org", "@graph": [page, site, person, *books, film]}, ensure_ascii=False, indent=1)

def page(lang):
    t = C[lang]
    P = "" if lang == "ml" else "../"
    url = SITE_URL + ("/" if lang == "ml" else "/en/")
    nav = "".join(f'<a href="#{i}">{e(l)}</a>' for i, l in t["nav"])
    sheet = "".join(f'<a href="#{i}">{e(l)}{icon("right")}</a>' for i, l in t["nav"])
    words = " ".join(f'<span class="w" aria-hidden="true"><span style="--w:{i}">{e(w)}</span></span>' for i, w in enumerate(t["name"].split()))
    band1 = "".join(f"<span>{e(x)}</span>" for x in t["band1"] * 3)
    band2 = "".join(f"<span>{e(x)}</span>" for x in t["band2"] * 3)
    roles = "".join(f"<span>{e(r)}</span>" for r in t["roles"])
    stats = "".join(f'<li class="reveal spot" style="--i:{i}"><strong class="num" data-count="{n}" data-suffix="{s}">{n}{s}</strong><span>{e(l)}</span></li>' for i, (n, s, l) in enumerate(t["stats"]))
    facts = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in t["facts"])
    family = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in t["family"])
    def shops(y):
        if y not in SHOPS: return ""
        btns = "".join(
            f'<a class="shop shop--{k}" href="{u}" target="_blank" rel="noopener">'
            f'<img src="{ic}" width="20" height="20" alt="" loading="lazy" decoding="async" referrerpolicy="no-referrer" onerror="this.remove()">'
            f'<span>{e(t["buy_on"].format(name))}</span>{icon("arrow")}</a>' for k, u, ic, name in SHOPS[y])
        return f'<div class="shops">{btns}</div>'
    books = "".join(f'<li><time datetime="{y}">{y}</time><strong>{e(n)}</strong><span>{e(k)}</span>{shops(y)}</li>' for y, n, k in t["books"])
    works = "".join(f'<div class="spot"><strong class="num">{n}</strong><span>{e(l)}</span></div>' for n, l in t["works"])
    aw = "".join(f'<li><span>{e(a)}</span>{f"<small>{e(x)}</small>" if x else ""}</li>' for a, x in t["awards"])
    awf = "".join(f'<li><span>{e(a)}</span><small>{e(x)}</small></li>' for a, x in t["awards_f"])
    from urllib.parse import quote
    wa = WHATSAPP + "?text=" + quote(t["wa_text"])
    sprite = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + PLAY
    other_url = SITE_URL + ("/en/" if lang == "ml" else "/")

    return f'''<!doctype html>
<html lang="{t["html_lang"]}" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="author" content="Deepu Kattoor">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ml" href="{SITE_URL}/">
<link rel="alternate" hreflang="en" href="{SITE_URL}/en/">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<meta name="theme-color" content="#f3f6fb">
<meta name="color-scheme" content="light">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="{e(t["name"])}">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/Assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(t["portrait_alt"])}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta property="og:locale:alternate" content="{"en_IN" if lang == "ml" else "ml_IN"}">
<meta property="profile:first_name" content="Deepu">
<meta property="profile:last_name" content="Kattoor">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t["title"])}">
<meta name="twitter:description" content="{e(t["desc"])}">
<meta name="twitter:image" content="{SITE_URL}/Assets/img/og.jpg">
<link rel="icon" href="{P}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{P}Assets/img/apple-touch-icon.png">
<link rel="manifest" href="{P}site.webmanifest">
<script>
(function(){{try{{var t=localStorage.getItem("theme");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}document.documentElement.classList.add("js");}})();
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anek+Malayalam:wght@400;500;600&family=Noto+Serif+Malayalam:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap">
<link rel="preload" as="image" href="{P}Assets/img/portrait.webp" imagesrcset="{P}Assets/img/portrait-480.webp 480w, {P}Assets/img/portrait.webp 960w" imagesizes="(min-width: 900px) 440px, 90vw" fetchpriority="high">
<link rel="stylesheet" href="{P}Assets/css/style.css?v={VERSION}">
<script type="application/ld+json">
{jsonld(t, lang, url)}
</script>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{sprite}</svg>
<a class="skip" href="#main">{e(t["skip"])}</a>

<header class="header">
  <div class="wrap header__in">
    <a class="brand" href="#top" aria-label="{e(t["name"])}"><span class="brand__mark" aria-hidden="true">{t["mark"]}</span><span translate="no">{e(t["name"])}</span></a>
    <nav class="nav" aria-label="{e(t["menu"])}">{nav}</nav>
    <div class="tools">
      <a class="tool lang" href="{t["lang_other_href"]}" hreflang="{t["lang_other_code"]}" lang="{t["lang_other_code"]}" aria-label="{e(t["lang_label"])}" title="{e(t["lang_label"])}"><b>{t["lang_short"]}</b></a>
      <button type="button" class="tool theme-btn" aria-label="{e(t["theme"])}" title="{e(t["theme"])}">{icon("sun", "i-sun")}{icon("moon", "i-moon")}</button>
      <button type="button" class="tool menu-btn" aria-label="{e(t["menu"])}" aria-expanded="false" aria-controls="sheet">{icon("menu", "i-menu")}{icon("x", "i-x")}</button>
    </div>
  </div>
</header>
<nav class="sheet" id="sheet" aria-label="{e(t["menu"])}">{sheet}</nav>

<main id="main">
  <section class="hero" id="top" aria-labelledby="hero-title">
    <div class="wrap hero__grid">
      <div class="hero__text">
        <p class="hero__roles reveal">{roles}</p>
        <h1 id="hero-title" translate="no" class="reveal" style="--i:1" aria-label="{e(t["name"])}">{words}</h1>
        <div class="reveal" style="--i:2">{WAVE}</div>
        <p class="hero__lead reveal" style="--i:2">{e(t["lead"])}</p>
        <div class="hero__cta reveal" style="--i:3">
          <a class="btn btn--primary" href="#gallery">{e(t["cta1"])}{icon("right")}</a>
          <a class="btn btn--ghost" href="#contact">{e(t["cta2"])}</a>
        </div>
      </div>
      <figure class="portrait reveal reveal--right" style="--i:2">
       <div class="portrait__tilt">
        <span class="portrait__ring" aria-hidden="true"></span>
        <div class="portrait__frame">
          <span class="portrait__shine" aria-hidden="true"></span>
          <img src="{P}Assets/img/portrait.webp" srcset="{P}Assets/img/portrait-480.webp 480w, {P}Assets/img/portrait.webp 960w" sizes="(min-width: 900px) 440px, 90vw" width="960" height="1200" alt="{e(t["portrait_alt"])}" fetchpriority="high" decoding="async">
        </div>
        <a class="latest" href="#works">
          <img src="{P}Assets/img/books/thumb/02.webp" width="56" height="72" alt="" loading="lazy" decoding="async">
          <span><small>{e(t["latest_label"])}</small><strong>{e(t["latest_title"])}</strong></span>
        </a>
       </div>
      </figure>
    </div>
  </section>

  <section class="stats" aria-label="{e(t["bio_title"])}">
    <div class="wrap"><ul>{stats}</ul></div>
  </section>

  <div class="band" aria-hidden="true">
    <div class="band__row" data-speed="-0.25">{band1}</div>
    <div class="band__row band__row--alt" data-speed="0.25">{band2}</div>
  </div>

  <section class="section" id="bio" aria-labelledby="bio-title">
    <div class="wrap split">
      <article class="bio">
        <header class="reveal">
          <p class="eyebrow">{e(t["bio_eyebrow"])}</p>
          <h2 class="section-title" id="bio-title">{e(t["bio_title"])}</h2>
          {WAVE}
        </header>
        <div class="bio__intro reveal">{"".join(f"<p>{e(p)}</p>" for p in t["intro"])}</div>

        <section class="reveal" aria-labelledby="facts-title">
          <h3 id="facts-title">{icon("info")}{e(t["facts_title"])}</h3>
          <dl class="facts">{facts}</dl>
        </section>

        <section class="reveal" aria-labelledby="family-title">
          <h3 id="family-title">{icon("users")}{e(t["family_title"])}</h3>
          <dl class="facts">{family}</dl>
          <p class="note" style="margin-top:16px">{e(t["heritage"])}</p>
        </section>

        <section class="reveal" id="works" aria-labelledby="books-title">
          <h3 id="books-title">{icon("book")}{e(t["books_title"])}</h3>
          <ol class="timeline">{books}</ol>
        </section>

        <section class="reveal" aria-labelledby="films-title">
          <h3 id="films-title">{icon("film")}{e(t["films_title"])}</h3>
          <div class="works">{works}</div>
          <p class="prose">{t["films_text"]}</p>
        </section>

        <section class="reveal" aria-labelledby="awards-title">
          <h3 id="awards-title">{icon("award")}{e(t["awards_title"])}</h3>
          <div class="awards-group"><h4>{e(t["awards_story"])}</h4><ul class="awards">{aw}</ul></div>
          <div class="awards-group"><h4>{e(t["awards_film"])}</h4><ul class="awards">{awf}</ul></div>
        </section>
      </article>
      {gallery_html(t, P)}
    </div>
  </section>

  <section class="section contact" id="contact" aria-labelledby="contact-title">
    <div class="wrap contact__grid">
      <div class="reveal">
        <p class="eyebrow">{e(t["contact_eyebrow"])}</p>
        <h2 class="section-title" id="contact-title">{e(t["contact_title"])}</h2>
        {WAVE}
        <p class="contact__lead">{e(t["contact_lead"])}</p>
      </div>
      <div class="channels">
        <a class="channel spot reveal" style="--i:0" href="{wa}" target="_blank" rel="noopener">
          <span class="channel__icon">{icon("chat")}</span><span><small>{e(t["ch_whatsapp"])}</small><span class="num">{PHONE_DISPLAY}</span></span>{icon("arrow", "arrow")}
        </a>
        <a class="channel spot reveal" style="--i:1" href="tel:{PHONE}">
          <span class="channel__icon">{icon("phone")}</span><span><small>{e(t["ch_phone"])}</small><span class="num">{PHONE_DISPLAY}</span></span>{icon("arrow", "arrow")}
        </a>
        <a class="channel channel--wide spot reveal" style="--i:2" href="mailto:{EMAIL}">
          <span class="channel__icon">{icon("mail")}</span><span><small>{e(t["ch_email"])}</small><span>{EMAIL}</span></span>{icon("arrow", "arrow")}
        </a>
        <a class="channel spot reveal" style="--i:3" data-link="facebook" href="{FACEBOOK_URL or "#"}" target="_blank" rel="noopener me">
          <span class="channel__icon">{icon("facebook")}</span><span><small>{e(t["ch_facebook"])}</small><span data-link-value>{e(t["fb_value"])}</span></span>{icon("arrow", "arrow")}
        </a>
        <a class="channel spot reveal" style="--i:4" data-link="youtube" href="{YOUTUBE_URL or "#"}" target="_blank" rel="noopener me">
          <span class="channel__icon">{icon("youtube")}</span><span><small>{e(t["ch_youtube"])}</small><span data-link-value>{e(t["yt_value"])}</span></span>{icon("arrow", "arrow")}
        </a>
        <div class="channel channel--wide reveal" style="--i:5">
          <span class="channel__icon">{icon("pin")}</span><span><small>{e(t["ch_address"])}</small><address>{t["address"]}</address></span>
        </div>
      </div>
    </div>
  </section>
</main>

<footer class="footer">
  <div class="wrap footer__in">
    <span>{e(t["footer"])}</span>
    <a href="{t["lang_other_href"]}" hreflang="{t["lang_other_code"]}" lang="{t["lang_other_code"]}" data-lang-link>{e(t["lang_label"])}</a>
  </div>
</footer>

<div class="progress" aria-hidden="true"><span></span></div>
<button type="button" class="to-top" aria-label="{e(t["top"])}"><svg class="ring" viewBox="0 0 46 46" aria-hidden="true"><circle cx="23" cy="23" r="22"/></svg>{icon("up")}</button>

<dialog class="lightbox" aria-label="{e(t["lb_label"])}" data-watch="{e(t["watch"])}" data-noembed="{e(t["no_embed"])}">
  <div class="lb__bar"><span class="lb__count num"></span><button type="button" class="lb__btn lb__close" aria-label="{e(t["close"])}">{icon("x")}</button></div>
  <div class="lb__stage"></div>
  <button type="button" class="lb__btn lb__nav lb__nav--prev lb__prev" aria-label="{e(t["prev"])}">{icon("left")}</button>
  <button type="button" class="lb__btn lb__nav lb__nav--next lb__next" aria-label="{e(t["next"])}">{icon("right")}</button>
  <div class="lb__foot"><div class="lb__info"><p class="lb__cap"></p><a class="lb__yt" href="#" target="_blank" rel="noopener" hidden>{icon("youtube")}<span>{e(t["watch"])}</span></a></div><div class="lb__mobnav"><button type="button" class="lb__btn lb__prev" aria-label="{e(t["prev"])}">{icon("left")}</button><button type="button" class="lb__btn lb__next" aria-label="{e(t["next"])}">{icon("right")}</button></div></div>
  <div class="lb__strip"></div>
</dialog>

<script src="{P}Assets/js/main.js?v={VERSION}" defer></script>
</body>
</html>
'''

def main():
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page("ml"))
    os.makedirs(os.path.join(ROOT, "en"), exist_ok=True)
    open(os.path.join(ROOT, "en", "index.html"), "w", encoding="utf-8").write(page("en"))
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{SITE_URL}/</loc>
    <xhtml:link rel="alternate" hreflang="ml" href="{SITE_URL}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en/"/>
    <changefreq>monthly</changefreq><priority>1.0</priority>
  </url>
  <url>
    <loc>{SITE_URL}/en/</loc>
    <xhtml:link rel="alternate" hreflang="ml" href="{SITE_URL}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{SITE_URL}/en/"/>
    <changefreq>monthly</changefreq><priority>0.8</priority>
  </url>
</urlset>
''')
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("built")

if __name__ == "__main__":
    main()
