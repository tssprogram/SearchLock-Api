# searchlock
    BIBLIOTECA PARA A INTERAÇÃO DA API DO SEARCHLOCK
![SEARCHLOCK](/img/searchlock.jpg)

<hr>

# Como Funciona?
- A biblioteca é um conjunto de funções em que eles podem ser usual para automação como: Bots do discord, whatsapp, telegram e afins. O script interage, sendo necessário que você entre no site [Searchlock](https://searchlock.me) e se registrar e pedir sua chave da api, com a aplicação do site.
- A plataforma pode ser usada para consulta de dados tanto dentro do painel, quanto com a API dele e essa biblioteca facilita a interação.
- Lembrando: Essa biblioteca não está nos projetos da Pypip, então o uso do ```pip install searchlock``` não irá funcionar

<hr>

# Oque devo fazer?
- Primeiro, deve se registrar no site e colocar suas informações necessárias
- Depois, para usar o painel você deve fazer uma recarga de 20 reais para poder usar (Obs: Esse painel não é, em hípotese alguma, da TSS)
- Após colocar créditos você já pode usar a API após conectar seu telegram com o site e irão disponibilizar a sua chave para poder autenticar com a API do site.

<hr>

# Exemplos
- Depois de já ter pego a sua chave de autorização, basta apenas conferir esse exemplo:

```python3

from searchlock import searchclient

client = searchclient.Client()

client.key("{sua chave do site}")
```

Seguindo esse exemplo, você já pode retornar dados, em json como:

```python3

client.searchlock_cpf("{cpf da pessoa}")
```
