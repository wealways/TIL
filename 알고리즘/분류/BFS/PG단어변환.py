begin ="hit"
target = "cog"
words=["hot", "dot", "dog", "lot", "log", "cog"]	
# return 4

from collections import deque

answer = 0
n = len(words)
visit = []

q = deque([])
q.append((begin,0))

while q:
    sentence,cnt = q.popleft()
    if sentence == target:
        answer = cnt
        break
    for i in range(97,123):
        for j in range(len(sentence)):
            tempS = sentence[:j] + chr(i)+sentence[j+1:]
            if tempS in words and tempS not in visit:
                visit.append(tempS)
                q.append((tempS,cnt+1))

print(answer)