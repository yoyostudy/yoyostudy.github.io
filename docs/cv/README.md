# CV source

`cv.html` is the source of `assets/CV.pdf`. To rebuild the PDF:

```
pip install playwright && playwright install chromium
python render.py "$(pwd)/cv.html" ../../assets/CV.pdf
```

`render.py` uses Google Chrome at `/usr/bin/google-chrome`; change `executable_path` (or remove it to use Playwright's Chromium) on another machine. Fonts: Palatino and Gill Sans (TeX Gyre Pagella and Gillius ADF work as substitutes).

This folder is under `docs/`, which `_config.yml` excludes from the Jekyll build, so it is not published on the site.
