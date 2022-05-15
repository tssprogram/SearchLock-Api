# searchlock
    BIBLIOTECA PARA A INTERAÇÃO DA API DO SEARCHLOCK
![SEARCHLOCK](/img/searchlock.jpg)

## Installing
`pip install searchlock`

### Example
```python3
# Usando a Biblioteca

from searchlock import searchclient
client = searchclient.Client()
client.key("{sua chave da api}")
client.searchlock_cpf("{cpf da pessoa}")
```
