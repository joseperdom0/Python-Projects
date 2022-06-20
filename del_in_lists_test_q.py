nums = [1, 2, 3]
vals = nums
print("pre", nums, vals)
del vals[1:2]
print("post", nums, vals)

###
del vals
print(nums)
print(vals)
