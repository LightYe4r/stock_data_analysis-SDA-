with open('ban.csv', 'r') as f:
    ban_data=f.readlines()
    # ban_data=ban_data.split(',')
    ban_data = [item.split(',') for item in ban_data]

with open('종목별 코드.csv', 'r') as g:
    print(g)
    jong_data=g.readlines()
    jong_data = [item.split(',') for item in jong_data]

# for i in ban_data[:10]:
#     print(i)

# ban_data.sort()
# print("-" * 10)

# for i in ban_data[:10]:
#     print(i)

print(jong_data)
