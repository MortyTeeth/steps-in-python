def timur_and_his_team(n, m, k, x, y, z):
    all_students = k + (m - y - x) + n + z
    return all_students


n = int(input())
m = int(input())
k = int(input())
x = int(input())
y = int(input())
z = int(input())

print(timur_and_his_team(n, m, k, x, y, z))
