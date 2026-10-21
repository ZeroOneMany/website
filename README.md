# Zero One Many, site source

This branch holds the source of zeroonemany.com. The live site is the `main` branch, served by GitHub Pages. Nothing on this branch is published.

## Layout

- `web/build.py`: the generator. All page text (FR and EN) lives in the `FR` and `EN` dictionaries at the top. Switches: `BOOKING` (HubSpot meeting link), `SHOW_PRICES`, `SHOW_LEGAL`.
- `web/assets/`: stylesheet, fonts (Inter, self hosted), logo mark, favicons, OG image, portrait.
- `web/mkog.py`: regenerates the OG image (needs `logo/make_logos.py`).
- `logo/`: logo generator and exported brand files (monogram 01M, palette #111111 / #FFFFFF / #E8590C).
- `photo/`: portrait cutout and `portrait.py`, which rebuilds `web/assets/nicolas.jpg`.

## Build and deploy

```
cd web
python3 build.py          # writes dist/ (production) and preview/ (local preview with index.html links)
```

Then replace the content of the `main` branch with `web/dist/` and push. Pages republishes within a minute or two.

## Rules kept on purpose

- The contact address is never written in clear, here or in the HTML: it is stored reversed and assembled on click.
- No cookies, no analytics, no third party scripts. Booking opens HubSpot in a separate page.
- No em or en dashes in site copy.
- The logo scripts read Inter from system fonts (`/usr/share/fonts/opentype/inter/`); install the Inter font package if missing.
