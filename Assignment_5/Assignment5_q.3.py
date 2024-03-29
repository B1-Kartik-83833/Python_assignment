def replace_average(student_details):
    updated_details = []
    for student in student_details:
        average = (student['V'] + student['VI']) / 2
        student.pop('V')
        student.pop('VI')
        student['V+VI'] = average
        updated_details.append(student)
    return updated_details


student_details = [
                   {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
                   {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
                   {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
                   ]

new_list = replace_average(student_details)
print(new_list)
