# 10이 몇번 곱해졌나? -> 2와 5가 몇번 곱해졌나 -> (2의 개수 >= 5의 개수) -> 5가 몇번 곱해졌나?

# 5로 나눈 몫 -> 곱해진 모든 5의 배수의 개수
# 5**2로 나눈 몫 -> 곱해진 모든 25의 배수는 5가 두 번 들어서 위의 경우에서 놓친 개수를 잡아줌
# 5**3로 나눈 몫 -> 125의 배수,, 위와 같은 이유
# 0 <= N <= 500이라서 625로 나눈 몫은 신경x

import sys
N = int(sys.stdin.readline())
print(N//5+N//25+N//125)