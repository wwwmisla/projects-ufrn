def main():
    numero = int(input())
    
    if 10 <= numero <= 20:
        numero_bin = bin(numero)[2:]
        
        #lista_bit = [bit for bit in numero_bin]
        lista_bit = list(numero_bin)
        
        print(lista_bit)
    else:
        print("O número inserido não está dentro do intervalo permitido.")
    
if __name__ == "__main__":
    main()