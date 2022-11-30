'''3명의 학생은 1번 문제부터 마지막 문제까지 다음과 같이 마킹합니다.
1번 학생: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ... 
2번 학생: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ... 
3번 학생: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ... 

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
• 문제의 정답은 1, 2, 3, 4, 5중 하나입니다. 
• 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요. '''

def solution(answers):
    answer = []
    case1 = [1, 2, 3, 4, 5]
    case2 = [2, 1, 2, 3, 2, 4, 2, 5]
    case3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for idx, val in enumerate(answers):
        if case1[idx % len(case1)] == val:
            scores[0] += 1
        if case2[idx % len(case2)] == val:
            scores[1] += 1
        if case3[idx % len(case3)] == val:
            scores[2] += 1
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)
    return answer

answer1 = [1,2,3,4,5]
answer2 = [1,3,2,4,2]
print(solution(answer1))
print(solution(answer2))

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result