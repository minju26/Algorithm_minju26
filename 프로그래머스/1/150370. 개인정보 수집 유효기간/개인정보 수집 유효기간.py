from datetime import datetime, date

def dateCal(fdate, term):
    y, m, d = map(int, fdate.split("."))
    term = int(term)
    
    if d != 1:
        d -= 1
    else: 
        d = 28
        m -= 1
        if m == 0:
            m = 12
            y -= 1
    
    if (m+term)%12 == 0:
        m = 12
        y += (m+term)//12 - 1  # m이 12일 경우, 연도 증가 처리 수정
    else:
        y += (m+term)//12
        m = (m+term)%12
    
    due = date(y, m, d)
    return due
    

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, "%Y.%m.%d").date()
    dic_terms = {}
    
    for t in terms:
        k, v = t.split()
        dic_terms[k] = v
        
    for i, n in enumerate(privacies, start=1):
        fdate, term = n.split()
        due = dateCal(fdate, dic_terms[term])
        
        if due < today: answer.append(i)  
        
    return answer