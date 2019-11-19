# Contributing to Latex-Access
If you would like to contribute code or documentation to Latex-Access, please follow these guidelines.

## Submitting Changes
For anything other than minor bug fixes, please comment on an existing issue or create a new issue providing details about your proposed change. Unrelated changes should be addressed in separate issues. Include information about use cases, design, user experience, etc. This allows us to discuss these aspects and any other concerns that might arise, thus potentially avoiding a great deal of wasted time. You should generally wait for acceptance of your proposal before you start coding. Please understand that we very likely will not accept changes that are not discussed first.
If this is a minor/trivial change which definitely wouldn't require design, user experience or implementation discussion (i.e. a fix for a typo/obvious coding error), you can just create a pull request rather than using an issue first. However, this should be fairly rare. If in doubt, use an issue first. Use this issue to discuss the alternatives you have considered in regards to implementation, design, and user experience. Then give people time to offer feedback.
If this is your first contribution, you will first need to "fork" the latex-access repository on GitHub.
When you fork the repository, GitHub will create a copy of the master branch. However, this branch will not be updated when the official master branch is updated. To ensure your work is always based on the latest commit in the official master branch, it is recommended that your master branch be linked to the official master branch, rather than the master branch in your GitHub fork. If you have cloned your GitHub fork, you can do this from the command line as follows:

```
# Add a remote for the SugarCaneNS latex-accessrepository.
git remote add SugarCaneNS https://github.com/SugarCaneNS/latex-access.git
# Fetch the SugarCaneNS branches.
git fetch SugarCaneNS
# Switch to the local master branch.
git checkout master
# Set the local master to use the SugarCaneNS master as its upstream.
git branch -u SugarCaneNS/master
# Update the local master.
git pull
```
You should use a separate "topic" branch for each issue. All code should usually be based on the latest commit in the official master branch at the time you start the work unless the code is entirely dependent on the code for another issue. Branches should never be based on the "next" branch.
If you are adding a feature or changing something that will be noticeable to the user, you should update the User Guide accordingly.
When it is time to submit your code, you should open a pull request referring to the original issue. Code review will then be done on this pull request.

## Code Style
### Encoding
* Where Python files contain non-ASCII characters, they should be encoded in UTF-8.
	* There should be no Unicode BOM at the start of the file, as this unfortunately breaks one of the translation tools we use (xgettext). Instead, include this as the first line of the file (only if the file contains non-ASCII characters):
```# -*- coding: UTF-8 -*-```
	* This coding comment must also be included if strings in the code (even strings that aren't translatable) contain escape sequences that produce non-ASCII characters; e.g. `\xff`. This is particularly relevant for braille display drivers. This is due to a gettext bug; see https://github.com/nvaccess/nvda/issues/2592#issuecomment-155299911.

### Indentation
* Indentation must be done with tabs (one per level), not spaces.
* When splitting a single statement over multiple lines, just indent one or more additional levels. Don't use vertical alignment; e.g. lining up with the bracket on the previous line.
	* Be aware that this requires a new-line after an opening parenthesis/bracket/brace if you intend to split the statement over multiple lines.
	* For the parameter list of function definitions, double indent, this differentiates the parameters and the body of the function.

### Identifier Names
* Use descriptive names
	* name constants to avoid "magic numbers" and hint at intent or origin of the value. Consider, what does this represent?
* Functions, variables, methods, properties, etc. should use mixed case to separate words, starting with a lower case letter; e.g. speakText.
* Boolean functions or variables
	* should try to use the positive form of the language (to avoid double negatives like shouldNotDoSomething = False)
	* start with a "question word" to hint at their boolean nature. EG shouldX, isX, hasX
* Classes should use mixed case to separate words, starting with an upper case letter; e.g. GlobalPlugin.
* Constants should be all upper case, separating words with underscores; e.g. LANGS_WITH_CONJUNCT_CHARS.
* For the NVDA addon, event handlers are prefixed with "event_", and are often in the form "event_ACTION" or "event_OBJECT_ACTION". Where OBJECT refers to the class type that the ACTION refers to.

### Translatable Strings (For the NVDA Addon):
* All strings that could be presented to the user should be marked as translatable using the _() function; e.g. _("Text review").
* All translatable strings should have a preceding translators comment describing the purpose of the string for translators. For example:
```
# Translators: The name of a category of NVDA commands.
SCRCAT_TEXTREVIEW = _("Text review")
```