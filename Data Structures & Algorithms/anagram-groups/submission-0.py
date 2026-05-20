class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myhash = {}
        for i in strs:
            if tuple(sorted(i)) in myhash:
                myhash[tuple(sorted(i))].append(i)
                continue
            myhash[tuple(sorted(i))] = [i]
        return(list(myhash.values()))
