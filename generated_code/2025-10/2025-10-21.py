def is_subsequence(s1, s2):
    it = iter(s2)
    return all(char in it for char in s1)
