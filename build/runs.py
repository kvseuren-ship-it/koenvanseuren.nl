# Speeldata, gestructureerd. Datums: 'JJJJ', 'JJJJ-MM' of 'JJJJ-MM-DD'.
# RUNS[slug] = lijst van (van, tot of None, soort, plaats); soort: "premiere", "tour" of None.
# AGENDA[slug] = (van, tot of None, korte plaatsaanduiding) — één regel per productie in de agenda.
RUNS = {
 "de-zelfmoordenaar": [("2026-11-13", "2026-11-15", None, "Jonge Harten Festival, Groningen")],
 "we-zijn-niet-alleen": [("2026-07", None, None, "De Parade, Den Haag en Amsterdam"),
                         ("2026-08-14", "2026-08-18", None, "De Parade, Utrecht")],
 "bosch-parade-2026": [("2026-05-20", "2026-06-21", None, "Tuin der Lusten, Citadel, ’s-Hertogenbosch"),
                       ("2026-06-18", "2026-06-21", None, "Bosch Parade, Dommel, ’s-Hertogenbosch")],
 "herzschmerz": [("2026-02-20", None, "premiere", "Grand Theatre Groningen"),
                 ("2026-02", "2026-04", "tour", "De Nieuwe Vorst Tilburg, Schuur Haarlem, Theater Kikker Utrecht, Zaal 3 Den Haag, De Harmonie Leeuwarden, Theater Bellevue Amsterdam, Theater Walhalla Rotterdam, De Lieve Vrouw Amersfoort, Theater aan de Rijn Arnhem")],
 "revenge-of-the-extras": [("2025-06-20", None, "premiere", "De Parade Rotterdam"),
                           ("2025-07", "2025-08", None, "De Parade Den Haag, Amsterdam, Utrecht")],
 "we-are-the-world-we-are-the-brabant": [("2025-01-31", None, "premiere", ""),
                                         ("2025-02", "2025-03-16", "tour", "Tilburg, ’s-Hertogenbosch, Helmond, Etten-Leur, Roosendaal, Eindhoven")],
 "bosch-parade-2024": [("2024-06-20", "2024-06-23", None, "Bosch Parade, Dommel, ’s-Hertogenbosch")],
 "as-the-world-hurts": [("2024-05-04", None, "premiere", "Grand Theatre Groningen"),
                        ("2024", "2025", "tour", "Theater Bellevue Amsterdam, Theater Kikker Utrecht, Theater Walhalla Rotterdam, Schuur Haarlem, Zaal 3 Den Haag, Verkadefabriek Den Bosch")],
 "funf-sechs-alles-flex": [("2023-06-23", None, "premiere", "")],
 "hamlet-versus-don-quixote": [("2023-02-24", None, "premiere", "Grand Theatre Groningen"),
                               ("2023", None, "tour", "Festival Cement Den Bosch, Het Nationale Theater Den Haag, Theater Kikker Utrecht, Theater Walhalla Rotterdam, De Sloot Amsterdam")],
 "peer-gynt": [("2022-06-04", None, "premiere", "Grand Theatre Groningen"),
               ("2022", "2024", "tour", "Het Nationale Theater Den Haag, Theater Kikker Utrecht, Theater Walhalla Rotterdam, De Lawei Drachten, Stormram-tournee Groningen/Friesland/Drenthe")],
 "on-hold": [("2022-04-07", None, None, "Likeminds, Amsterdam")],
 "de-rattenvanger": [("2020-02-08", None, "premiere", "")],
}
AGENDA = {
 "vvv-voor-volk-en-vaderland": ("2027", "2028", {"nl": "in ontwikkeling", "en": "in development", "ru": "в разработке"}),
 "de-zelfmoordenaar": ("2026-11-13", "2026-11-15", "Jonge Harten Festival, Groningen"),
 "we-zijn-niet-alleen": ("2026-07", "2026-08", "De Parade, Den Haag · Amsterdam · Utrecht"),
 "bosch-parade-2026": ("2026-06-18", "2026-06-21", "’s-Hertogenbosch"),
 "herzschmerz": ("2026-02", "2026-04", "Grand Theatre Groningen + tournee"),
 "revenge-of-the-extras": ("2025-06", "2025-08", "De Parade, Rotterdam · Den Haag · Amsterdam · Utrecht"),
 "we-are-the-world-we-are-the-brabant": ("2025-01", "2025-03", "Brabant-tournee"),
 "bosch-parade-2024": ("2024-06-20", "2024-06-23", "’s-Hertogenbosch"),
 "as-the-world-hurts": ("2024", "2025", "Grand Theatre Groningen + tournee"),
 "funf-sechs-alles-flex": ("2023-06-23", None, "Het Zuidelijk Toneel / Club Gewalt"),
 "hamlet-versus-don-quixote": ("2023", None, "Grand Theatre Groningen + tournee"),
 "peer-gynt": ("2022", "2024", "Grand Theatre Groningen + tournee"),
 "on-hold": ("2022-04-07", None, "Likeminds, Amsterdam"),
 "de-rattenvanger": ("2020-02-08", None, "Theater Oostpool"),
}
MONTHS = {
 "nl": "jan feb mrt apr mei jun jul aug sep okt nov dec".split(),
 "en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(),
 "ru": "янв. февр. марта апр. мая июня июля авг. сент. окт. нояб. дек.".split(),
}
KIND = {"premiere": {"nl": "première", "en": "premiere", "ru": "премьера"},
        "tour": {"nl": "tournee", "en": "tour", "ru": "гастроли"}}
