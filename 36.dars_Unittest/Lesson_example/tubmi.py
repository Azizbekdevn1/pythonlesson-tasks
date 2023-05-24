def tubSonmi(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # faqat toq sonlarni tekshiramiz
        if n % i == 0:
            return False
    return True
