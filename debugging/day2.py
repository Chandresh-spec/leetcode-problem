def longest_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in seen:
            left=seen[s[right]]+1
        seen[s[right]]=right
        max_len = max(max_len, right - left + 1)

    return max_len



st="acdeabcdef"
print(longest_substring(st))