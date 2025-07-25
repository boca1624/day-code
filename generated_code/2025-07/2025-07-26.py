def is_subsequence(s1, s2):
    iter_s2 = iter(s2)
    return all(char in iter_s2 for char in s1)
