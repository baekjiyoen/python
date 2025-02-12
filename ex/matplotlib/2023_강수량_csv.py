import csv
f = open('ex/2023_강수량.csv','r',encoding='utf-8')
# csv.reader : 구분자로 끊어서 리스트에 담아서 반환
csvfile = csv.reader(f,delimiter=',')
print(type(csvfile))

# 제목 읽어오기
header = next(csvfile)
x = []
y = []
for line in csvfile :
   print(line)
   x.append(line[0].replace('2023-',''))
   y.append(float(line[2]))
   
   # 그래프로 출력하기
import matplotlib.pyplot as plt

# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc ,pyplot as plt
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

plt.plot(x,y)
# 제목
plt.title('2023년 월별 강수량')
# 축제목
plt.xlabel('월')
plt.ylabel('강수량(mm)')
# 범례
plt.legend('2023')
plt.show()