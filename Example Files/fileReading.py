def numChars(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()
    return len(content)

def numLines(filename):
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    return len(lines)

def numWords(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()
    return len(content.split())
