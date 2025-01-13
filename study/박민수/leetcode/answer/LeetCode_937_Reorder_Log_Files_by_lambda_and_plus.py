class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        answer = []
        for log in logs:
            if log.split()[1].isdigit(): # 이것도 처음엔 let,dig만 나오는 줄 알고 했는데 아니였음 isdigit()으로 숫자인지 확인 가능
                dig.append(log)
            else:
                let.append(log)
        let.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # 식별자 이후를 분류하는걸 몰랐음
        # sort()는 튜플을 기준으로 정렬할 때, 튜플의 첫 번째 요소를 기준으로 정렬한 후,
        # 만약 같은 값이 나오면 두 번째 요소를 기준으로 정렬
        answer.extend(let)
        answer.extend(dig)
        return answer  # return let+dig