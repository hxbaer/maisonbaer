# Maison Baer

Members-only website for Maison Baer, a private dinner club. One table, seven guests, never an eighth.

Live (Wix Headless): https://headless-vnosfbwpdpi-hxbaer1-1407.wix-site-host.com/

## Files

- `index.html`: password gate (dark green door with the Baer coat of arms) and the house page (ivory paper). One self-contained file: HTML, CSS and JS.
- `legal.html`: Legal Notice in English. Name and address are still placeholders.
- `img/`: coat of arms and four watercolour paintings of Zürich (Seeufer, Innenhof, Grossmünster, Quaibrücke).
- `tools/watercolour.py`: the Python/OpenCV filter that turned the photos into the paintings.

## Notes

- Code: `7`. It is checked against a SHA-256 hash in the browser. This is a soft gate, not real access control: anyone who reads the source can see the content.
- The live Wix site loads its images from Wix Media. In this copy, the paths point to `img/`.
- The painting gallery is switched off for now (`hidden` on `.gallery`, `startGallery()` commented out).
- Fonts: Cormorant Garamond, Cormorant SC and EB Garamond from Google Fonts.
