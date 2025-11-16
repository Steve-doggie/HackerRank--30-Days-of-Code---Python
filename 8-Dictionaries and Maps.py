# 读取电话簿条目数量
n = int(input().strip())

# 构建电话簿字典
phone_book = {}

# 读取 n 个条目
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    phone_number = entry[1]
    phone_book[name] = phone_number

# 处理查询（持续读取直到EOF）
while True:
    try:
        query = input().strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        # 没有更多输入时退出
        break