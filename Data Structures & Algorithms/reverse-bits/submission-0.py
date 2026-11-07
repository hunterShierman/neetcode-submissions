class Solution:
    def reverseBits(self, n: int) -> int:
        
        print(n)
        binaryInt = bin(n)[2:].zfill(32)
        binaryList = list(binaryInt)
        print(binaryInt)
        tempList = []

        print(binaryList)
        while len(binaryList) != 0:
            bit = binaryList.pop()
            tempList.append(bit)

        answerStr = ''.join(tempList)
        answer = int(answerStr, 2)

        return answer



