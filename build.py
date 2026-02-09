from jinja2 import Environment, PackageLoader, select_autoescape
import glob
import os
from markdown_it import MarkdownIt
import shutil
from pathlib import Path
from markdown_it.renderer import RendererHTML

# -- utils

def get_output_location(page):
    return sanitize(f"out/{page.removeprefix('pages/').split('.')[0]}.html", allow="/-_.")

def sanitize(text, allow="-_"):
    return ''.join(filter(lambda x: x in allow or x.isalnum(), text.lower().replace(" ","-")))

def get_articles():
    for file in glob.glob("pages/articles/*.md"):
        yield {"path": get_output_location(file), "name": file.split("/")[-1].removesuffix(".md")}

def get_challenges():
    for file in glob.glob("pages/challenges/**/*.md"):
        yield {"path": get_output_location(file), "name": file.split("/")[-2].removesuffix(".md")}

# -- actual build

env = Environment(
    loader=PackageLoader("build", ""),
    autoescape=False
)
env.globals.update(get_articles=get_articles, get_challenges=get_challenges)

if os.path.exists("out/"):
    shutil.rmtree("out/")
os.mkdir("out")

for page in glob.glob("pages/**/*.*", recursive=True):
    if page.endswith(".html"):
        template = env.get_template(page)
        rendered = template.render()
    if page.endswith(".md"):
        md = MarkdownIt()

        def render_open(renderer, tokens, idx, options, env):
            tokens = tokens[idx:]

            # find tag with any content
            content_head = next(filter(lambda x: len(x.content) > 0, tokens))

            sanitized = sanitize(content_head.content)

            return f"<{tokens[0].tag}><a class='anchor' href='#{sanitized}' id='{sanitized}'># </a>"

        md.add_render_rule("heading_open", render_open)

        rendered_md = md.render(open(page).read())
        template = env.get_template("templates/article.html")
        rendered = template.render(md=rendered_md)

    output_location = Path(get_output_location(page))
    output_location.parent.mkdir(exist_ok=True, parents=True)

    open(output_location, "w+").write(rendered)