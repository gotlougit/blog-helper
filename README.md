# blog-helper
Small script to add templates and add blogpost entry to main webpage with easy customization settings.

## Requirements
In the website folder, ie, the place where your website is stored, you MUST have a ```templates/``` folder with the following three files:
- head.html: this is what gets added at the top of the webpage
- foot.html: this is what gets added at the bottom of the webpage
- entry.html: this is how each blog entry will be added to the main webpage

Note: the names of these 3 files can be customized in your ```web_config.json``` file (if you run the program once it will automatically be created.

## Installation

Coming soon! Right now, just download the two files ```config.py``` and ```main.py``` and place them in the website folder

## Usage

- Add templates to given webpage FILENAME (this is known as polish)

```bash
python3 main.py add-polish FILENAME
```

If you are running this command for the first time, there will be a single line of output as such: 

```config file not found! creating one with default values..```

This creates a file called ```web_config.json`` in your website folder. Edit this file to specify the name of your:

     * head file
     * foot file
     * entry file
     * index file (this is the main webpage where each post will be added
     * the comment style for specifying that your file's head has ended, or your file's foot is beginning
     * and much more!

- Add entry to the main webpage

```bash
python3 main.py add-entry FILENAME
```

- Update polish for a webpage

```bash
python3 main.py update-polish FILENAME
```
