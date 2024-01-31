import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # scoville 리스트를 힙으로 변환

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우

        # 가장 맵지 않은 음식과 그 다음으로 맵지 않은 음식을 섞어서 새로운 음식 생성
        new_scoville = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1

    return answer