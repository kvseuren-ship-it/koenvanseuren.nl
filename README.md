# koenvanseuren.nl

Persoonlijke site van Koen van Seuren (NL / EN / RU). Statisch; gehost op GitHub Pages vanuit deze opslagplaats (map `site/`, workflow in `.github/workflows/pages.yml`).

- `build/content.py`: alle tekst (bio, eigen tekst, producties, credits, speeldata, vertalingen).
- `build/build.py`: maakt alle pagina's in `site/` (`cd build && python3 build.py`).
- `build/static/`: CSS, JS, favicon.
- `site/`: de gepubliceerde site. Elke push naar `main` gaat automatisch live.

Foto's in `site/img/` zijn verkleind (1600 px en `-sm` 760 px) en worden in de browser rood duotoon met korrel (SVG-filter in `build.py`); bij hover verschijnt de kleur.
