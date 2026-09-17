# Defesa Escrita - Prática 02

### 1. Onde estão os modelos ORM no seu projeto?
Os modelos ORM estão definidos dentro do arquivo `models.py`. São as classes `Autor` e `Livro`, que herdam da classe `Base` (criada em `database.py`).

### 2. Qual classe representa o lado "um" e qual representa o lado "muitos" no relacionamento?
- **Lado "Um"**: A classe `Autor` representa o lado um, pois um autor pode estar associado a vários livros.
- **Lado "Muitos"**: A classe `Livro` representa o lado muitos, pois cada livro individual pertence a apenas um autor.

### 3. Para que serve o ForeignKey em Livro.autor_id?
O `ForeignKey("autores.id")` estabelece a restrição de chave estrangeira no banco de dados relacional. Ele garante a integridade referencial, definindo que o valor salvo na coluna `autor_id` da tabela `livros` deve obrigatoriamente existir na coluna `id` da tabela `autores`.

### 4. O que acontece se você esquecer o session.commit() após inserir os dados?
Se o `session.commit()` for omitido, as inserções feitas via `session.add()` ou `session.add_all()` permanecerão apenas na memória/transação temporária do programa. Ao fechar a sessão, a transação sofrerá um rollback automático, fazendo com que nenhum dado seja efetivamente gravado no arquivo `biblioteca.db`.