import json

nums=[3,123,31,1,123,1321,1]

nm='nums.json'
with open(nm,'w') as f:
    json.dump(nums,f)
print('finish!')