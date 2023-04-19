#세명의 학생 (국어, 수학) 성적을 입력받아
#국어는 오름차순, 수학은 내림순으로 정렬

score_list=dict()
korea_list=list()
math_list=list()

print(intput(num))
for i in range(0,num):
    korea= print(input("국어 성적을 입력하세요> "))
    math= print(input("수학 성적을 입력하세요> "))
    korea_list.append(korea)
    math_list.append(math)

korea_list.sort()
math_list.sort(reverse=true)

score_list['국어'] = korea_list  # 딕셔너리 key에 값 추가
score_list['수학'] = math_list

print(score_list['사회'])
print(score_list.get['수학'])
