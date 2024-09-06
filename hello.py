print('hello') # 출력 함수
# 파이썬 프로그램 주석
# print('err')

'''
    여러줄 주석처럼 사용될 수 있지만
    프로그램에서 문자열로 생성되어 지므로 주석은 아닙니다.
'''
# 문자열은 감싸줘야 합니다
# 문자열은 '문자,"문자","""문자"""
str1 = '문자열'
print(str1)
str1 = "쌍따옴포료 작성"
print(str1)
# 세따옴표를 이용하면 줄바꿈 처리가 되어져서 출력
str1 = """쌍따옴표 
        세개로 
        작성"""
print(str1)
str1 ='''홑따옴표 세개로 작성'''
print(str1)

# 오류
# 문자열과 숫자의 + 연산시 TypeError가 발생
# print('오늘은' + 6 +'일 입니다.')
print('오늘은', 6 ,'일입니다.')

# * 반복횟수
# 반복횟수만큼 반복하여 출력 할 수 있다
print('=' *20)

# print() 함수는 기본적으로 출력후 줄바꿈되어짐
print('반짝')
print('반짝')

# end 
# 출력 후 줄바꿈하지 않음
print('반짝', end='')
print('반짝')

# 실습
# ,로 연결하면 띄어쓰기가 되서 출력됨
print('너무','반짝'*2,'눈이 부셔','No'*5)
print('너무','깜짝'*2,'놀란 나는','Oh'*5)
print('너무','짜릿'*2,'몸이 떨려','Gee'*5)

# 대입연산자를 이용해 변수에 값을 저장
num1 = 5
num2 = 10
print('두수의 곱 : ',5*10)

# 문자열 입력받기
# input() 함수의 반환 타입은 문자열
# 매개변수는 넣어주면 매개변수를 출력 해주고 입력을 대기
# input()
# 입력값을 변수에 저장
name = input('이름을 입력해주세요 : ')
print(name + '님 환영합니다.')

# 형변환
# 문자 타입을 정수 타입으로 형변환
# 실수타입의 값이 입력된 경우 오류가 발생
# num1 = int(input('숫자를 입력해 주세요 : '))
# 문자타입을 실수타입으로 형변환
# 정수타입인 경우 실수타입으로 변환(.0붙음)되어 처리됨
num1 = float(input('숫자를 입력해 주세요 : '))
print(num1+num1)
# 숫자타입을 문자타입으로 형변환
print('오늘은' + str(6) + '일 입니다.')
