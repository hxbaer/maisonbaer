# Maison Baer

Members-only website for Maison Baer, a private dinner club. One table, seven guests, never an eighth.

Live (GitHub Pages): https://hxbaer.github.io/maisonbaer/

## Files

- `index.html`: the house page (ivory paper, Baer coat of arms). One self-contained file: HTML, CSS and JS.
- `legal.html`: Legal Notice in English.
- `img/`: coat of arms and four watercolour paintings of Zürich (Seeufer, Innenhof, Grossmünster, Quaibrücke).
- `tools/watercolour.py`: the Python/OpenCV filter that turned the photos into the paintings.

## Notes

- The password page has been removed; the site opens directly on the house page.
- The painting gallery is switched off for now (`hidden` on `.gallery`, `startGallery()` commented out).
- Fonts: Cormorant Garamond, Cormorant SC and EB Garamond, self-hosted in `fonts/` (latin subset, from Fontsource; SIL Open Font License). No requests go to Google.
