def anagram_groups(strings):
    from collections import defaultdict

    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string))
        anagrams[sorted_string].append(string)
    
    return list(anagrams.values())

# Example usage
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram_groups(strings))
