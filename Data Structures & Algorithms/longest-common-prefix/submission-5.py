class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        for j in range(200):
            if strs[0] == "":
                return ""
            if j==len(strs[0]):
                return prefix
            prefix+=strs[0][j]

            for i in range(len(strs)):
                    if strs[i] == "":
                        return ""
                    if j == len(strs[i]):
                        prefix = prefix[0:len(prefix)-1]
                        return prefix
                    if strs[i][j] != strs[0][j]:
                        prefix = prefix[0:len(prefix)-1]
                        return prefix
        
        
            
        