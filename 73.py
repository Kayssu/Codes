colocados = ("Atlético","Bahia","Botafogo","Bragantino","Ceará","Corinthians","Cruzeiro"
             ,"Flamengo","Fluminense","Fortaleza","Grêmio","Internacional","Juventude"
             ,"Mirassol","Palmeiras","Santos","Sport","São Paulo","Vasco","Vitória",)

print("-="*20)
print(f"Lista de times do Brasileirão: ",colocados)
print("-="*20)
print(f"Os 5 primeiros são: ",colocados[:5])
print("-="*20)
print(f"Os 4 últimos são são: ",colocados[-4:])
print("-="*20)
print(f"Times em ordem alfábética: ",sorted(colocados))
print("-="*20)

#Dessa forma funciona
inter = colocados.index("Internacional")
colocacao = inter +1
print("O time Internacional está na {}ª posição.".format(colocacao))

#Dessa forma não sei onde coloca o +1
# print("O time Internacional está na {}ª posição.".format(colocados.index("Internacional")))

print("-="*20)