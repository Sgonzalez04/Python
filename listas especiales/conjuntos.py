#union |
a=(1,3,5,6,9,12)
b=(5,7,9,15,20,30)
c=a|b

c
(1,3,5,7,9,12,15,20,30)

#interseccion &
d=a&b
d
(9,5,7)

#diferencia -
e=a-b
e
(1, 3, 12)
f=b - a
f
(20,30,15)