n  = input()
#알파벳 이랑 같이 -1
#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
ap = "abcdefghijklmnopqrstuvwxyz"
for i in ap:
    if i in n:
        print(n.index(i),end=" ")
    else:
        print("-1",end=" ")





  


