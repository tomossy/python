def check_seiza(month, day):
    constellation = [
        '山羊座', '水瓶座', '魚座', '牡羊座', '牡牛座', '双子座', '蟹座',
        '獅子座', '乙女座', '天秤座', '蠍座', '射手座', '山羊座'
    ]

    limit = [
        19, 18, 20, 19, 20, 21,
        22, 22, 22, 23, 22, 21, 19
    ]
    
    lastday = [
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]

    if day >= 1 and month >= 1:
        if day <= limit[month - 1] and day <= lastday[month - 1]:
            print("1通過");
            return constellation[month - 1]
        elif day >  lastday[month - 1]:
            print("2通過");
            print("そんな日は存在しません")
        elif month >= len(constellation):
            print("3通過");
            print("そんな月は存在しません")
        else:
            print("4通過");
            return constellation[month]
    else:
        print("正しく入力してください")

month = int(input("誕生した月は？"))
day = int(input("誕生した日は？"))
print(check_seiza(month, day))

