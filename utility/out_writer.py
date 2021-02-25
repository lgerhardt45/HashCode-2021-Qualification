import os
from classes.Submission import Submission


def write_file(file_name: str, submission_output: Submission):
    input_text = convert_input(submission_output)
    base_path = os.path.dirname(os.getcwd())  # get the base directory
    out_path = os.path.join(base_path, 'data', 'out', f'out_file_{file_name}.txt')

    with open(out_path, mode="w") as out_file:
        out_file.write(input_text) # does this work?


def convert_input(submission: Submission):

    str_list = [str(submission.nr_intersections) + "\n"]
    for schedule in submission.schedules:
        str_list.append(str(schedule.intersection_id) + "\n")
        str_list.append(str(schedule.num_incoming_streets) + "\n")
        for street in schedule.street_time:
            str_list.append(street + "\n")
    return ''.join(str_list)
