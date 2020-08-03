import random
start = input("請輸入隨機數字起始值:")
end = input("請輸入隨機數字結束值:")
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = input("請猜數字:")
    num = int(num)
    if num == r:
        print("你猜中了!")
        print("這是你猜的第", count, "次")
        break
    elif num > r and num in range(start, end + 1):
        print("再猜小一點")
    elif num < r and num in range(start, end + 1):
        print("再猜大一點")
    elif num < start or num > end:
    	print("別鬧了，你設定的數字是", start, "到", end, "之間")
    else:
    	print("你真調皮><")
    print("這是你猜的第", count, "次")
