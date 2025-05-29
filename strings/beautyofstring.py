

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        ele=Counter(s)
        sorted_freq=sorted(ele.items(),key=lambda item:item[1],reverse=True)
        return "".join(char*freq for char,freq in sorted_freq)
        