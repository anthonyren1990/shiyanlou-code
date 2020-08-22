for i in range(1, 101):
    #要跳过7和7的倍数, 然后跳过个位数是7的数字，最后跳过十位数是7的数字
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        continue
    print(i)
