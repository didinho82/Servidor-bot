import os
import staypresent

# 1. Configura uma resposta simples para o Render ver que o serviço está vivo.
# Isso satisfaz a exigência do Render de ter uma porta HTTP respondendo [citation:1].
staypresent.web.json({"status": "running", "service": "meu-bot-24h"})

# 2. AUTO-PING: Substitua a URL abaixo pela URL real do seu serviço no Render.
# O intervalo é de 240 segundos (4 minutos), seguro pois o Render dorme após 15 min [citation:2].
# O ping PRECISA ser na URL pública (https://...onrender.com) [citation:1].
staypresent.cron(
    "https://servidor-bot-1-49ck.onrender.com", 
    interval=240,
    on_failure=lambda r: print(f"Falha no auto-ping: {r['error']}")
)

# 3. Inicia o seu bot (o código do bot deve estar no arquivo bot.py).
# Ele lê a porta que o Render injeta automaticamente na variável PORT [citation:1].
staypresent.run(
    "bot.py",
    port=int(os.getenv("PORT", 8080)),
    restart_on_crash=True,  # Reinicia o bot se ele cair [citation:2]
    max_restarts=5          # Evita loop infinito de crashes
)
