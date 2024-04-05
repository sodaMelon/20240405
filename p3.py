import sys

def find_largest_sqaure_size(n,m,samples):
    dp = [[0] * m for _ in range(n)]  # n x m 크기의 dp 배열 초기화
    answer = 0
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:  # 첫 번째 행이나 열인 경우
                dp[i][j] = samples[i][j]  # dp 값은 현재 값과 동일
            elif samples[i][j] == 0:  # 현재 위치가 0이라면 정사각형이 될 수 없음
                dp[i][j] = 0
            else:  # 그 외의 경우
                # 왼쪽 상단, 위, 왼쪽 중 최소값을 선택하고 현재 위치의 값에 1을 더함
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            answer = max(dp[i][j], answer)  # 현재까지의 최대 정사각형 길이 갱신
    return answer  # 최대 정사각형 변 길이 반환

#예시 입력
n = int(input())  # 행의 개수
m = int(input())  # 열의 개수

samples = []


for _ in range(n):
    samples.append(list(map(int, sys.stdin.readline().strip())))  # 입력된 배열 정보 저장
print(find_largest_sqaure_size(n,m,samples))  # 최대 정사각형 변 길이 출력