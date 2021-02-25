# write whatever we decide has to be written out in /data/out/new text file
import os


def write_file(input):
    input_text = convertInput(input)
    base_path = os.path.dirname(os.getcwd())  # get the base directory
    out_path = os.path.join(base_path, 'data', 'out', 'out_file')  # use os.path.join (works better across system)

    with open(out_path) as out_file:
        out_file.write(input_text) # does this work?

def convertInput(submission):
    #naive approach
    submission_text = str(submission.numIntersections) + "\n"
    for schedule in submission.schedules:
        submission_text += schedule.intersection_id + "\n"
        submission_text += schedule.numIncomingStreets + "\n"
        for street in schedule.street_time:
            submission_text += street + "\n"
    return submission_text

# test