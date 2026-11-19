# -*- coding: utf-8 -*-
"""Bouwt koenvanseuren.nl als statische site in ../site  —  python3 build.py"""
import json, os, shutil, html, re
from content import *

SITE = "https://koenvanseuren.nl"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
YEAR_NOW = 2026

try:
    from images import M as _IMG
except Exception:
    _IMG = {}
from PIL import Image
def dims(k):
    p = os.path.join(OUT, "img", k + ".jpg")
    with Image.open(p) as im:
        return im.size

DATE_TR = {
 "en": [("première", "premiere"), ("tournee", "tour"), ("o.a.", "incl."), ("juli", "July"), ("zomer", "summer"),
        ("feb–apr", "Feb–Apr"), ("Den Haag", "The Hague"), ("Stormram-tournee", "Stormram tour")],
 "ru": [("première", "премьера"), ("Stormram-tournee", "тур Stormram"), ("tournee", "гастроли"), ("o.a.", "в т.ч."), ("juli", "июль"), ("zomer", "лето"),
        ("feb–apr", "февраль–апрель")],
}
def tr_date(s, lang):
    for a, b in DATE_TR.get(lang, []):
        s = s.replace(a, b)
    return s

def prefix(lang):  # url-prefix per taal
    return "" if lang == "nl" else lang + "/"

def rel(depth):
    return "../" * depth

def esc(s):
    return html.escape(s, quote=True)

SVG_FILTER = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="duo" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB"><feColorMatrix in="SourceGraphic" type="matrix" values=".33 .33 .33 0 0 .33 .33 .33 0 0 .33 .33 .33 0 0 0 0 0 1 0" result="g"/><feTurbulence type="fractalNoise" baseFrequency="GRAINF" numOctaves="2" seed="7" stitchTiles="stitch" result="n"/><feColorMatrix in="n" type="matrix" values=".33 .33 .33 0 0 .33 .33 .33 0 0 .33 .33 .33 0 0 0 0 0 0 1" result="ng"/><feComposite in="g" in2="ng" operator="arithmetic" k1="0" k2="1" k3="GRAINK" k4="GRAINOFF" result="m"/><feComponentTransfer in="m"><feFuncR type="table" tableValues=".72 1 1 1"/><feFuncG type="table" tableValues="0 .05 .5 .85 1"/><feFuncB type="table" tableValues="0 .05 .5 .85 1"/><feFuncA type="identity"/></feComponentTransfer><feComposite in2="SourceGraphic" operator="in"/></filter></svg>"""
GRAIN = {"f": ".62", "k": ".62", "off": "-.31"}
SVG_FILTER = SVG_FILTER.replace("GRAINF", GRAIN["f"]).replace("GRAINK", GRAIN["k"]).replace("GRAINOFF", GRAIN["off"])

def img_tag(key, root, alt="", cls="duo", sizes="(max-width: 760px) 100vw, 60vw", eager=False, zoom=True):
    w, h = dims(key)
    sm = f"{root}img/{key}-sm.jpg"; lg = f"{root}img/{key}.jpg"
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    z = f' data-full="{lg}"' if zoom else ""
    return (f'<img class="{cls}" src="{sm}" srcset="{sm} 760w, {lg} {w}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{esc(alt)}" {load} decoding="async"{z}>')

