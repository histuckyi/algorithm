"""
LeetCode 599. Minimum Index Sum of Two Lists
blog : https://daimhada.tistory.com/164
problem : https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""

class Solution:
    def findRestaurant(self, list1, list2):
        restaurant_list = dict()
        common = True
        for i in range(len(list1)):
            restaurant_name = list1[i]
            restaurant_list[restaurant_name] = i

        min_index = 20000
        min_name = []
        for j in range(len(list2)):
            restaurant_name = list2[j]
            if restaurant_name in restaurant_list:
                v = restaurant_list[restaurant_name]
                if min_index > v + j:
                    min_name = [restaurant_name]
                    min_index = v + j
                elif min_index == v + j:
                    min_name.append(restaurant_name)
        return min_name

if __name__ == "__main__":
    input1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    input2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    s = Solution()
    print(s.findRestaurant(input1, input2))

