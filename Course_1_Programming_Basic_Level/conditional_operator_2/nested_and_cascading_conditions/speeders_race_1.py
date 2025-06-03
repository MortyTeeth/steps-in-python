speed_zoom = int(input())
speed_flash = int(input())

if speed_zoom == speed_flash:
    print("Don't know")
elif speed_zoom > speed_flash:
    print('NO')
elif speed_flash > speed_zoom:
    print('YES')