class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
        
        return list(anagram_dict.values())


