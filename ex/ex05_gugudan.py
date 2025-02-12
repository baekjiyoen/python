# 구구단
# 1. 2단부터 9단까지 출력
for i in range(2,10) :
    print(f"---{i}단---")
    for j in range(2,10) :
        print(f"{i} * {j} = {i * j}")
print()
# 2. 홀수단만 출력
for i in range(1,10,2) :
    print(f"---{i}단 --- ")
    for j in range(1,10) : 
        print(f"{i} *{j} = {i*j}")
        


# range() 함수를 이용해서 숫자 리스트를 만들어 반복문을 이용 한다
dan_range = range(2,10) # 2 ~ 9
i_range = range(1,10) # 1 ~ 9
for dan in dan_range :
    # 홀수단만 출력
    # 짝수인 경우에는 다음 반복문으로 넘김
    if dan % 2 == 0:
        continue
    # 아래 로직이 홀수일 경우에만 실행
    print('dan : ', dan)
    # 단이 1 증가할때마다 i는 9번 실행됨
    for i in i_range :
        # print(f'i : {i}')
        # print 함수 안에 f()를 입력 하고는 변수는 {}안에 작성
        print(f'({dan} * {i} = {dan*i})')