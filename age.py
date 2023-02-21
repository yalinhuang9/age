# age = input('請輸入年齡：')
# age = int(age) #casting 型別轉換
# if age >= 20:
#     print('恭喜你可以投票')
# else:
#     print('你還不能投票喔')
# else if 另外如果＝ elif
# elif A and B 即A＆B 都是true才執
# if age < 13:
#     print('還是國小喔')
# elif age >= 13 and age < 18:
#     print('國高中')
# elif age >= 18 and age < 22:
#     print('大學')
# else:
#     print('社會')
driving = input('請問你有沒有開過車？ yes/no  ')
if driving != 'yes' and driving != 'no':
    print('只能輸入 yes/no')
    raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == 'yes':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('奇怪 你怎麼有開過車？')
elif driving == 'no':
    if age >= 18:
        print('你可以考駕照了啊 怎麼不滾去考')
    else:
        print('再過幾年就可以考了')

