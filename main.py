def PrimeList(N):
    # 存储小于 N 的质数
    primes = []
    # 遍历 2 到 N-1 的每个数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 试除：从 2 到 num 的平方根，若能整除则不是质数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # 如果是质数，加入列表
        if is_prime:
            primes.append(str(num))
    # 用空格连接质数，输出结果
    return " ".join(primes)
# 测试示例
print(PrimeList(10))  # 输出：2 3 5 7
