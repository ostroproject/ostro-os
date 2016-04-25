import os
import fileinput

CONST_PATH = os.path.dirname(os.path.realpath(__file__))

def insert_content(index, content, file_path):
    with open(file_path, 'r') as fp:
        contents = fp.readlines()
        fp.close()
        contents.insert(index, content)
        with open(file_path, 'w+') as fp:
            contents = ''.join(contents)
            fp.write(contents)
            fp.close()

def update_suite_js():
    file_path = os.path.join(
        CONST_PATH,
        'tests/suite.js'
        )

    for line in fileinput.input(file_path, inplace = True):
        new_line = line.replace('prefix: "tests"', 'prefix: "invasive-tests"')
        print new_line.strip('\n')

if __name__ == '__main__':
    update_suite_js()