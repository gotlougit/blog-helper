# blog-helper
Small program to add templates and add blogpost entry to main webpage with easy customization settings. 

It utilizes only the builtin modules and is a pretty small code base to understand for easy maintenance and extensibility. 

## Requirements
In the website folder, ie, the place where your website is stored, you MUST have a ```templates/``` folder with the following three files:
- head.html: this is what gets added at the top of the webpage
- foot.html: this is what gets added at the bottom of the webpage
- entry.html: this is how each blog entry will be added to the main webpage

If you want an rss feed as well, the following 3 files will also be needed in the ```templates/``` folder:

- rsshead.xml: corresponds to head.html for rss feed
- rssfoot.xml: corresponds to foot.html for rss feed
- rssentry.xml: corresponds to entry.html for rss feed

Note: the names of these files can be customized in your ```web_config.json``` file; if you run the program once it will automatically be created.

## Installation

First clone this repository by typing

```git clone https://github.com/gotlougit/blog-helper.git``` in the terminal.

Then, ```cd blog-helper```

And finally, ```pip install .```

## Usage

- First initialize the program

```bash
python3 -m blog-helper init
```

This creates the ```web_config.json``` file that has lots of configuration options. 
Edit this file to specify the name of your:

     * head file
     * foot file
     * entry file
     * index file (this is the main webpage where each post will be added)
     * the comment style for specifying that your file's head has ended, or your file's foot is beginning
     * enabling rss feed
     * main page link for your website
     * date and timestamp with custom formatting 
     * custom placeholders for content
     * and much more!
     
These are pretty self-explanatory, but a more detailed explanation of each variable found in the file will be written at a later date.

Note: some of these options are intended for future features, so don't mess around with those until the feature has been added.

Check [this link](https://www.tutorialspoint.com/python/time_strftime.htm)  for details on custom layouts (look for Directive) 

After this, go ahead and edit certain parameters to your liking, like if you want rss enabled

- Add rss feed (make sure to set rss to 1 in json file and pagelink to your website in ```web_config.json``` file)

```bash
python3 -m blog-helper add-rss
```

You HAVE to run this command, as this creates the ```rss.xml``` file (as per default settings) where your rss feed resides.

- Add templates to given webpage FILENAME (this is known as polish).

This will also modify your ```<title>``` tag value if you write title placeholder in the ```head.html``` template. So for example, ```<title>this is a title</title>``` will become ```<title>Hello world!</title>``` if your content starts with ```<h1 id='...'>Hello world!</title>```

```bash
python3 -m blog-helper add-polish FILENAME
```

- Add entry to the main webpage (if rss has already been enabled it will add an entry to the rss feed as well)

```bash
python3 -m blog-helper add-entry FILENAME
```

- Update polish for a webpage

```bash
python3 -m blog-helper update-polish FILENAME
```

- Update polish for index.html

```bash
python3 -m blog-helper update-index FILENAME
```

## Upcoming Features

- Adding a "last updated" feature

- PyPI installation method: to encourage easy usage via the command line, which is what this project is all about

- Sample templates so that it can be cleared up how to write these; these will be uploaded soon to this repo

- RSS feed customization, such as adding images, author's email and other info

- Pages of ```index.html``` so that it doesn't just load an extremely long page of blog posts ;)
