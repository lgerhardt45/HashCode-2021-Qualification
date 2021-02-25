from utility import in_reader, out_writer
from classes import Input
from classes.Schedule import Schedule
from classes.Submission import Submission

from datetime import datetime


def main():

    file_names = ['a', 'b', 'c', 'd', 'e', 'f']

    # ALL THE FILES
    for file_name in file_names:
        start = datetime.now().time()
        print(f'starting file {file_name} at {start}')

        # read in the input
        challenge_input: Input = in_reader.open_file(file_name=file_name)

        # create all schedules
        schedules = []
        for intersection in challenge_input.intersections:

            # create dictionary to hold street name and time
            street_time = []  # String array
            for street in intersection.incoming_streets:
                time = str(1)  # tbd
                street_time.append(street.street_id + ' ' + time)   # as a String

            # create new schedule object
            new_schedule = Schedule(intersection.intersection_id,
                                    intersection.nr_incoming_streets,
                                    street_time)
            # add new schedule object to schedule array
            schedules.append(new_schedule)

        # create submission object
        num_intersections = len(challenge_input.intersections)
        submission = Submission(num_intersections, schedules)

        # write the output file in /data
        out_writer.write_file(file_name=file_name, submission_output=submission)

        print(f'done with file {file_name} ({datetime.now().time()})')


if __name__ == '__main__':
    main()
