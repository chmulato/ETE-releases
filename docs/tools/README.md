# Ferramentas — Licenciamento Ouro 4.0

Uso **interno** pela Cara-Core Informática. Não distribuir com o aplicativo.

## Gerador de license.key (`gerar_license.py`)

Gera arquivos de licença para ativação do módulo Mineração (Minerador 4.0 / Ouro 4.0).

### Requisitos

- Python 3.9+

### Uso

```bash
python gerar_license.py <HARDWARE_ID> [VALID_UNTIL]
```

- **HARDWARE_ID:** ID de ativação enviado pelo cliente (ex.: após pagamento PIX). Apenas caracteres alfanuméricos; será normalizado em maiúsculas.
- **VALID_UNTIL:** Data de validade no formato `YYYY-MM-DD`. Opcional; padrão: `2099-12-31`.

### Exemplos

```bash
python gerar_license.py A7F2C9E1B4D8
# Gera license_A7F2C9E1B4D8.key com validade 2099-12-31

python gerar_license.py B3E8D1F6A2C9 2030-12-31
# Gera license_B3E8D1F6A2C9.key com validade 2030-12-31
```

### Saída

- Cria um arquivo `license_<HID>.key` no diretório atual.
- Imprime o conteúdo da chave no terminal para copiar e enviar ao cliente (ex.: WhatsApp).

O cliente deve salvar o conteúdo em um arquivo chamado **`license.key`** na pasta do simulador e reiniciar o aplicativo.

### Segredo (produção)

O script assina a licença com HMAC-SHA256. O **segredo** é lido das variáveis de ambiente:

- `LICENSE_SECRET` ou
- `CARA_CORE_LICENSE_SECRET`

Se nenhuma estiver definida, usa o segredo de **demonstração** (compatível com o painel web `licencas_ete.html`). Para **produção**, defina um segredo forte e único no ambiente e use o **mesmo** segredo no simulador (chmulato/ETE) para validação.

```bash
export LICENSE_SECRET="seu-segredo-forte-aqui"
python gerar_license.py A7F2C9E1B4D8
```

### Registro

Após gerar a chave, registrar no controle de pedidos (ex.: `licencas_ete.html` ou planilha): Hardware ID, Data de ativação, Canal (WhatsApp/Telegram), Valid_Until. Manter a relação com dados pessoais apenas em sistema externo (LGPD).
