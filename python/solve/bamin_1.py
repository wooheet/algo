# It should convert the string to upper case in the input string array and return the first string whose length is between 5 and 10.
#
# And if there is no object that meets the condition in the input string array, "none" should be returned.
#
# Constraints: Conditional statements and loop statements (if, switch/case, for, while) should not be used. Instead, you should write it as a lambda, such as java stream /optional.



# import java.util.Arrays;
# import java.util.Optional;
#
# public class StringConverter {
# public static String convertString(String[] arr) {
# Optional<String> result = Arrays.stream(arr)
# .filter(str -> str.length() >= 5 && str.length() <= 10)
# .map(String::toUpperCase)
# .findFirst();
# return result.orElse("none");
# }
# }
