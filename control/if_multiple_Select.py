score = int(input("請輸入成績:"))

if(score>=90):
    if(score>=98):
        print("你是AA級")
    else:
        print("你是A級")
elif(score>=80) and (score<=89):
    print("你是B級")
elif(score>=70) and (score<=79):
    print("你是C級")
elif(score>=60) and (score<=69):
    print("你是D級")
else:
    print("其它")