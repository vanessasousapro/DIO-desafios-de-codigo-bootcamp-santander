# Importa o módulo re, que é a biblioteca de expressões regulares do Python. 
import re

def analyze_sentiment():
    # Entrada do usuário
    comentario = input("Sentimento: ")

    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
    neutras = ["mas", "deixou", "apesar", "embora"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)
    # TODO: Conte quantas palavras neutras estão presentes no comentário.  

    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
        # Se há mais palavras negativas do que positivas e não há palavras neutras, o comentário é considerado negativo
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    # Se há um número igual de palavras positivas e negativas, ou há palavras neutras, o comentário é considerado neutro
    else:
        return "Neutro"

# Saída esperada
sentimento = analyze_sentiment()
print(sentimento)