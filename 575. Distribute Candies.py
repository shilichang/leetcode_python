
candies = [1,1,2,2,3,3]
len(set(candies))
if len(candies)/2 <= len(set(candies)):'''糖果种类多于每个人分到的糖果'''
    return int(len(candies)/2)
else:
    return len(set(candies)