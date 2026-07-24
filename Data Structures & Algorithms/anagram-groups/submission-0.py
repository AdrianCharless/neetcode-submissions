class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = {}
        for str in strs:
            sorted_string = tuple(sorted(str))
            if sorted_string in string_dict:
                string_dict[sorted_string].append(str)
            else:
                string_dict[sorted_string] = [str]
        
        return list(string_dict.values())