# EnhancedFindDialog for NVDA ${addon_version}
Enhanced find dialog addon for NVDA, implementing search improvements:

* search history
* search wrapping, configured per profile
* case sensitivity, configured per profile
* contextual information on searches

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

### Search wrapping

Search Wrapping is a feature that, if configured, doesn't consider the current position you are on a text when performing searches.

This means that if you search for something that is not present below your current position, search will be performed from the beginning of the text to check if this term exists somewhere in the whole text.

This is specially important to people who work with web based systems and need to find a given button or piece of text regardless of where they are on the page.

This option is profile specific, meaning that you can have a profile where it is active and other where it isn't.

#### How it works?

Simply install the addon. When it is activated, the find dialog will offer a checkbox called search wrap.

If it is checked:

1. Iff you search for a term and it is found below the current position, you will be placed on that text.
2. If this term is not found below the current position, it will be searched from the top of the text.
3. If the term is found, a short beep is produced to let you know that the text found is above your current position and you are placed at its position.
4. If this term isn't found at all, then the text not found message is displayed.

Changing this check box and performing a search will save the new state (checked or unchecked) for the active profile. Canceling the search won't change its state on the active profile, even if you changed it before canceling the search.

### case sensitivity

NVDA already offers the case sensitivity checkbox to allow searches considering case. This addon extends this functionality by saving the state of this checkbox in the active profile, so that you can have profiles with this configured differently.

#### How it works?

Simply install the addon. Changing the case sensitivity check box and performing a search will save the new state (checked or unchecked) for the active profile. Canceling the search won't change its state on the active profile, even if you changed it before canceling the search.

### contextual information on searches

The way NVDA behaves when a search term is found is the following: you are placed at the position of the searched term and the line is read from the searched term on.

This has always been problematic when you need to search several times (by using NVDA + f3) for something, because the first thing you listen is the searched term itself, when you know that term because you just searched for it.

This addon places the cursor at the position of the term, but instead of reading from the term on it reads the full line, gibing you the context where that term was found.

For example, supose you are searching for "Marlon" because you know that there is a button called target Marlon somehwere. You don't want to search for target, because there are other buttons called "target x y z" and you want to find the target Marlon Button.

Here is the text:

Delete Marlon comments

reply directly to Marlon

Report Marlon as spammer

Target Marlon on a response

If you would search for Marlon before this block, you would hear
Marlon Comments

If you keept pressing NVDA + f3 you would hear

Marlon

Marlon as spammer

Marlon on a response

This would reduce your productivity because first you would hear only marlon, without knowing nothing about this ocurrence.

The next time, you would hear Marlon and would have to wait for as spammer to be spoken, because  you wouldn't know either what is about Marlon on this text.

Similarly, the next time you would need to wait for on a response to be spoken, because you wouldn't be sure about what was this thing about Marlon either.

Further more, if you pressed NVDA + f3 quickly, you would hear Marlon, Marlon, Marlon, Marlon ... which is not productive cinse you know you are searching for Marlon.

#### How it works

Simply install the addon.

After it is installed, the current line of the found search term is read and you are placed at the term on it.

In our example above, at The first time you performed the search you would hear

Delete Marlon comments

If you keept pressing NVDA + f3 you would hear

reply directly to Marlon

Report Marlon as spammer

Target Marlon on a response

Further more, if you pressed NVDA + f3 quickly, you would hear the beginning of each line, allowing you to quickly hit enter on the target line because you know that Marlon is present att a latter position on that same line.

## Contributing and translating

If you want to contribute or translate this addon, please access the [project repository](https://github.com/marlon-sousa/EnhancedFindDialog) and find instructions on the contributing.md in the english documentation directory.

## Contributors

Special thanks to


* Ângelo Miguel Abrantes - Portuguese translation
* Rémy Ruiz - French translation
* Rémy Ruiz - Spanish translation
* Tarik Hadžirović - Croatian translation
*  Thiago Seus - Brazilian Portuguese translation
* Umut KORKMAZ - Turkish translation
* Valentin Kupriyanov - Russian translation
