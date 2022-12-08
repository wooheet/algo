def matchingStrings(strings, queries):
    result = list()
    for query in queries:
        result.append(strings.count(query))

    # print('\n'.join(map(str, result)))
    return result




# strings = ["ab", "ab", "abc"]
# queries = ["ab", "abc", "bc"]

# strings = ["aba", "baba", "aba", "xzxb"]
# queries = ["aba", "xzxb", "ab"]

strings = ["def", "de", "fgh"]
queries = ["de", "lmn", "fgh"]

matchingStrings(strings, queries)

