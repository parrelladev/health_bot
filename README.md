# Health Bot

Este projeto contém um esqueleto de bot para Telegram que auxilia profissionais da saúde a gerar vídeos éticos utilizando LLMs e a API do HeyGen.

## Requisitos
- Python 3.11+
- Dependências listadas em `requirements.txt`
- Tokens de acesso para Telegram, OpenAI e HeyGen

## Configuração
1. Crie um arquivo `.env` na raiz definindo:
   ```
   TELEGRAM_BOT_TOKEN=seu_token
   OPENAI_API_KEY=sua_chave
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o bot:
   ```bash
   python bot.py
   ```

O bot irá receber uma foto, coletar o briefing e gerar o roteiro via LLM. Após aprovado, envia para o HeyGen (integração a ser implementada) e retorna o link do vídeo gerado.
