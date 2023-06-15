def ispalindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(ispalindrom("лепсспел"))#выведет True
print(ispalindrom("helloworld"))#выведет False


