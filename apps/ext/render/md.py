import markdown


_extension_configs = {"codehilite": {"linenums": True}}


md = markdown.Markdown(
    output_format="html",
    extensions=[
        "markdown.extensions.extra",
        # "markdown.extensions.headerid",
        "markdown.extensions.codehilite",
        "markdown.extensions.sane_lists",
        "markdown.extensions.toc",
        "markdown.extensions.fenced_code",
        "pymdownx.arithmatex",
        "pymdownx.magiclink",
        "pymdownx.betterem",
        "pymdownx.tilde",
        "pymdownx.emoji",
        "pymdownx.tasklist",
        "pymdownx.superfences",
    ],
    extension_configs=_extension_configs,
)
