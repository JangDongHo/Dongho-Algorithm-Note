def solution(today, terms, privacies):
    def to_days(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d

    terms_dict = {}
    for term in terms:
        kind, month = term.split()
        terms_dict[kind] = int(month)

    today_days = to_days(today)
    answer = []

    for i, privacy in enumerate(privacies, 1):
        date, kind = privacy.split()
        expire_days = to_days(date) + terms_dict[kind] * 28 - 1
        
        if expire_days < today_days:
            answer.append(i)

    return answer