# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    st = set()
    for r in report: # 중복된 데이터 제거
        a, b = r.split()
        st.add((a, b))
        
    count = {name: 0 for name in id_list}
    report_set = {name: set() for name in id_list}
        
    for name1, name2 in st: # 신고 결과 반영
        report_set[name1].add(name2)
        count[name2] += 1
        
    ans = []
    for name in id_list: # 답 구하기
        cnt = 0
        for n in report_set[name]:
            cnt += (count[n] >= k)
        ans.append(cnt)    
        
    return ans