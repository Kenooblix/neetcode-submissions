class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string))
            result += "#"
            result += string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        ptr = 0
        while ptr < len(s):
            numstr = ""
            while s[ptr] != "#":
                numstr += s[ptr]
                ptr += 1
            num = int(numstr)
            ptr += 1
            strtoadd = ""
            for i in range(num):
                strtoadd += s[ptr]
                ptr += 1
            result.append(strtoadd)
        return result
