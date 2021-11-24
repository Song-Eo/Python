from collections import deque
def palindrome(sen):
    if len(sen) % 2 == 1:
        del (sen[len(sen)//2])
    de = deque()
    for ch in sen:
        de.append(ch)

    while not len(de) == 0:
        if not de.pop() == de.popleft():
            return False
    return True

sen = input()
new_sen = []
for ch in sen:
    if ch in (',', ' ', '?', '!', '"', "'"):
        continue
    else:
        new_sen.append(ch)

if palindrome(new_sen): print("회문입니다.")
else:   print("회문이 아닙니다.")