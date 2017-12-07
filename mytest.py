fname = "C:\\Users\\Арина\\Desktop\\quotes.txt"
ql = []
with open(fname, encoding="utf-8") as f:
    quote = f.readlines()
    #ql.append(quote)
for line in quote:
    word = line.split()
for q in quote:
    if len(quote) > 10 and len(q.split(' ', 1)[0]) < 5:
        print(q)

    
