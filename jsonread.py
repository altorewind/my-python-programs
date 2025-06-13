import json

num=None

fn='nums.json'
with open(fn)as f:
    num=json.load(f)
print(num)