weekday = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6
}

def solution(S, K):
    S = list(weekday.values())[list(weekday.keys()).index(S)]
    S %= 7
    result = (S + K) % 7
    X = list(weekday.keys())[list(weekday.values()).index(result)]
    return str(X)

print(solution("Sat", 23))