import markdown

md = markdown.Markdown(extensions=["markdown.extensions.extra",
                                   "markdown.extensions.headerid",
                                   "markdown.extensions.codehilite",
                                   "markdown.extensions.sane_lists",
                                   "markdown.extensions.toc",
                                   "markdown.extensions.nl2br",
                                   ], )