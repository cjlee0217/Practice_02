## 문제 1: 1차원 점들중 가장 가까운 두 점을 출력 ###
s=[9,5,2,7,3,20,100,95]

l = sorted(s)

x1, x2, dist = 0, 0, []

for i in range(len(l)-1):
    x1 = l[i]
    x2 = l[i+1]
    dist.append((x1, x2, l[i+1]-l[i]))

shortest = dist[0]
for j in range(len(dist)):
    if dist[j][2] < shortest[2]:
        shortest = dist[j]

print(shortest[0], shortest[1])


### 문제2: 이메일 주소 검사기 ###
import re

email = input("검사할 이메일 주소 입력: ")

if re.match("([a-zA-Z0-9][a-zA-Z_0-9.]+)\@([a-zA-Z]+\.[a-z]{3})", email):
    print("검사 통과")
else:
    print("검사 통과 실패")


### 문제 3: 도메인주소(URL) 검사기 ###
import re

url = input("검사할 도메인주소(URL) 입력: ")

if re.match("^(http|https)://([a-z]{3}\.)(\w+\.)([a-z]{3})(/\w+)(/\w+)(/\w+\.\w+?[?=\w])", url):
    print("pass")
else:
    print("fail")