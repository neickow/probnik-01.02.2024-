for N in range(100, 1000):
    R = str(N)
    R1 = int(R[0]) * int(R[1])
    R2 = int(R[1]) * int(R[2])
    if R1 > R2:
        R = str(R1) + str(R2)
    else:
        R = str(R2) + str(R1)
    R=int(R)
    if R==240:
        print(R, N)
