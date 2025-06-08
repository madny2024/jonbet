# app.py
import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/resultados')
def api_resultados():
    cookies = { '_gid': 'GA1.2.781127896.1714749072', '_did': 'web_712234434B09A034', '_fbp': 'fb.1.1714749077202.1498210684', '_ga': 'GA1.1.1834781342.1714749072' }
    headers = { 'accept': 'application/json, text/plain, */*', 'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7', 'referer': 'https://jonbet.com/pt/games/double', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' }
    try:
        # Usamos a URL que retorna a lista de resultados recentes
        response = requests.get(
            'https://jonbet.bet.br/api/singleplayer-originals/originals/roulette_games/recent/1',
            cookies=cookies,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        
        # NOVO: Processa a lista completa
        if isinstance(data, list) and data:
            # Extrai o valor de 'roll' de cada objeto na lista usando "list comprehension"
            # e inverte a lista para que o mais antigo apareça primeiro na tela (opcional, mas bom para o layout)
            rolls = [item['roll'] for item in data if isinstance(item, dict) and 'roll' in item]
            return jsonify(rolls)

        return jsonify({"status": "waiting"})

    except Exception as e:
        print(f"Erro na requisição: {e}")
        return jsonify({"error": f"Falha ao se comunicar com a API externa: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)