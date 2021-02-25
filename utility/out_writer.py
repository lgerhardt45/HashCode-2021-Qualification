# write whatever we decide has to be written out in /data/out/new text file
import os
from classes.Submission import Submission
from classes.Schedule import Schedule
from classes.Input import Input


def write_file(input):
    input_text = convertInput(input)
    base_path = os.path.dirname(os.getcwd())  # get the base directory
    out_path = os.path.join(base_path, 'data', 'out', 'out_file.txt')  # use os.path.join (works better across system)

    with open(out_path, mode="w") as out_file:
        out_file.write(input_text) # does this work?

def convertInput(submission):
    #naive approach
    #submission_text = str(submission.numIntersections) + "\n"
    #for schedule in submission.schedules:
    #    submission_text += str(schedule.intersection_id) + "\n"
    #    submission_text += str(schedule.numIncomingStreets) + "\n"
    #    for street in schedule.street_time:
    #        submission_text += street + "\n"
    #return submission_text

    #better approach
    str_list = [str(submission.numIntersections) + "\n"]
    for schedule in submission.schedules:
        str_list.append(str(schedule.intersection_id) + "\n")
        str_list.append(str(schedule.numIncomingStreets) + "\n")
        for street in schedule.street_time:
            str_list.append(street + "\n")
    return ''.join(str_list)

# test
if __name__ == "__main__":
    schedule1 = Schedule(2, 1, ["example street 1"])
    schedule2 = Schedule(3, 2, ["example street 2", "example street 3"])
    schedules = [schedule1, schedule2]
    submission = Submission(2, schedules)
    write_file(submission)