from simpleGA import simpleGA

target = "andi lukman"
besar_populasi = 10
laju_mutasi = 0.4

solusi, generasi = simpleGA(target, besar_populasi, laju_mutasi)
print(generasi)