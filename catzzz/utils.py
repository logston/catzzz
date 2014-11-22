import os


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def generate_cats():
    with open(os.path.join(CURRENT_DIR, 'ascii_catzzz.txt')) as fd:
        ascii_catzzz_lines = fd.readlines()

        cat_lines = []
        for line in ascii_catzzz_lines:
            if not line.strip():
                yield ''.join(cat_lines)
                cat_lines = []
            else:
                cat_lines.append(line)
