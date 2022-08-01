'''문제
우현이는 어린 시절, 지구 외의 다른 행성에서도 인류들이 살아갈 수 있는 미래가 오리라 믿었다. 그리고 그가 지구라는 세상에 발을 내려 놓은 지 23년이 지난 지금,
세계 최연소 ASNA 우주 비행사가 되어 새로운 세계에 발을 내려 놓는 영광의 순간을 기다리고 있다.

그가 탑승하게 될 우주선은 Alpha Centauri라는 새로운 인류의 보금자리를 개척하기 위한 대규모 생활 유지 시스템을 탑재하고 있기 때문에,
그 크기와 질량이 엄청난 이유로 최신기술력을 총 동원하여 개발한 공간이동 장치를 탑재하였다. 하지만 이 공간이동 장치는 이동 거리를 급격하게 늘릴 경우 기계에 심각한 결함이 발생하는 단점이 있어서,
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 
그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )



김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

입력
입력의 첫 줄에는 테스트케이스의 개수 T가 주어진다. 각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며, x는 항상 y보다 작은 값을 갖는다. (0 ≤ x < y < 231)

출력
각 테스트 케이스에 대해 x지점으로부터 y지점까지 정확히 도달하는데 필요한 최소한의 공간이동 장치 작동 횟수를 출력한다.'''

'''
1. 여기서 숫자는 1씩 늘어나고, 홀수가 될 때 마다 같은 숫자를 하나씩 더 반복합니다.
한 눈에 보기 쉽도록 규칙을 정리해보겠습니다.
(1, 2) (3, 3, 4, 4) (5, 5, 5, 6, 6, 6) (7, 7, 7, 7, 8, 8, 8, 8) 
*괄호를 위처럼 묶은 이유
-> 반복한 횟수가 같은 숫자끼리 묶음.
예)
1과 2는 반복을 1번
3과 4는 반복을 2번
5와 6은 반복을 3번
7과 8은 반복을 4번


이 규칙으로, 만약 총 이동 거리가 15일때, 공간이동 작동 횟수를 구하려면 반복 횟수의 합으로 구하면 됩니다.
 
1 + 1 + 2+ 2 + 3 + 3 = 12    
-> 15는 12보다 크므로 반복 횟수 하나를 더 더해준다. (반복횟수의 합이 이동 거리보다 작으면 안됨.)
(이해가 안간다면 아래를 참고해 보자)
 
이동 거리                 :  1           2         3,4      5,6     7,8,9   10,11,12   13,14,15,16
공간이동 반복 횟수 합: 1    +    1    +    2    +    2    +    3    +    3    +    4    =    16 
공간이동 작동 횟수 :    1          2         3,3       4,4      5,5,5    6,6,6     7,7,7,7 
 
그러므로 거리가 15일때 공간이동 작동 횟수는 7이 된다. 
 
그러면 거리가 26일때는?? 
1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 = 25
26은 25보다 크므로 그 다음 반복횟수 하나를 더 더해준다
1 + 1  + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 = 30
총 10개의 숫자를 더했으므로 , 거리가 30일때 공간이동 작동 횟수는 10이 된다.
 
=> 요점: 총 3개의 숫자를 더하면 공간이동 작동 횟수는 3이되고, 총 6개의 숫자를 더하면 6이된다.
반복회수를 더한 숫자 만큼 공간이동 작동 횟수가 결정된다.


여기서 반복 횟수가 같은 것끼리 더하면 2*1, 2*2, 2*3 ... 2*n 이 나온다. 그리고, n의 제곱은 경계선에 있는 숫자와 같다. 


n과의 관계:  n*(n+1)
 
y-x(총 이동해야될 거리)가
n의 제곱보다 작거나 같을 때
공간이동 작동 횟수 = n * 2 - 1
 
n의 제곱보다 클 때
공간이동 작동 횟수 = n * 2


'''

T = int(input()) 

for i in range(T):
  x, y = map(int, input().split()) #출발 및 도착 지점

  d = y - x #거리

  n = 0

  while True:
    if d <= n*(n+1):
      break
    n += 1
  
#총 이동 거리가 n의 제곱보다 작거나 같을 때
  if d <= n**2:
    print(n*2-1)
 
#총 이동 거리가 n의 제곱보다 클 때
  else:
    print(n*2)
