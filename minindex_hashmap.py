
#Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
#You need to help them find out their common interest with the least list index sum. 
#If there is a choice tie between answers, output all of them with no order requirement. 
#You could assume there always exists an answer.

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

def findRestaurant(list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if(len(list1) == 0 | len(list2) == 0):
        	return None

        d1 = {s:i+list2.index(s)  for i, s in enumerate(list1) if s in list2}
        min_sum = min(d1.values())
        result = [restaurant for restaurant in d1 if d1[restaurant] == min_sum]
        return result
        


print(findRestaurant(list1, list2))
        

