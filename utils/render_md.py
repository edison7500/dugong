import markdown

md = markdown.Markdown(extensions=[
    "markdown.extensions.extra",
    "markdown.extensions.headerid",
    "markdown.extensions.codehilite",
    "markdown.extensions.sane_lists",
    "markdown.extensions.toc",

    "pymdownx.arithmatex",
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.tilde",
    "pymdownx.emoji",
    "pymdownx.tasklist",
    "pymdownx.superfences",
],)
