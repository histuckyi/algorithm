"""
2357. Make Array Zero by Subtracting Equal Amounts

nums는 0 이상의 정수로 이뤄진 배열이다.
x는 nums에 있는 수 중에 0보다 크지만 가장 작은 수이다.
선택한 x의 값을 사용하여 nums에 있는 모든 요소(element)에서 값을 뺀다.
이를 몇 번 반복하면 배열의 모든 값이 0이 되도록 할 수 있을까?


풀이 방법
1. 배열 nums를 set으로 변경하여 중복된 값을 제거하고 정렬한 newNums 배열을 생성한다. 
2. newNums 배열로부터 가장 큰 값(maxNum)을 구한다. 
3. 가장 큰 값(maxNum)이 0인 경우는 더이상 값을 뺄 필요가 없어 0을 반환한다.
   가장 큰 값(maxNum)이 1인 경우에는 nums의 길이가 1이고, 가장 작은 값이기도 한 본인의 값만 빼면 배열의 모든 값이 0이 되므로 1을 반환한다.
4. 정렬된 newNums에서 0 이상의 값의 수를 세면 답이 나온다.
   그 이유를 생각해보면, 
   newNums = [1,3,5] 일 때, 
   결과적으로 가장 큰 값은 앞의 값들로 인해 값이 감소되더라도, 결국 본인이 가장 작은 값이 될때까지 남아있기 때문이다. 
   본인의 차례가 와야만 본인의 값을 제거할 수 있다. 
   이렇게 되는 이유는 맨 처음에 set을 사용하여 중복을 제거했던 덕분이라고 할 수 있다. 
   
   [0, 2, 4]  -- 1(index가 0인 값)이 제일 작으므로 1만큼 값 제거
   [0, 0, 2]  -- 2(index가 1인 값)가 제일 작으므로 2만큼 값 제거
   [0, 0, 0]  -- 2(index가 2인 값)가 제일 작으므로 2만큼 값 제거

"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        newNums = sorted(set(nums))
        maxNum = newNums[-1]
        
        if maxNum == 0:
            return 0
        if len(newNums) == 1:
            return 1
        
        count = 0
        for curr in newNums:
            if curr > 0:
                count += 1
        return count
