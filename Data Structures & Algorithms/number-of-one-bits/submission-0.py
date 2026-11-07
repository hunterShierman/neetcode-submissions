class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryStr = bin(n)
        count = 0

        for bit in binaryStr:
            if bit == '1':
                count += 1

        return count