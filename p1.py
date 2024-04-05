import heapq
#import sys

def get_min_rooms(n, meeting_timings):
    meeting_timings.sort()
    room = []
    heapq.heappush(room, meeting_timings[0][1])

    for i in range(1, n): # 그리디로 접근
        if meeting_timings[i][0] < room[0]:  # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
            heapq.heappush(room, meeting_timings[i][1]) # 새로운 회의실 개설
        else: # 현재 회의실에 이어서 회의 개최 가능
            heapq.heappop(room)  # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
            heapq.heappush(room, meeting_timings[i][1])

    return len(room)
    
# 예시 입력 받기
#input = sys.stdin.readline
n = int(input()) # 회의실 개수 입력
constant2 = int(input()) # 의미 없는 상수

meeting_timings = []
for i in range(n):
    start, end = map(int, input().split()) # 시작시간, 종료시간 입력
    meeting_timings.append([start, end])

print(get_min_rooms(n, meeting_timings))