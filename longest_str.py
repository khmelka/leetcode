def length_of_longest_substring(s: str) -> int:
    char_set = []
    start = 0
    max_length = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.append(s[end])
        max_length = max(max_length, end - start + 1)

    # return max_length
    print("HERE", char_set, max_length)

length_of_longest_substring("abcabcbb")