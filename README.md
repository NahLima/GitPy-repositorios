# GitPy-repositorios
#desafio

------------------------

O Export dos arquivo  com as informações referentes aos repositórios ficam salvos como **repositoriesExport.txt**

# Ferramentas
- pyhton 
- studio visual code
- ambiente virtual (venv)  
- conda

# 1. Ambiente virtual
Usei o ambiente virtual dentro do Node.js (windows). Para isso digite o comando na pasta do projeto 

````javascript
python -m venv " + o nome do ambiente"

/* na sequencia precisamos ativar o ambiente digite o código */

.\"nome do ambiente"\Scripts\Activate.ps1 

/* usamos ps1 porque estamos no powershell 
 se der um erro no seu powershell é porque ele é restrito por 
padrão, então vamos precisar destravar ele.*/

````

No windowsPowerShell (admin) e digite o comando 
````javascript
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned 
````
Depois digite 
````javascript
S 
// para confirmar
````

Vai até o nodejs e ative o ambiente com o comando citado acima. 


# 2. Instalando as dependências
Após estar no seu ambiente, vamos instalar as dependências que estão no arquivo **requirements.txt**.
No terminal, na raiz do projeto, digite o comando:

````javascript
pip install -r requirements.txt
````
# 3. Testando a aplicação

````javascript
python execute.py  

// ou dar o comando CTRL+ ALT + N no arquivo execute.py
````

----------------------------------------------------------------------------

# Pontos a melhorar

- Fazer com que o código pegue uma lista de repositórios e exporte cada resultado  individualmente. 

- Melhorar a performance 

- exportar os arquivos txt


# Observação

Para testar com outros repositórios basta mudar o endereço que está no 
código **execute.py**

````javascript
//exemplo 
    tree = process_url('NahLima/API-REST---EXPRESS---MYSQL-')
    generate_report('NahLima/API-REST---EXPRESS---MYSQL-', tree)
````
ele vai retornar no console:

![imagem-console](./img/console.JPG)
