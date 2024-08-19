#
# PyPSA documentation build configuration file, created by
# sphinx-quickstart on Tue Jan  5 10:04:42 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
from importlib.metadata import version as get_version

# Add the pypsa directory to the path
sys.path.insert(0, os.path.abspath(".."))

# For some reason is this needed, otherwise autosummary does fail on RTD but not locally
import pypsa  # noqa

# -- Version information -------------------------------------------------

# The short X.Y version.
release: str = get_version("pypsa")
version: str = ".".join(release.split(".")[:2])

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_reredirects",
    "nbsphinx",
    "nbsphinx_link",
    #    'sphinx.ext.pngmath',
    #    'sphinxcontrib.tikz',
    # 'rinoh.frontend.sphinx',
    "sphinx.ext.imgconverter",  # for SVG conversion
]

autodoc_default_flags = ["members"]
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "PyPSA"
copyright = "2015-2024 PyPSA Developers, see https://pypsa.readthedocs.io/en/latest/references/developers.html"
author = "PyPSA Developers, see https://pypsa.readthedocs.io/en/latest/references/developers.html"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_book_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "repository_url": "https://github.com/pypsa/pypsa",
    "use_repository_button": True,
    "show_navbar_depth": 1,
    "show_toc_level": 2,
}


# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "PyPSA: Python for Power System Analysis"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "PyPSA"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "img/pypsa-logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = ["theme_overrides.css"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "PyPSAdoc"

# -- Options for nbsphinx -------------------------------------------------
# nbsphinx_kernel_name = 'pypsa'
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None).replace("nblink", "ipynb").replace("examples/", "examples/notebooks/") %}
{% if env.config.release != 'master' %}
    {% set binder_url = 'https://mybinder.org/v2/gh/PyPSA/pypsa/v' + env.config.release + '?labpath=' + docname %}
{% else %}
    {% set binder_url = 'https://mybinder.org/v2/gh/PyPSA/pypsa/' + env.config.release + '?labpath=' + docname %}
{% endif %}

.. note::

    You can `download <https://github.com/pypsa/pypsa/tree/{{ env.config.release|e }}/{{ docname }}>`_ this example as a Jupyter notebook
    or start it `in interactive mode <{{ binder_url }}>`_.

"""

nbsphinx_allow_errors = True


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "PyPSA.tex", "PyPSA Documentation", "PyPSA Developers", "manual"),
]


# Added for rinoh http://www.mos6581.org/rinohtype/quickstart.html
rinoh_documents = [
    (
        master_doc,  # top-level file (index.rst)
        "PyPSA",  # output (target.pdf)
        "PyPSA Documentation",  # document title
        "PyPSA Developers",
    )
]  # document author


# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pypsa", "PyPSA Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "PyPSA",
        "PyPSA Documentation",
        author,
        "PyPSA",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

redirects = {
    # Redirects from old/ similar urls to new ones
    # Getting Started
    "introduction.html": "getting-started/introduction.html",
    "installation.html": "getting-started/installation.html",
    "setup.html": "getting-started/installation.html",
    "quick_start.html": "getting-started/quick-start.html",
    "quick-start.html": "getting-started/quick-start.html",
    "examples-basic.html": "getting-started/examples-basic.html",
    # User Guide
    "design.html": "user-guide/design.html",
    "components.html": "user-guide/components.html",
    "import_export.html": "user-guide/import-export.html",
    "power_flow.html": "user-guide/power-flow.html",
    "optimal_power_flow.html": "user-guide/optimal-power-flow.html",
    "contingency_analysis.html": "user-guide/contingency-analysis.html",
    "plotting.html": "user-guide/plotting.html",
    # Contributing
    "contributing.html": "contributing/contributing.html",
    "support.html": "contributing/support.html",
    "troubleshooting.html": "contributing/troubleshooting.html",
    "mailing_list.html": "contributing/mailing-list.html",
    # References
    "api_reference.html": "references/api-reference.html",
    "api-reference.html": "references/api-reference.html",
    "api.html": "references/api-reference.html",
    "release_notes.html": "references/release-notes.html",
    "release-notes.html": "references/release-notes.html",
    "citing.html": "references/citing.html",
    "users.html": "references/users.html",
    "developers.html": "references/developers.html",
}
