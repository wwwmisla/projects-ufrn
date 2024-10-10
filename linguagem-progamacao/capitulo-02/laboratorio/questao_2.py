def main():
    # Palavra ou frase do usuário
    pOuf = input()
    
    print(f'{len(pOuf)}\n{pOuf[0]}\n{pOuf[-1]}\n{pOuf[::-1]}')
    
    #comprimento_string = len(pOuf)
    #primeira_letra_string = pOuf[0]
    #ultima_letra_string = pOuf[comprimento_string-1]
    #inverte_pOuf = pOuf[::-1]

    #print(f"{comprimento_string}\n{primeira_letra_string}\n{ultima_letra_string}\n{inverte_pOuf}")
    
if __name__ == "__main__":
    main()