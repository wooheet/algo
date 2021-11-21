#!/bin/python3

import math
import os
import random
import re
import sys


# https://github.com/markschaafsma/TechTest_Tyro_GetTheGroups/blob/master/src/getthegroups/Solution.java
# Complete the 'getTheGroups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY queryType
#  3. INTEGER_ARRAY students1
#  4. INTEGER_ARRAY students2
#

def getTheGroups(n, queryType, students1, students2):
    students_groups = list()

    for i in range(1, n):
        students = list()
        students.append(i)

        students_groups.append(students)

    group_totals = list()

    for q in range(0, len(queryType)):
        if queryType[q] == "Friend":

            add_to_index = 0
            remove_from_index = 0

            for i in range(0, len(students_groups)):
                students_set = students_groups[i]

                if students1[q] in students_set:
                    students_set.append(students2[q])
                    add_to_index = i

                if students2[q] in students_set and students1[q] not in students_set:
                    remove_from_index = i

            add_to_student_set = students_groups[add_to_index]
            remove_from_student_set = students_groups[remove_from_index]

            for i in range(0, len(remove_from_student_set)):
                if remove_from_student_set[i] != students2[q]:
                    add_to_student_set.append(remove_from_student_set[i])

            # print(add_to_student_set)
            # print(remove_from_student_set)

            while len(remove_from_student_set) != 0:
                remove_from_student_set.clear()

            if len(remove_from_student_set) == 0:
                students_groups.clear()

            print(students_groups)
            print(add_to_student_set)
            print(remove_from_student_set)

        elif queryType[q] == "Total":
            size1 = 0
            size2 = 0

            for i in range(0, len(students_groups)):
                students_set = students_groups[i]

                if students1[q] in students_set:
                    size1 = len(students_groups[i])

                if students2[q] in students_set:
                    size2 = len(students_groups[i])

            group_total = size1 + size2
            group_totals.append(group_total)

    return group_totals


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # queryType_count = int(input().strip())
    #
    # queryType = []
    #
    # for _ in range(queryType_count):
    #     queryType_item = input()
    #     queryType.append(queryType_item)
    #
    # students1_count = int(input().strip())
    #
    # students1 = []
    #
    # for _ in range(students1_count):
    #     students1_item = int(input().strip())
    #     students1.append(students1_item)
    #
    # students2_count = int(input().strip())
    #
    # students2 = []
    #
    # for _ in range(students2_count):
    #     students2_item = int(input().strip())
    #     students2.append(students2_item)

    # result = getTheGroups(n, queryType, students1, students2)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()

    result = getTheGroups(3, ['Friend', 'Total'], [1,2], [2,3])
    print('\n'.join(map(str, result)))