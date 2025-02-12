# 한글깨짐 해결
# 맷플롭에서 사용하는 폰트를 한글폰트로 변경
from matplotlib import font_manager, rc, pyplot as plt
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

import csv

color = ['b' ,'g', 'r' ,'c' ,'m', 'y' ,'k' ]
 
# x축, y축 데이터의 갯수가 일치
x = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
y = [0.0, 23.8, 26.8, 47.3, 37.8, 74.0, 194.4, 190.5, 139.8, 55.5, 78.8, 22.6]

# x축데이터, y축데이터, 마커, 선, 색상
# 선그래프를 추가
plt.plot(x,y,marker = 'x' , color=color.pop())    # 그래프 추가

x = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
y = [60.5, 53.1, 16.3, 16.9, 112.4, 139.6, 270.4, 675.7, 181.5, 0.0, 120.1, 4.6]
plt.plot(x, y, marker='x', color=color.pop())     # 그래프 추가

plt.title('선그래프')       # 타이틀
plt.xlabel('x축')      # x축 이름
plt.ylabel('y축')      # y축 이름
plt.legend(['선1','선2'])      # 범례

plt.show()
