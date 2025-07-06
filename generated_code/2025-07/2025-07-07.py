from collections import defaultdict

def find_anagram_groups(words):
    """
    将一组单词按变位词分组，例如 ["eat", "tea", "tan", "ate", "nat", "bat"]
    返回 [["eat","tea","ate"],["tan","nat"],["bat"]]
    """

    anagram_map = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))  # 哈希表的关键：排序后的字符元组作为键
        anagram_map[key].append(word)

    return list(anagram_map.values())


# 示例输入
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = find_anagram_groups(words)
print(groups)
