def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    return s1_sorted == s2_sorted
