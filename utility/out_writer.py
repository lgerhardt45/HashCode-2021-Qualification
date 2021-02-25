# write whatever we decide has to be written out in /data/out/new text file
import os


def write_file(input):
    base_path = os.path.dirname(os.getcwd())  # get the base directory
    out_path = os.path.join(base_path, 'data', 'out', 'out_file')  # use os.path.join (works better across system)

    with open(out_path) as out_file:
        out_file.write(input) # does this work?
