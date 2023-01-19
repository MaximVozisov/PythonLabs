from pyDatalog import pyDatalog 
import random

#��������� ����� ���� 
pyDatalog.create_terms('arrSum, N, AVS, arrRandom, arrRandom2, arrRandomMedian')

arrSum[N] = N + arrSum[N-1]
arrSum[1] = 1

print(arrSum[100]==N)

# ������� �������� ����
AVS[N] = (N + 1)/2
print(AVS[200]==N)

# ����� ���� ��������� ����� [1,100]
arrRandom[N] = random.randint(0,100) + arrRandom[N - 1]
arrRandom[1] = random.randint(0, 100)
print(arrRandom[100]==N)

#������� ���� ��������� �����
arrRandom2[N] = random.randint(0,100) + arrRandom2[N - 1]
arrRandom2[1] = random.randint(0, 100)
arrRandomMedian[N] = arrRandom2[N] / N
print(arrRandomMedian[100] == N)