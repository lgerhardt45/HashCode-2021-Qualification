from utility import in_reader, out_writer
from classes import Input

def main():
    # read in the input
    input: Input = in_reader.open_file('a')

    # create all schedules
    schedules = []
    for intersection in input.intersections:
        # create dictionary to hold street name and time
        street_time = []
        for street in intersection.incomingStreets:
            time = String(1) #tbd
            street_time.append([street, time])

        # create new schedule object
        newSchedule: Schedule(intersection.id,
                              intersection.nrIncomingStreets,
                              street_time)
        # add new schedule object to schedule array
        schedules.append(newSchedule)

    # create submission object
    num_intersections = len(input.intersections)
    submission: Submission(num_intersections, schedules)

    # write the output file in /data
    out_writer.write_file(input=stuff)

if __name__ == '__main__':
    main()