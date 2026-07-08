#======================
#  uso do split e strip
#======================

frase = "   python é muito poderoso   "

frase = frase.split()
for frases in frase:
    print(f"palavra:{frases}")

for index, frase_enumerada in enumerate(frase):
    print(index,frase_enumerada)

segunda_frase = "   python é muito poderoso   "
print(segunda_frase.strip())
print(segunda_frase.split())
print(len(segunda_frase.split()))

