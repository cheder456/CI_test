
def create_file(filename):
    f = open(filename + ".txt", "x")
    f.close()
    return {'Done': 1}

def read_file(filename):
    f = open(filename + ".txt", "r")
    content = f.read()
    return {'content': content}

def change_file_content(filename, content):
    f = open(filename + ".txt", "w")
    f.write(content)
    f.close()
    return {'Done': 1}
