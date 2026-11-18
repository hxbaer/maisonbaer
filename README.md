# Maison Baer

Members-only website for Maison Baer, a private dinner club. One table, seven guests, never an eighth.

Live (Wix Headless): https://headless-vnosfbwpdpi-hxbaer1-1407.wix-site-host.com/

## Files

- `index.html`: the house page (ivory paper, Baer coat of arms). One self-contained file: HTML, CSS and JS.
- `legal.html`: Legal Notice in English. Name and address are still placeholders.
- `img/`: coat of arms and four watercolour paintings of Zürich (Seeufer, Innenhof, Grossmünster, Quaibrücke).
- `tools/watercolour.py`: the Python/OpenCV filter that turned the photos into the paintings.

## Notes

- The password page has been removed; the site opens directly on the house page.
- The live Wix site loads its images from Wix Media. In this copy, the paths point to `img/`.
- The painting gallery is switched off for now (`hidden` on `.gallery`, `startGallery()` commented out).
- Fonts: Cormorant Garamond, Cormorant SC and EB Garamond from Google Fonts.
