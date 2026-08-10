class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        #arr = [17, 18, 5, 4, 6, 1]

        right_max = arr[-1] # 1
        current = 0 #6
        arr[-1] = -1 #arr = [17, 18, 5, 4, 6, -1]

        for i in range(len(arr)-2, -1, -1):
            current = arr[i] #6
            arr[i] = right_max

            if current > right_max:
                right_max = current

        return arr


            


            