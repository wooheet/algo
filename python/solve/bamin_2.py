# You need to write a function that extracts the strings common to two given string arrays, sorts them in ascending order, and returns a string separated by ','.
#
# Requirements
# 1. String arrays are input through the leftArray and rightArray parameters.
# 2. After extracting strings that exist in both arrays and sorting them in ascending order, the generated string is returned.
#
# 3. For duplicate strings, you need to remove duplicates.
# 4. Returns an empty string ("") if no string exists in both arrays.
#
# Restrictions
# The length of the array must be greater than 1 and less than 1000.
# The length of the original document is a string between 1 and 100.
#
#
# I/O example
# leftArray: ["a","b","c"]
# rightArray: ["b","c","d"]
# result: "b,c"
#
#
# Returns "b,c" because "b" and "c" are equal and sorted in ascending order.


# import java.util.Arrays;
# import java.util.HashSet;
# import java.util.Set;
# import java.util.stream.Collectors;
#
# public class StringArrayIntersection {
# public static String getIntersection(String[] leftArray, String[] rightArray) {
# Set<String> leftSet = new HashSet<>(Arrays.asList(leftArray));
# Set<String> rightSet = new HashSet<>(Arrays.asList(rightArray));
#
# Set<String> intersection = leftSet.stream()
# .filter(rightSet::contains)
# .collect(Collectors.toSet());
#
# if (intersection.isEmpty()) {
# return "";
# }
#
# return intersection.stream()
# .sorted()
# .collect(Collectors.joining(","));
# }
# }
