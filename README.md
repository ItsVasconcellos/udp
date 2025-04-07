# Implementação Raw do Protocolo de Transferência UDP

Esta implementação consiste em uma versão simplificada do protocolo UDP, baseada no [RFC 768](https://datatracker.ietf.org/doc/html/rfc768). O protocolo utiliza um cabeçalho customizado composto por:

- **Porta de Origem** (opcional; se não utilizado, o valor é 0)
- **Porta de Destino**
- **Comprimento** (tamanho do cabeçalho + dados)
- **Checksum** (para verificação de integridade dos dados)

## Estrutura do Projeto

A estrutura do repositório é a seguinte:

```
udp_protocol/src/
├── client.py
└── server.py
```

## Como Funciona

### Protocolo Customizado

- **Cabeçalho UDP:**  
  O cabeçalho é composto por 8 bytes distribuídos da seguinte forma:
  - 2 bytes para a **Porta de Origem** (valor 0 se não for utilizado)
  - 2 bytes para a **Porta de Destino**
  - 2 bytes para o **Comprimento** (cabeçalho + dados)
  - 2 bytes para o **Checksum**

- **Checksum:**  
  É calculado de maneira simples, somando os valores dos campos do cabeçalho (com o campo checksum zerado) e dos dados, para detectar possíveis erros na transmissão.

### Funcionamento do Cliente e Servidor

- **Cliente (`client.py`):**  
  Cria um pacote com o cabeçalho e os dados, e envia esse pacote através de um socket UDP para o servidor.

- **Servidor (`server.py`):**  
  Fica escutando na porta definida (por padrão, 9999). Ao receber um pacote, ele:
  - Realiza o *parsing* do cabeçalho e dos dados.
  - Calcula e valida o checksum.
  - Exibe as informações recebidas, como portas, comprimento, checksum e conteúdo dos dados.

## Requisitos

- **Python 3.x:**  
  Certifique-se de que o Python 3 está instalado no seu sistema.

## Como Executar

### 1. Clone o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/ItsVasconcellos/udp
cd udp_protocol
```

### 2. Execute o Servidor

Em um terminal, inicie o servidor com o comando:

```bash
python server.py
```

O servidor ficará escutando na porta 9999 e aguardará a chegada de pacotes.

### 3. Execute o Cliente

Em outro terminal, execute o cliente com o comando:

```bash
python client.py
```

O cliente enviará um pacote para `127.0.0.1` na porta `9999` contendo a mensagem "Hello from client!".

### 4. Verifique a Saída

- **No terminal do servidor:**  
  Você verá a exibição dos detalhes do pacote recebido, incluindo as portas, comprimento, checksum (e sua validade) e os dados enviados.

## Considerações Finais

Esta implementação serve como demonstração de como construir e interpretar pacotes de dados com um cabeçalho similar ao do UDP. Para fins de estudo e testes, é possível estender a funcionalidade, adicionando, por exemplo:
- Mecanismos de retransmissão.
- Confirmação de recebimento (ACKs).
- Uso de sockets brutos (raw sockets) para maior controle.

## Licença

Este projeto é distribuído sob a [Licença MIT](https://opensource.org/licenses/MIT).