#delimiter
# str = "a-b-c-d-e-fg-h-i-jk,qwe"
# parse_str = str.split(',')
# # print(type(parse_str))
# # print(f"Value: {parse_str[0], parse_str[1]}")

# print(parse_str[0].split('-'))
# print(parse_str[1])

# init_list = [1,2,3,4]
# init_list.append(5)
# init_list.append(6)
# init_list.append(7)
# init_list.append(8)
# init_list.append([9,10,11])
# print(init_list)
# print(init_list[-1][0])


items = [1,2,3,4,"Dog",5,6,7,8]
for i in items:
    try:
        print (int(i))
    except Exception as e:
        pass


items = [1,2,3,4,"Dog",5,6,7,8]
for i in items:
    # print(type(i))
    if str(type(i)) == "<class 'int'>":
        print(i)

# class Operator:

#     def add():
#         print("Add")

#     def sub():
#         print("Sub")

# def parse(input):
#     return input.split(',')

# if __name__ == '__main__':
#     op = Operator
#     op.add()

    
#     str_comb = "1m,12,1,1,1,1,2,3,4,5123,"
#     parse_str = parse(str_comb)
#     print(parse_str)

vail1 = -1
print(abs(vail1))