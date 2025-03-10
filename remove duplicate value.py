def remove_duplicate_value(a,b):
    var_1=set(a)
    var_2=set(b)
    remove=set(var_1|var_2)
    print(remove)
a=[1,2,3,4,5,6]
b=[1,2,3,7,8,9,1]
remove_duplicate_value(a,b)