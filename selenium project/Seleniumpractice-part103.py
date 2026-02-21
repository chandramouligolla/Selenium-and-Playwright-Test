prod="2*3"
first_element=int(prod[0])
second_element=prod[1]
Third_element=int(prod[2])
# print(type(first_element))
# print(second_element)
# print(int(Third_element))
dicti={
    "+":"add",
    "-":"sub",
    "*":"mul",
    "/":"div"
}
if second_element in dicti.keys():
        if dicti[second_element]=="add":
            print(first_element+Third_element)
        elif dicti[second_element]=="sub":
            print(first_element-Third_element)
        elif dicti[second_element]=="mul":
            print(first_element*Third_element)
        else:
            print(first_element/Third_element)




