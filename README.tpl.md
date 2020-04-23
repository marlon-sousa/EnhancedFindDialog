# EnhancedFindDialog for NVDA ${addon_version}
Enhanced find dialog addon for NVDA, implementing search improvements:
* search history

## Download
Download the [Enhanced Find Dialog ${addon_version} addon](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Features

### Search history
In many web sites and web applications, the fastest way to access specific places is by using the search command, often bound to ctrl + nvda + f keys.

The search dialog allows us to type a text and be placed on the next occurrence of that text if it exists.

In many cases, you will find yourself visiting the same web sites several times during the same NVDA session. In many of these web sites you will need to search for the same terms, specially if this is the only way to get quickly to a link or section of that web site.

This is specially the case of people who work on a daily basis with web based systems as part of their jobs.

However, NVDA does not keep the previous terms you searched on a list. This slows down your productivity, because unless you are searching for the exact same term of your last search, you have to type it again.

This addon keeps a search history that lasts as long as NVDA is running. So, on activation, you just need to press down arrow and choose previously searched terms to perform a new search.

You can of course type new terms. They will also be added to the list next time you activate the search dialog.

#### How it works?

Simply install the addon. When it is activated, pressing down and up arrows on the edit field on the search dialog will let you navigate through the list of previously searched terms.

You can at any time type a new term as usual.

## Contributing

### building the addon

You will need:

* python 3.6 or above.
* pip must be configured
* scons (pip install scons)
* markdown (pip install markdown)
* msgfmt utility. The easiest way of getting it is by installing git bash and choosing to include bash tools at command prompt

Once you have everything installed, issuing scons at the root of the project should build the addon and generate docs.

### translations

#### translating the addon

Assuming you have everything set up to build the addom (see previous topic) issuing scons pot should generate a pot file at the root project directory. It is them possible to generate and contribute the .po files for your language.
Current languages can be found at /addon/locale directory

#### translating documentation

Documentation translations are generated from .tpl.md (not from .md) files. This is why, except from this file (read.md) at the root of the project, you won't find other .md files.

The .tpl.md files are normal markdown files with one addition: if you use ${[var]} within its text, [var] will be replaced by a var with the same name defined in buildvars.py when the corresponding md and.html files are generated.

If no variable with that name exists, the substitution doesn't take place.

This is useful for example to generate links and titles with the addon version included without having to rewrite documentation.

To translate documentation, grab the readme.tpl.md file at the root of the project and translate it. The translated file must be named readme.tpl.md and must be placed inside the addon/doc/[lang] directory.

The ${[xxx]} vars need to stay untouched. To generate the docs, issue scons and the markdown and HTML will be generated.
