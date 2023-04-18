# 빈 딕셔너리 생성
score_dict = {}

# 국어, 수학 성적을 입력받아 리스트로 정리
for i in range(4):
    name = input(f"{i+1}번째 학생 이름: ")
    korean_score = int(input(f"{name}의 국어 성적: "))
    math_score = int(input(f"{name}의 수학 성적: "))
    score_list = [korean_score, math_score]

    # 홀수의 값만 딕셔너리에 추가
    for score in score_list:
        if score % 2 == 0: #1이면 홀수고 0으로 바꾸면 모두 나옴
            if name in score_dict:
                score_dict[name].append(score)
            else:
                score_dict[name] = [score]

# 결과 출력
print(score_dict)
