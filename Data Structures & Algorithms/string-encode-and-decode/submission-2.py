class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedstr = ""
        for i in strs:
            encodedstr+=i
            encodedstr+="SPLIT"
        return encodedstr

    def decode(self, s: str) -> List[str]:
        decodedstrs=s.split("SPLIT")
        decodedstrs.pop()
        return decodedstrs
