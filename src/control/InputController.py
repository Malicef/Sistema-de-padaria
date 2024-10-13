class InputController:
    def getInputInteiro(comeco=0, fim=1000, texto=None):
        while True:
            try:
                usario_input = int(input(f"\n{texto}: "))
                if usario_input < comeco or usario_input > fim:
                    print("\nOpção inválida! Tente novamente.")
                if comeco <= usario_input <= fim:
                    return usario_input
            except ValueError:
                print("\nOpção inválida! Tente novamente.")