#elif문 - 개요
pocket = ['paper','cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

#elif문 적용
pocket = ['paper','cellphone']
card = 1
if('money' in pocket):
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")