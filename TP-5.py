def tri_fusion(l):
    if len(l) == 1 :
        return l[0]
    l1,l2 = tri_fusion(l[:len(l)//2]), tri_fusion(l[len(l)//2:])
    print(l1)
    if l1[0]>l2[0]:
        return l1+l2
    return l1+l2


l=[1,2,3,5,9,0]
print(tri_fusion(l))
