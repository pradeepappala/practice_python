
t = int(input().strip())

# result list
res = ['']
for _ in range(t):
    curr_input = input().strip().split()
    if int(curr_input[0]) == 1:
        # append current input to the current last elem and add to res
        res.append(res[-1]+curr_input[1])
    elif int(curr_input[0]) == 2:
        # delete n characters from the current last elem and add to res
        res.append(res[-1][:-int(curr_input[1])])
    elif int(curr_input[0]) == 3:
        # print a char at position given
        print(res[-1][int(curr_input[1])-1])
    elif int(curr_input[0]) == 4:
        # undo last operation
        res.pop(-1)
    print(res)