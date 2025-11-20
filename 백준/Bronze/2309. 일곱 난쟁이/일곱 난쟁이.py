data_list = []
for i in range(9):
    data_list.append(int(input()))


def seven(data_list):
    remain = sum(data_list) - 100
    for i in range(8):
        for j in range(i+1, 9):
            
            if data_list[i] + data_list[j] == remain:
                data_list.remove(data_list[i])
                data_list.remove(data_list[j-1])
                return sorted(data_list)
                

result = seven(data_list)

for item in result:
    print(item)

