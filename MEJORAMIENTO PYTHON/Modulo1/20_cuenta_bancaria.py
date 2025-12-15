class Cuenta:
 def __init__(s,sal): s.sal=sal
 def dep(s,m): s.sal+=m
c=Cuenta(1000); c.dep(500); print(c.sal)