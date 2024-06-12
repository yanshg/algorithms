def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  res = ''
  i = 0
  for c in C:
    if i >= N:
      break
    res += 'B' if c == 'A' else 'A'
    i += 1
  return res

N = 3
C = 'BAB'
res = getWrongAnswers(N, C)
print("C: " + C + "  result: " + res)
