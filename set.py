a={1,2,3,4,5,6,7,1,2}
print(type(a))
print(a)
#print(a.index(2)) is not subscriptable
#print(a[1])is not subscritable that is it cannot have the index value
my_set={1,2,3,4}
print(my_set)
my_set.add(5)
print(my_set)
my_set.update([1,2,3,4,8],{4,5,6,7})
print(my_set)
#random_set=set({"education",101,101.01,(true,false)})
#print(random_set)
#random_set.discard(101)
#print(random_set)
#random_set.remove(101)
#print(random_set)
unordered_set={1,2,3,4,5,6,7,8,9}
for num in unordered_set:
    print(num)
    set_A={1,2,3,4}
    set_B={'a','b','c',2}
    print(set_A | set_B)
    print(set_A.union(set_B))
    print(set_B.union(set_A))
    print(set_A & set_B)
    print(set_A.intersection(set_B))
    print(set_B.intersection(set_A))
    print(set_A - set_B)
    print(set_A.difference(set_B))
    print(set_B.difference(set_A))
    set1={"samsung":35000, "apple":75000 ,"vivo":20000 ,"oppo":21000 ,"samsung":25000}
    print(len(set1))
    print(type(set1))
    print(set1["apple"])
    print(set1.keys())
    print(set1.values())
    print(set1.get("apple","not available"))
    print(set1.get("realme", "not available"))
    print("apple" in set1)
    del set1["oppo"]
    print(set1.pop("oppo","none"))
    print(set1.popitem("apple", "not available"))




