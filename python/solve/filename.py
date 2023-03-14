import re

filename = "/Users/n2203020/Downloads/word-processor-main/src/main/resources/test.txt"
output_filename = "req_" + filename

# Read the input file and collect all timestamps in a dictionary
timestamps = {}
with open(filename, "r") as f:
    for line in f:
        timestamp = re.search(r'\[(.*?)\]', line).group(1)
        print(timestamp)

        if timestamp in timestamps:
            timestamps[timestamp] += 1
        else:
            timestamps[timestamp] = 1

# Write the duplicate timestamps to the output file
# with open(output_filename, "w") as f:
#     for timestamp, count in timestamps.items():
#         if count > 1:
#             f.write("[" + timestamp + " -0400]\n")
