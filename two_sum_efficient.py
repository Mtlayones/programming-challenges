class Solution(object):
    def binarySearch(self, array, target):
        midPoint = len(array) // 2
        if len(array) == 0 or (len(array) == 1 and target != array[0][1]):
            return -1
        if target == array[midPoint][1]:
            return array[midPoint][0]
        if target < array[midPoint][1]:
            return self.binarySearch(array[:midPoint], target)
        else:
            return self.binarySearch(array[midPoint+1:], target)

    def twoSum(self, nums, target):
        newArray = []
        for itr in range(len(nums)):
            newArray.append((itr, nums[itr]))
        newArray = sorted(newArray,  key=lambda x: x[1])
        for itr in range(len(newArray)):
            findElement = target - newArray[itr][1]
            if findElement < newArray[itr][1] and findElement < 0:
                break
            tempArray = newArray[:]
            tempArray.remove(newArray[itr])
            index = self.binarySearch(tempArray, findElement)
            if index != -1:
                return [newArray[itr][0], index]
            tempArray = newArray[:]
        return [-1, -1]
