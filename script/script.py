from utility import in_reader, out_writer
from classes import Input

def main():
    # read in the input
    input: Input = in_reader.open_file('a')

    # do cool stuff here!!


    # write the output file in /data
    out_writer.write_file(input=stuff)


if __name__ == '__main__':
    main()