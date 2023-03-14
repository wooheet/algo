# In this challenge, read a text file and capture a timestamp from each line of text. Then create a text file with a list of all timestamps that occur multiple times, each on its own line. Naming convention and data description are as follows:
#
# Naming convention: You will be provieded with an input file name called filename. Your output filename should be req_filename(replace filename). For example, given filename = "hosts_access_log_00.txt", process the recoreds in hosts_access_log00.txt and create an output file named req_hosts_access_log_00.txt.
#
# Data description: Each line of the .txt file contains a single log record for July 1995 with the following columns in order:
#
# 1. The hostname of the host making the request.
# 2. This column's values are missing and described by a hyphen (i.e., -).
# 3. A timestamp enclosed in square brackets following the format [DD/mmm/YYYY:HH:MM:SS -0400], where DD is the day of the month, mmm is the name of the month, YYYY is the year, HH:MM:SS is the time in 24-hour format, and -0400 is time zone
# 5. the request, enclosed in quotes(e.g, "GET/images/NASA-logosmall-gif HTTP/1.0").
# 6. The HTTP response code.
# 7. The total number of bytes sent in the response.
#
# For example, given the following log record:
# burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
#
#
#
# We can label each column in the record like so
#
# [hostname - - timestamp request http Response code Bytes]
# [burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0]
#
# Given a string, filename, that denotes the name of a real text file, create an output file named req_filename to store timestamp records. Each line of the output file must contain a time stamp in the format [DD/mmm/YYYY:HH:MM:SS -0400] for any timestamp that appears in more than one request in filename. The line order in the output file does not matter.
#
# Note: The output file has to be written to the current directory.
#
#
#
# sample input:
# hosts_access_log_00.txt
#
# sample output:
# 01/Jul/1995:00:00:12
# 01/Jul/1995:00:00:14
# 01/Jul/1995:00:00:15
#
#
# The data confirms the following:
#
#
# 1. The timestamp 01/Jul/1995:00:00:12 occurs two times.
# 2. The timestamp 01/Jul/1995:00:00:14 occurs three times.
# 3. The timestamp 01/Jul/1995:00:00:15 occurs two times.
#
# Strip the brackets and time zones from the three timestamps occuring more than once and append them to the output file.



import re

filename = "hosts_access_log_00.txt"
output_filename = "req_" + filename

timestamps = {}

# Step 1
with open(filename, "r") as input_file:
    # Step 2
    for line in input_file:
        match = re.search(r'\[(.*?)\]', line)
        if match:
            timestamp = match.group(1)
            # Step 3
            if timestamp in timestamps:
                timestamps[timestamp] += 1
            else:
                timestamps[timestamp] = 1

# Step 4
with open(output_filename, "w") as output_file:
    for timestamp, count in timestamps.items():
        if count > 1:
            # Remove brackets and time zone from timestamp
            timestamp = re.sub(r'[^\d:\/a-zA-Z\s]', '', timestamp)
            output_file.write(timestamp + "\n")
