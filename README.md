# blog-helper
Small script to add templates and add blogpost entry to main webpage with easy customization settings. 

It utilizes only the builtin modules and is a pretty small code base to understand for easy maintenance and extensibility. 

## Requirements
In the website folder, ie, the place where your website is stored, you MUST have a ```templates/``` folder with the following three files:
- head.html: this is what gets added at the top of the webpage
- foot.html: this is what gets added at the bottom of the webpage
- entry.html: this is how each blog entry will be added to the main webpage

Note: the names of these 3 files can be customized in your ```web_config.json``` file (if you run the program once it will automatically be created.

## Installation

Coming soon! Right now, just download the two files ```config.py``` and ```main.py``` and place them in the website folder

## Usage

- First initialize the program

```bash
python3 main.py init
```

This creates the ```web_config.json``` file that has lots of configuration options. 
Edit this file to specify the name of your:

     * head file
     * foot file
     * entry file
     * index file (this is the main webpage where each post will be added
     * the comment style for specifying that your file's head has ended, or your file's foot is beginning
     * and much more!
     
Note: some of these options are intended for future features, so don't mess around with those until the feature has been added.

- Add templates to given webpage FILENAME (this is known as polish)

```bash
python3 main.py add-polish FILENAME
```

- Add entry to the main webpage

```bash
python3 main.py add-entry FILENAME
```

- Update polish for a webpage

```bash
python3 main.py update-polish FILENAME
```

## Upcoming Features

- RSS feed maker: this goes almost hand in hand with a typical blog, so this is one feature that will be pretty important.

- PyPI installation method: to encourage easy usage via the command line, which is what this project is all about
