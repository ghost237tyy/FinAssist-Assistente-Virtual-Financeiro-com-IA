print("=" * 50)
print("FINASSIST - ASSISTENTE FINANCEIRO")
print("=" * 50)

print("Olá! Sou o FinAssist.")
print("Posso explicar conceitos financeiros básicos.")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ").lower().strip()

    if pergunta == "sair":
        print("FinAssist: Até mais!")
        break

    if "pix" in pergunta:
        resposta = (
            "O Pix é um sistema de pagamentos instantâneos "
            "que permite realizar transferências e pagamentos "
            "de forma rápida."
        )

    elif "cartão" in pergunta or "cartao" in pergunta:
        resposta = (
            "O cartão de crédito permite realizar compras "
            "utilizando um limite disponibilizado pela instituição "
            "financeira. As compras são cobradas posteriormente "
            "na fatura."
        )

    elif "poupança" in pergunta or "poupanca" in pergunta:
        resposta = (
            "A poupança é uma modalidade de aplicação financeira "
            "utilizada para guardar dinheiro e obter rendimento."
        )

    elif "juros compostos" in pergunta:
        resposta = (
            "Nos juros compostos, os juros de cada período são "
            "incorporados ao saldo, fazendo com que os próximos "
            "juros sejam calculados sobre um valor maior."
        )

    elif "juros" in pergunta:
        resposta = (
            "Juros representam um valor adicional relacionado "
            "ao uso ou aplicação de dinheiro durante determinado período."
        )

    elif "segurança" in pergunta or "senha" in pergunta:
        resposta = (
            "Nunca compartilhe senhas, códigos de segurança ou "
            "dados bancários completos. Em caso de suspeita de fraude, "
            "procure os canais oficiais da instituição financeira."
        )

    else:
        resposta = (
            "Não encontrei essa informação na minha base de conhecimento. "
            "Tente perguntar sobre Pix, cartão, poupança ou juros."
        )

    print(f"FinAssist: {resposta}\n")
