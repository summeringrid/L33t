import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def hash(string):
            return tuple([(ord('letter') - ord(string[0])) % 26 for letter in string])
        output = collections.defaultdict(list)  # {hash:value}
        for string in strings:
            output[hash(string)].append(string)
        return list(output.values())
    
    # Time = O(N), N is sum of the string length in the strings