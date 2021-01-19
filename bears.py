def bears(n):
    if n==42:
        return True
    if n%2==0:
        return bears(n/2)
    elif n%3==0 or n%4==0:
        t1 = n
        t1 /= 100
        t1 *= 100
        t1 = (n-t1)/10
        t2 = n
        t2 /= 10
        t2 *= 10
        t2 = n-t2
        return bears(t1*t2)
    elif n%5==0:
        return bears(42)
    return False
        
