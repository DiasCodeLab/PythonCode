import whois

def existe_um_dominio(nome_dominio):
    try:
        w = whois.whois(nome_dominio)
        return "domínio existe", nome_dominio

    except Exception as error:
        return f"Erro: {type(error).__name__} - {error}"

print(existe_um_dominio("google.com.br"))
