import os
import markdown 

from sys import argv
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('src/templates'))

def getMarkdownFilesFromDirectory(directory): 
    files = []
    with os.scandir(directory) as dir:
        for entry in dir: 
            if(entry.is_dir()):
                files += (getMarkdownFilesFromDirectory(entry.path))
            else: 
                files.append(entry)
    return files 

def getFoldersFromDirectory(directory):
    folders = []
    with os.scandir(directory) as dir:
        for entry in dir: 
            if(entry.is_dir()):
                folders.append(entry)
    return folders 

def getReferences(files):
    references = []
    for f in files:
        filename = os.path.splitext(f.name)[0].capitalize()
        references.append(filename)
    return references

def writeToFile(f, references):
    filename = os.path.splitext(f.name)[0]
    md = markdown.Markdown(extensions=['toc'])
    with open(f.path) as input: 
        text = input.read()
        html = md.convert(text)

    template = env.get_template('page.html')
    with open("output/{file}.html".format(file=filename), 'w+', encoding="utf-8") as output: 
        template_data = template.render(html=html, references=references)
        output.write(template_data)

def main(folder):
    files = getMarkdownFilesFromDirectory(folder)
    references = getReferences(files)

    for f in files:
        print("Processing file: {file}".format(file=f.name))
        writeToFile(f, references)

if __name__ == "__main__":
    folder = str(argv[1]) 
    main(folder)