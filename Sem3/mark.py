s1_20 = '2 5 5 3 3'
s1_20 = round(sum(map(int, s1_20.split()))*2/23, 2)

s2_20 = '10 10 10 10 10 10'
s2_20 = round(sum(map(int, s2_20.split()))*2/60, 2)
k1 = 9/10

s3_20 = '10 15 1'
s3_20 = round(sum(map(int, s3_20.split()))*2/50, 2)
s3_20 = 2 if s3_20 > 2 else s3_20

s4_20 = '3 3 3 10'
s4_20 = round(sum(map(int, s4_20.split()))*2/19, 2)
k2 = 10/10

rez = round(s1_20+s2_20+k1+s3_20+s4_20+k2)
print(rez)

rez = round(s1_20+s2_20+k1+s3_20+s4_20+k2, 2)
print(rez)
