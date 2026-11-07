class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for num in range(n+1):
            binaryStr = bin(num)
            count = 0

            for bit in binaryStr:
                if bit == '1':
                    count += 1

            output.append(count)

        return output