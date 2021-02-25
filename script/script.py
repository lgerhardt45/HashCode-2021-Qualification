from utility import in_reader, out_writer
from classes import Input
from classes.Schedule import Schedule
from classes.Submission import Submission


def main():

    file_name = 'a'

    # read in the input
    input: Input = in_reader.open_file(file_name=file_name)

    # create all schedules
    schedules = []
    for intersection in input.intersections:

        # create dictionary to hold street name and time
        street_time = []  # String array
        for street in intersection.incomingStreets:
            time = str(1)  # tbd
            street_time.append(street.id + ' ' + time)   # as a String

        # create new schedule object
        new_schedule = Schedule(intersection.id,
                                intersection.nrIncomingStreets,
                                street_time)
        # add new schedule object to schedule array
        schedules.append(new_schedule)

    # create submission object
    num_intersections = len(input.intersections)
    submission = Submission(num_intersections, schedules)

    # write the output file in /data
    out_writer.write_file(file_name=file_name, input=submission)


if __name__ == '__main__':
    main()
