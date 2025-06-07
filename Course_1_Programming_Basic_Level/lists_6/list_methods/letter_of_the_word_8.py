n = int(input())

cloud = []
string = ''
count = 0

for i in range(n):
    s = input()
    cloud.append(s)
    count +=1
k = int(input())

for j in range(n):
    if len(cloud[j]) >= k:
        string += cloud[j][k - 1]
print(string) 