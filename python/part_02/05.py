n, m, c, k = map(int, input().split())

PAPER_PER_PACK = 200

total_paper = n * m
total_paper -= k
total_packs = 0

if total_paper % PAPER_PER_PACK == 0:
    total_packs = total_paper // PAPER_PER_PACK
else:
    total_packs = total_paper // PAPER_PER_PACK + 1

total_price = total_packs * c

print(total_price)