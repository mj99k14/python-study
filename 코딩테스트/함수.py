def digit_sum(n):
    if n < 10:           # 한 자리 수면 멈춤
        return n
    return (n % 10) + digit_sum(n // 10)