def page(lang, depth, path_nl, title, body, desc=None, og_img="portret", active=""):
    """path_nl: pad zonder taalprefix, bv 'werk/peer-gynt.html' of 'index.html'"""
    u = UI[lang]; root = rel(depth)
    full_title = f"{title} · {NAME[lang]}" if title else f"{NAME[lang]} · {u['title_suffix']}"
    canon = SITE + "/" + prefix(lang) + ("" if path_nl == "index.html" else path_nl)
    alts = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE}/{prefix(l)}{"" if path_nl=="index.html" else path_nl}">' for l in LANGS)
    def link(l):  # zelfde pagina in andere taal
        base = rel(depth) if lang == "nl" else rel(depth)  # root van huidige pagina
        return f"{base}{prefix(l)}{path_nl}".replace("index.html", "") or "./"
    langs_html = "".join(
        f'<li><a href="{link(l)}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l==lang else ""}>{UI[l]["lang_name"]}</a></li>' for l in LANGS)
    home = f"{root}{prefix(lang)}" or "./"
    nav = [("over", f"{root}{prefix(lang)}over.html"), ("agenda", f"{root}{prefix(lang)}agenda.html"), ("werk", f"{root}{prefix(lang)}werk.html")]
    nav_html = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k==active else ""}>{u[k]}</a>' for k, h in nav)
    aside = f"""
<aside class="info" aria-label="Contact">
  <a class="portrait" href="{root}{prefix(lang)}over.html">{img_tag(PORTRAIT['img'], root, NAME[lang], sizes='(max-width: 760px) 50vw, 18vw', zoom=False)}</a>
  <hr>
  <ul class="links">
    <li>→ <a href="mailto:{CONTACT['email']}">{u['email']}</a></li>
    <li>→ <a href="{CONTACT['instagram']}" rel="me">Instagram</a></li>
    <li>→ <a href="{CONTACT['antiklimax']}">Antiklimax</a></li>
  </ul>
  <p class="tel"><span aria-hidden="true">✆</span> <a href="tel:{CONTACT['phone_href']}">{CONTACT['phone']}</a></p>
  <ul class="langs">{langs_html}</ul>
  <p><a href="{home}">{u['home']}</a></p>
</aside>"""
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc or u['meta_desc'])}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc or u['meta_desc'])}">
<meta property="og:image" content="{SITE}/img/{og_img}.jpg">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#ff0000">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}fonts/courier-prime-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<a class="skip" href="#inhoud">{u['skip']}</a>
{SVG_FILTER}
<header class="top">
  <nav>{nav_html}<a class="name" href="{home}">{NAME[lang]}</a></nav>
</header>
<div class="wrap">
<main id="inhoud">
{body}
</main>
{aside}
</div>
<div class="lightbox" hidden><button type="button" aria-label="{u['close']}">×</button><img alt=""></div>
<script src="{root}site.js" defer></script>
</body>
</html>"""

def tr_label(lbl, lang):
    return lbl if lang == "nl" else CREDIT_LABELS[lang].get(lbl, lbl)

# ------------------------------------------------------------------ pagina's
def build_home(lang):
    u = UI[lang]; depth = 0 if lang == "nl" else 1; root = rel(depth)
    up = [w for w in WORK if w.get("upcoming")]
    recent = [w for w in WORK if not w.get("upcoming")][:3]
    def row(w):
        return (f'<li><a href="{root}{prefix(lang)}werk/{w["slug"]}.html"><span class="y">{w["year"]}</span> '
                f'<span class="t">{esc(w["title"])}</span> <span class="m">{esc(w["maker"][lang])}</span></a></li>')
    lead = HOME_LEAD[lang]
    titles = {w["slug"]: w["title"] for w in WORK}
    pool = [[k, w["slug"], w["title"]] for w in WORK
            for k in (([w["poster"]] if w.get("poster") else []) + w["imgs"])[:POOL_LIMIT.get(w["slug"], 99)]]
    pool_json = json.dumps(pool, ensure_ascii=False).replace("</", "<\\/")
    mosaic = "".join(f'<a data-k="{k}" class="{"poster" if k.startswith("poster") else "scene"}" href="{root}{prefix(lang)}werk/{sl}.html" title="{esc(titles[sl])}">'
                     f'{img_tag(k, root, titles[sl], sizes="(max-width: 520px) 50vw, (max-width: 860px) 33vw, 17vw", zoom=False)}</a>' for k, sl in MOSAIC)
    body = f"""
<div class="home">
  <figure class="home-img">{img_tag(HERO, root, "We zijn niet alleen", sizes="(max-width: 860px) 100vw, 40vw", eager=True)}
    <figcaption>{HERO_CAPTION[lang]}</figcaption></figure>
  <section class="home-lists">
    <p class="lead">{lead}</p>
    <p class="lead-src">— <a href="{root}{prefix(lang)}werk/hamlet-versus-don-quixote.html">{HOME_LEAD_SRC[lang]}</a></p>
    <h2>{u['binnenkort']}</h2>
    <ul class="mini">{''.join(row(w) for w in up)}</ul>
    <h2>{u['recent']}</h2>
    <ul class="mini">{''.join(row(w) for w in recent)}</ul>
    <p><a class="more" href="{root}{prefix(lang)}werk.html">→ {u['werk']}</a></p>
  </section>
