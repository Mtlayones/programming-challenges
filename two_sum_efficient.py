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
        # mapping index and the values in the list
        for itr in range(len(nums)):
            newArray.append((itr, nums[itr]))
        # sorting the map for better searching
        newArray = sorted(newArray,  key=lambda x: x[1])
        # iterating through the list

        while len(newArray) != 0:
            # dequeuing an element in array
            currentElement = newArray.pop(0)
            # getting the other element in list
            findElement = target - currentElement[1]
            # no found element
            if findElement < currentElement[1] and findElement < 0:
                break
            # getting the index of other element through binary search
            index = self.binarySearch(newArray, findElement)
            # no found element
            if index != -1:
                return [currentElement[0], index]
        return [-1, -1]
