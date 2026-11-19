# Maison Baer

Website for Maison Baer, a private dinner club.

Live (GitHub Pages): https://hxbaer.github.io/maisonbaer/

## Files

- `index.html`: the house page (ivory paper, Baer coat of arms). One self-contained file: HTML, CSS and JS.
- `history.html`: History (name, arms, why the club exists). `house.html` forwards there.
- `membership.html`: Membership (introduction by two guests, request button).
- `legal.html`: Legal Notice in English.
- `img/`: coat of arms and four watercolours, painted from photos on Unsplash (Unsplash License): Grossmünster at dusk and Bauschänzli in the blue hour (home, photos by Claudio Schwarz and Manuela Pezone), an old wooden door (History, photo by Joel & Jasmin Førestbird), the Limmat with St. Peter (Membership, photo by Tomi Blasic).
- `tools/watercolour.py`: the Python/OpenCV filter that turned the photos into the paintings.

## Notes

- The password page has been removed; the site opens directly on the house page.
- The two paintings sit still in the corners on wide screens (Grossmünster top right, Quaibrücke bottom left) and fade into the paper without a visible edge; on phones, one sits under the title and the other after the text, each in a soft vignette.
- Fonts: Cormorant Garamond, Cormorant SC and EB Garamond, self-hosted in `fonts/` (latin subset, from Fontsource; SIL Open Font License). No requests go to Google. The signature under the home text uses Monsieur La Doulaise (SIL Open Font License), also self-hosted.
