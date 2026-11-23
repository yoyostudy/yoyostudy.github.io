import sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page()
    pg.goto("file://" + src)
    pg.pdf(path=out, format="Letter", prefer_css_page_size=True, display_header_footer=True,
           header_template="<div></div>",
           footer_template='<div style="width:100%;text-align:center;font-family:\'TeX Gyre Pagella\',Palatino,serif;font-size:9.5pt;"><span class="pageNumber"></span></div>')
    b.close()
