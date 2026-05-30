class Solution:
    def convertToTitle(self, columnnumber: int) -> str:
        result = []

        while columnnumber > 0:
            columnnumber -= 1
            letter = chr(ord('A') + columnnumber % 26)
            result.append(letter)

            columnnumber = columnnumber// 26

        result.reverse()
        result = "".join(result)
        return result