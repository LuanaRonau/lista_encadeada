obj = ListaDuplamenteEncadeada()

# Olá De Lucca bom dia ^^
# Os comentários demonstram a situação da lista após cada método ser chamado

obj.inserirComoUltimo("C")      # C
print(obj.acessarAtual().valor)

obj.inserirApósAtual("D")       # C D
print(obj.acessarAtual().valor)

obj.excluirPrim()               # D
print(obj.acessarAtual().valor)

obj.inserirAntesDoAtual("B")    # B D
print(obj.acessarAtual().valor)

obj.inserirComoPrimeiro("A")    # A B D
print(obj.acessarAtual().valor)

obj.inserirNaPosicao(2, "C")    # A B C D
print(obj.acessarAtual().valor)

obj.inserirComoUltimo("E")      # A B C D E
print(obj.acessarAtual().valor)

obj.excluirElem("A")            # B C D E
print(obj.acessarAtual().valor)

obj.excluirDaPos(0)             # C D E
print(obj.acessarAtual().valor)

print(obj.buscar("A"))          # False

obj.excluirUlt()                # C D
print(obj.acessarAtual().valor)

obj.excluirAtual()              # C
print(obj.acessarAtual().valor)

'''
Nos métodos inserirNaPosicao() e excluirDaPos() decidi mover o cursor até o primeiro elemento e avançar o número de elementos utilizando um for até chegar na posição passada no parâmetro, eles geram exceção se o tamanho da lista for menor que a posição exigida
Os métodos excluirElem() e buscar() também movem o cursor ao início da lista e percorrem ela, em um for com range da variável tam da lista. Eles armazenam a posição em que o cursor estava quando o método foi chamado e caso a chave procurada não for encontrada na lista o cursor retorna àquela posição armazenada na variável auxiliar 
Ao excluir um elemento o cursor vai apontar para o elemento anterior
Reutilizei alguns métodos pois aqueles que envolviam os primeiros e últimos elementos da lista já possuiam o tratamento dos ponteiros para eles, um exemplo disso é o método inserirAntesDoAtual() que verifica se o atual é o primeiro e caso ele seja vai para o método inserirComoPrimeiro(), assim evitando o erro que ocorreria ao tentar acessar o atributo anterior (que seria None para o primeiro) e já atualizando o ponteiro inicio para o objeto adicionado
    
'''
