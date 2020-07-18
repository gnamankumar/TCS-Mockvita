n=int(input())
bride=list(i for i in input())
groom=list(i for i in input())
for i in bride:
    if i in groom:
        groom.remove(i)
    else:
        break
print(len(groom),end="")