PLACE_TR = {"en": [(" en ", " and "), ("Den Haag", "The Hague"), ("tournee", "tour"), ("Brabant-tournee", "Brabant tour"), ("Stormram-tour", "Stormram tour")],
            "ru": [(" en ", " и "), ("+ tournee", "+ гастроли"), ("Brabant-tournee", "гастроли по Брабанту"), ("Stormram-tournee", "тур Stormram")]}

def _parts(d):
    p = d.split("-")
    return int(p[0]), (int(p[1]) if len(p) > 1 else None), (int(p[2]) if len(p) > 2 else None)

def _one(y, m, d, lang, show_year=True):
    M = MONTHS[lang]
    s = ""
    if d: s += f"{d} "
    if m: s += M[m - 1]
    if show_year: s += (" " if m else "") + str(y)
    return s.strip()

def fmt(a, b, lang):
    """Eén datumstijl voor de hele site: 4 mei 2024 · 13–15 nov 2026 · 20 mei – 21 jun 2026 · feb–apr 2026 · 2022–2024."""
    y1, m1, d1 = _parts(a)
    if not b:
        return _one(y1, m1, d1, lang)
    y2, m2, d2 = _parts(b)
    if not (d1 and d2): d1 = d2 = None       # gelijke precisie: dagen alleen als beide bekend
    if y1 != y2 and not (d1 and d2): m1 = m2 = None
    if not m1 or not m2:                      # jaarprecisie
        return str(y1) if y1 == y2 else f"{y1}–{y2}"
    M = MONTHS[lang]
    if y1 == y2 and m1 == m2 and d1 and d2:   # 13–15 nov 2026
        return f"{d1}–{d2} {M[m1-1]} {y1}"
    if y1 == y2 and not d1 and not d2:        # feb–apr 2026
        return f"{M[m1-1]}–{M[m2-1]} {y1}"
    if y1 == y2:                              # 20 mei – 21 jun 2026
        return f"{_one(y1, m1, d1, lang, False)} – {_one(y2, m2, d2, lang)}"
    return f"{_one(y1, m1, d1, lang)} – {_one(y2, m2, d2, lang)}"

def place(s, lang):
    if isinstance(s, dict):
        return s[lang]
    for x, y in PLACE_TR.get(lang, []):
        s = s.replace(x, y)
    return s

def run_line(r, lang):
    a, b, kind, pl = r
    bits = [fmt(a, b, lang)]
    k = KIND[kind][lang] if kind else ""
    tail = k + ((": " if kind == "tour" else ", ") if k and pl else "") + place(pl, lang)
    return bits[0], tail
