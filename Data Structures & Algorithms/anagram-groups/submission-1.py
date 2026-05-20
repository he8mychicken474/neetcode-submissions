class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        myhash = {}
        for i in strs:
            sort = tuple(sorted(i))
            if sort in myhash:
                myhash[sort].append(i)
                continue
            myhash[sort] = [i]
        return(list(myhash.values()))
