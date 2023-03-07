import numpy as np

N = int(input())

words = np.zeros((N, 10), dtype=float)

for i in range(N):
    words[i] = [float(x) for x in input().split()]

wordQ = np.array([float(x) for x in input().split()])

words_sim = np.empty(shape=10)

for i in range(N):
    words_sim[i] = np.dot(wordQ, words[i]) / (np.linalg.norm(words[i]) * np.linalg.norm(wordQ))

if not np.any(words_sim > 1.0e-300):
    print("-1 0.0000")

else:
    print(f"{np.argmax(words_sim)} {np.amax(words_sim):.4f}")