</div>
<div class="mosaic" data-root="{root}{prefix(lang)}" data-img="{root}img/">{mosaic}</div>
<script type="application/json" id="pool">{pool_json}</script>"""
    return page(lang, depth, "index.html", "", body, og_img=HERO)

def build_werk(lang):
    u = UI[lang]; depth = 0 if lang == "nl" else 1; root = rel(depth)
    rows = []
    for w in WORK:
        th = img_tag(w.get("poster") or w["imgs"][0], root, "", sizes="120px", zoom=False) if (w.get("poster") or w["imgs"]) else '<span class="noimg" aria-hidden="true"></span>'
        st = f'<span class="status">{esc(w["status"][lang])}</span>' if w.get("status") else ""
        rows.append(f"""<li class="work">
  <a href="{root}{prefix(lang)}werk/{w['slug']}.html">
    <span class="y">{w['year']}</span>
    <span class="th">{th}</span>
    <span class="tt"><strong>{esc(w['title'])}</strong><span class="m">{esc(w['maker'][lang])}</span>{st}</span>
    <span class="r">{esc(w['role'][lang])}</span>
  </a>
</li>""")
    body = f"""<h1 class="pagetitle">{u['werk']}</h1>
<p class="note">{u['werk_intro']}</p>
<ol class="worklist" reversed>{''.join(rows)}</ol>"""
    return page(lang, depth, "werk.html", u["werk"], body, active="werk")

def build_prod(lang, w):
    u = UI[lang]; depth = 1 if lang == "nl" else 2; root = rel(depth)
    hero = f'<figure class="prod-hero">{img_tag(w["imgs"][0], root, w["title"], eager=True, sizes="(max-width: 760px) 100vw, 70vw")}</figure>' if w["imgs"] else ""
    text = "".join(f"<p>{p}</p>" for p in w["text"][lang])
    quotes = "".join(f'<blockquote><p>“{esc(q)}”</p><footer>— {esc(s)}</footer></blockquote>' for q, s in w["quotes"])
    credits = "".join(f"<dt>{esc(tr_label(a, lang))}</dt><dd>{esc(b)}</dd>" for a, b in w["credits"])
    dates = "".join(f"<li>{esc(tr_date(d, lang))}</li>" for d in w["dates"])
    gal = ""
    if len(w["imgs"]) > 1:
        gal = '<div class="gallery">' + "".join(
            f'<figure>{img_tag(k, root, w["title"] + " – " + u["photo"], sizes="(max-width: 760px) 50vw, 24vw")}</figure>' for k in w["imgs"][1:]) + "</div>"
    credit_line = f'<p class="photo-credit">{u["photo"]}: {esc(w["photo"])}</p>' if w["imgs"] and w["photo"] else ""
    st = f' · {esc(w["status"][lang])}' if w.get("status") else ""
    poster = f'<figure class="poster">{img_tag(w["poster"], root, w["title"] + " – poster", sizes="(max-width: 860px) 70vw, 24vw")}</figure>' if w.get("poster") else ""
    i = WORK.index(w)
    prev_w = WORK[i-1] if i > 0 else None; next_w = WORK[i+1] if i < len(WORK)-1 else None
    pn = '<nav class="pn">' + (f'<a href="{prev_w["slug"]}.html">← {esc(prev_w["title"])}</a>' if prev_w else "<span></span>") + \
         (f'<a href="{next_w["slug"]}.html">{esc(next_w["title"])} →</a>' if next_w else "") + "</nav>"
    body = f"""<article class="prod">
<p class="back"><a href="../werk.html">{u['terug']}</a></p>
<h1>{esc(w['title'])}</h1>
<p class="meta"><span>{w['year']}</span> · <span>{esc(w['maker'][lang])}</span>{st}<br><span class="role">{u['rol']}: {esc(w['role'][lang])}</span></p>
{hero}
<div class="cols">
  <div class="text">{text}{quotes}</div>
  <div class="facts">
    {poster}
    <h2>{u['credits']}</h2><dl>{credits}</dl>
    {f'<h2>{u["speellijst"]}</h2><ul class="dates">{dates}</ul>' if dates else ''}
  </div>
</div>
{gal}
{credit_line}
{pn}
</article>"""
    desc = re.sub("<[^>]+>", "", w["text"][lang][0])[:180]
    return page(lang, depth, f"werk/{w['slug']}.html", w["title"], body, desc=desc, og_img=(w["imgs"][0] if w["imgs"] else "portret"), active="werk")

def build_over(lang):
    u = UI[lang]; depth = 0 if lang == "nl" else 1; root = rel(depth)
    facts = "".join(f"<p>{p}</p>" for p in BIO[lang])
    own = "".join(f"<p>{p}</p>" for p in BIO_QUOTE[lang])
    body = f"""<h1 class="pagetitle">{u['over']}</h1>
