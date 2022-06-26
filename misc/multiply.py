class Solution(object):
    def multiply(self, num1, num2):
        l1,l2 = len(num1), len(num2)
        num1,num2=num1[::-1],num2[::-1]
        arr = [0]*(l1+l2)
        ans=''
        ord0 = ord('0')
        for i in range(l1):
            for j in range(l2):
                arr[i+j]+=(ord(num1[i]) - ord0) * (ord(num2[j]) - ord0)

        carryover = 0
        for num in arr:
            num += carryover
            digit = num % 10
            carryover = num // 10
            ans+=str(digit)

        if carryover:
            ans += chr(carryover+ord0)

        ans= ans[::-1]
        i=0
        while ans[i]=='0' and i < len(ans)-1:
            i+=1
        return ans[i:]

solution=Solution()
print("result: ", solution.multiply('123','456'))
print("result: ", solution.multiply('456','123'))
