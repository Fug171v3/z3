from z3 import *
v1=Int('v1')
v2=Int('v2')
v3=Int('v3')
v4=Int('v4')
v5=Int('v5')
v6=Int('v6')
v7=Int('v7')
v8=Int('v8')
v9=Int('v9')
v10=Int('v10')
v11=Int('v11')
v12=Int('v12')
v13=Int('v13')
v14=Int('v14')
v15=Int('v15')
v16=Int('v16')
v17=Int('v17')
v18=Int('v18')
v19=Int('v19')
v20=Int('v20')
v21=Int('v21')
v22=Int('v22')
s=Solver()
s.add(v2==116,v9==99,v16==110,v21==122,v22==125,v5==115,v3==18^0x74,v1==99,v7==100,v13==v12,v19==0x7a,v6+v14==104,v4==123,v15==v8,v8==95,165-v17==v11,2*v18-2*v17==v11-v5,v10==v13+1,v6==v14,2*v18-2*v17==v20-99,3*v6-3*v17+4*v4-4*v6+4*v17==v10,v10==104,v12==103)
s.check()
s.model()
