# generate html from markdown
# Usage: python gen_md.py

import markdown
import codecs


def gen_html(md_file):
    # read file
    with codecs.open(md_file, mode="r", encoding="utf-8") as f:
        md_text = f.read()

    # generate html
    html = markdown.markdown(md_text)

    # write file
    html_file = md_file.replace(".md", ".html")
    with codecs.open(html_file, mode="w", encoding="utf-8") as f:
        f.write(html)

    
gen_html('../md/test.md')