def count_a(word):
    count = 0

    for s in word:
        if s == "a":
            count +=1
    return count

def first_greater(nums):
    if len(nums) == 0:
        return None

    for n in nums:
        if n > 10:
            return n
