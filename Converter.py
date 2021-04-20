import os
import markdown 

def getMarkdownFilesFromDirectory(directory): 
    files = []

    with os.scandir(directory) as dir:
        for entry in dir: 
            if(entry.is_dir()):
                files += (getMarkdownFilesFromDirectory(entry.path))
            else: 
                files.append(entry)
    return files 


files = getMarkdownFilesFromDirectory("input")


for f in files:

    filename = os.path.splitext(f.name)[0]
    with open(f.path) as input: 
        text = input.read()
        html = markdown.markdown(text)
    with open("output/{file}.html".format(file=filename), 'w+') as output:
        output.write(html)
