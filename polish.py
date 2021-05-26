#module full of relevant functions for polishing webpages

def readFile(filename):
    with open(filename) as f:
        return f.read()

def addPolish(content):
    head = readFile(head_path)
    foot = readFile(foot_path)

    new_content = head + content + foot
    return new_content

def removePolish(content):
    
    raw_content = content.partition(head_end)[-1].partition(foot_start)[0]
    return raw_content

def polishFile(filename):
    f = readFile(filename)
    newfile_content = addPolish(f)

    with open(filename,'w') as nf: 
        nf.write(newfile_content)

def updatePolish(filename):
    old_content = readFile(filename)
    raw_content = removePolish(old_content)
    new_content = addPolish(raw_content)
    
    with open(filename,'w') as nf: 
        nf.write(new_content)

def addEntry(heading,rel_filename,desc):
   
    entry = open(entry_path).read()

    new_entry = entry.replace(title_temp,heading)
    new_entry = new_entry.replace(link_temp,rel_filename)
    new_entry = new_entry.replace(desc_temp,desc)

    index_content = readFile(index_path)
    raw_index = removePolish(index_content)
    new_content = addPolish(new_entry + raw_index)
    
    with open(index_path,'w') as nf:
        nf.write(new_content)

