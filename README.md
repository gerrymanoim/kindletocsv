# Kindle Definitions to CSV

Words you've looked up on the kindle, defined and thrown into a csv file (for later imports into Anki). 

## A Note on Dictionaries 

After reading [this fantstic article on dictionaries](https://jsomers.net/blog/dictionary) I've been using Webster's 1913 dictionary on my kindle. I wanted to have the same definitions in my csv. Originally I was going to parse the [Project Gutenberg Version](http://www.gutenberg.org/ebooks/29765), but luckily I found [GCIDE](https://gcide.gnu.org.ua/) which I read via [Dico](http://puszcza.gnu.org.ua/software/dico/dico.html). Opening a subprocess to read every definition is a bit slow for larger highlight lists. 

## Usage

- Get vocab.db file from Kindle and put copy it over somewhere
    * Located in /Volumes/Kindle/system/vocabulary/ (make sure you have show hidden files turned on)
- `python kindledefine.py --help`
