num = float(input())

total_kop = round(num * 100) 

rub = total_kop // 100
kop = total_kop % 100

print(f"{rub} rub {kop} kop")