<div class="over">
  <figure class="over-img">{img_tag(OVER_IMG['img'], root, OVER_IMG['alt'], sizes="(max-width: 860px) 100vw, 38vw", eager=True)}
    <figcaption>{u['photo']}: {OVER_IMG['credit']}</figcaption></figure>
  <div class="own">{own}</div>
  <div class="over-facts">{facts}<p class="also">{ALSO[lang]}</p>
    <p class="contactline">→ <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a></p></div>
</div>"""
    return page(lang, depth, "over.html", u["over"], body, active="over", og_img=OVER_IMG["img"])

def build_agenda(lang):
    u = UI[lang]; depth = 0 if lang == "nl" else 1; root = rel(depth)
    def block(ws, only_first=False):
        out = []
        for w in ws:
            ds = list(w["dates"])
            if not ds and w.get("status"):
                ds = [w["status"][lang]]
            for d in (ds[:1] if only_first else ds):
                out.append(f'<li><span class="d">{esc(tr_date(d, lang))}</span> <a href="{root}{prefix(lang)}werk/{w["slug"]}.html">{esc(w["title"])}</a></li>')
        return "".join(out)
    up = [w for w in WORK if w.get("upcoming")]
    recent = [w for w in WORK if not w.get("upcoming") and w["year"] == str(YEAR_NOW)]
    earlier = [w for w in WORK if not w.get("upcoming") and w["year"] != str(YEAR_NOW) and w["dates"]]
    body = f"""<h1 class="pagetitle">{u['agenda']}</h1>
<h2>{u['binnenkort']}</h2><ul class="agenda">{block(up)}</ul>
<h2>{u['recent']}</h2><ul class="agenda">{block(recent)}</ul>
<h2>{u['archief']}</h2><ul class="agenda">{block(earlier, only_first=True)}</ul>
<p class="note">{AGENDA_NOTE[lang]}</p>"""
    return page(lang, depth, "agenda.html", u["agenda"], body, active="agenda")

def write(path, s):
    p = os.path.join(OUT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)

def main():
    for lang in LANGS:
        pre = prefix(lang)
        write(pre + "index.html", build_home(lang))
        write(pre + "werk.html", build_werk(lang))
        write(pre + "over.html", build_over(lang))
        write(pre + "agenda.html", build_agenda(lang))
        for w in WORK:
            write(f"{pre}werk/{w['slug']}.html", build_prod(lang, w))
    # 404
    p404 = page("nl", 0, "index.html", "404",
          '<h1 class="pagetitle">404</h1><p>Deze pagina bestaat niet (meer). Een antiklimax.</p><p>This page does not exist. · Такой страницы нет.</p><p>→ <a href="/">home</a></p>')
    write("404.html", p404.replace("<head>", '<head>\n<base href="/">', 1).replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"', 1))
    # sitemap + robots
    urls = []
    for lang in LANGS:
        for p in ["", "werk.html", "over.html", "agenda.html"] + [f"werk/{w['slug']}.html" for w in WORK]:
            urls.append(f"{SITE}/{prefix(lang)}{p}")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "\n".join(f"<url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n")
    write("CNAME", "koenvanseuren.nl\n")
    # oude adressen doorsturen
    for lang in LANGS:
        for a, b in [("de-zelf-moordenaar", "de-zelfmoordenaar")]:
            write(f"{prefix(lang)}werk/{a}.html", f'<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="{b}.html"><meta http-equiv="refresh" content="0; url={b}.html"><a href="{b}.html">→</a>')  # eigen domein voor GitHub Pages
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    for f in ("style.css", "site.js", "favicon.svg"):
        shutil.copy(os.path.join(os.path.dirname(__file__), "static", f), os.path.join(OUT, f))
    fd = os.path.join(OUT, "fonts"); os.makedirs(fd, exist_ok=True)
    src = os.environ.get("FONTSRC", "/home/claude/fontsrc/node_modules/@fontsource/")
    for a, b in [("courier-prime/files/courier-prime-latin-400-normal.woff2", "courier-prime-400.woff2"),
                 ("courier-prime/files/courier-prime-latin-700-normal.woff2", "courier-prime-700.woff2"),
                 ("courier-prime/files/courier-prime-latin-400-italic.woff2", "courier-prime-400i.woff2"),
                 ("courier-prime/files/courier-prime-latin-ext-400-normal.woff2", "courier-prime-ext-400.woff2"),
                 ("pt-mono/files/pt-mono-cyrillic-400-normal.woff2", "pt-mono-cyr-400.woff2")]:
        if os.path.exists(src + a):
            shutil.copy(src + a, os.path.join(fd, b))
    print("klaar:", OUT)

if __name__ == "__main__":
    main()
