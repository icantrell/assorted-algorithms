def xgcd(a,b):
    swap = False
    if a < b:
        swap = True
        a, b = b, a
    prevx, x = 1, 0
    prevy, y = 0, 1

    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a%b
    if swap:
        prevx, prevy = prevy, prevx
    return a, prevx, prevy



