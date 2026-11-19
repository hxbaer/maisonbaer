# Maison Baer

Website for Maison Baer, a private dinner club.

Live (GitHub Pages): https://hxbaer.github.io/maisonbaer/

## Files

- `index.html`: the house page (ivory paper, Baer coat of arms). One self-contained file: HTML, CSS and JS.
- `house.html`: The House (name, arms, origin).
- `membership.html`: Membership (introduction by two guests, request button).
- `legal.html`: Legal Notice in English.
- `img/`: coat of arms and four watercolour paintings of Zürich: Grossmünster and Quaibrücke (home), a courtyard with a fountain (The House), Augustinergasse (Membership).
- `tools/watercolour.py`: the Python/OpenCV filter that turned the photos into the paintings.

## Notes

- The password page has been removed; the site opens directly on the house page.
- The two paintings sit still in the corners on wide screens (Grossmünster top right, Quaibrücke bottom left) and fade into the paper without a visible edge; on phones, one sits under the title and the other after the text, each in a soft vignette.
- Fonts: Cormorant Garamond, Cormorant SC and EB Garamond, self-hosted in `fonts/` (latin subset, from Fontsource; SIL Open Font License). No requests go to Google.
