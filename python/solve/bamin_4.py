# path variable 방식의 url을 사용하다가 query parameter방식으로 변경하였습니다. 관련된 코드는 수정했지만 요청 로그는 로그의 저장 형식이 달라서 파싱할 때 어려움을 겪고 있습니다.
#
# 기존에 path variable 방식의 로그를 query parameter 방식의 로그로 변경해야 합니다.
#
# /payment/{paymentId}/{paymentMethod} 형식의 문자열을 /payment/{paymentMethod}?paymentId={paymentId} 형식으로 변경하여 반환합니다.
#
# 제한사항
# paymentId는 1글자 이상 9글자 이하의 숫자로만 이루어져 있습니다.
# paymentMethod는 1글자 이상 10글자 이하의 알파벳으로 이루어져 있습니다
# 전달받은 URL이 형식이 맞지 않으면 문자열 "error"를 반환합니다.
# (힌트) 정규식을 최대한 활용하여 코드를 작성합니다.
#
# 입출력 예 1
# 입력: /patyment/1234/cancel
# result: /patyment/cancel?paymentId=1234
#
# /patyment/1234/cancel 에서 paymentId와 paymentMethod는 각각 123과 cancel이므로 /patyment/cancel?paymentId=1234를 반환합니다.
#
# 입출력 예 2
# 입력: /patyment/1234
# result: error
#
# /patyment/1234 에서 paymentMethod가 없어서 형식에 맞지 않으므로 "error"를 반환합니다.
#
# 입출력 예 3
# 입력: /patyment/a1234/cancel
# result: error
#
# /patyment/a1234/cancel 에서 paymentId가 제한사항에 맞지 않으므로 error를 반환합니다.
#
#
# 입출력 예 4
# 입력: /patyment/1234567890/cancel
# result: error
#
# /patyment/1234567890/cancel 에서 paymentId가 제한사항에 맞지 않으므로 error를 반환합니다.
#
# 입출력 예 5
# 입력: /patyment/1234/5678
# result: error
#
# /patyment/1234/5678 에서 paymentMethod가 제한사항에 맞지 않으므로 error를 반환합니다.

import re

def convert_path_to_query(url):
    # Match the input URL to the expected pattern
    match = re.match(r'^/payment/(\d{1,9})/([a-zA-Z]{1,9})$', url)
    if match:
        payment_id = match.group(1)
        payment_method = match.group(2)
        # Construct the new URL with query parameters
        new_url = f'/payment/{payment_method}?paymentId={payment_id}'
        return new_url
    else:
        return 'error'


# import java.util.regex.*;
#
# public static String convertPathToQuery(String url) {
#                                                     // Define the regular expression pattern
# Pattern pattern = Pattern.compile("^/payment/(\\d{1,9})/([a-zA-Z]{1,9})$");
# Matcher matcher = pattern.matcher(url);
#
# if (matcher.matches()) {
#     String paymentId = matcher.group(1);
# String paymentMethod = matcher.group(2);
# // Construct the new URL with query parameters
# String newUrl = String.format("/payment/%s?paymentId=%s", paymentMethod, paymentId);
# return newUrl;
# } else {
# return "error";
# }
# }
