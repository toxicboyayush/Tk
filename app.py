from flask import Flask, request, jsonify
import os
from Login import LoginCookie
from GetToken import TokenEAAG, TokenEAAB, TokenEAAD, TokenEAAC, TokenEAAF, TokenEABB
import requests as req_lib

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <body style="font-family: Arial; padding: 50px; max-width: 800px; margin: auto;">
        <h1>Facebook Token Generator</h1>
        <input id="cookie" type="text" placeholder="Facebook Cookie Paste Karo" style="width: 100%; padding: 10px; margin: 10px 0;">
        <button onclick="getTokens()" style="padding: 10px 20px;">Get Tokens</button>
        <div id="result" style="margin-top: 20px;"></div>
        
        <script>
        async function getTokens() {
            const cookie = document.getElementById('cookie').value;
            const result = document.getElementById('result');
            
            result.innerHTML = 'Loading...';
            
            const response = await fetch('/api/tokens', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({cookie: cookie})
            });
            
            const data = await response.json();
            
            if (data.error) {
                result.innerHTML = '<p style="color:red;">' + data.error + '</p>';
            } else {
                result.innerHTML = `
                    <p><b>EAAG:</b> ${data.EAAG}</p>
                    <p><b>EAAB:</b> ${data.EAAB}</p>
                    <p><b>EAAD:</b> ${data.EAAD}</p>
                    <p><b>EAAC:</b> ${data.EAAC}</p>
                    <p><b>EAAF:</b> ${data.EAAF}</p>
                    <p><b>EABB:</b> ${data.EABB}</p>
                `;
            }
        }
        </script>
    </body>
    </html>
    '''

@app.route('/api/tokens', methods=['POST'])
def get_tokens():
    try:
        cookie = request.json.get('cookie')
        r = req_lib.Session()
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        
        validated = LoginCookie(r, ua, cookie)
        if not validated:
            return jsonify({'error': 'Invalid cookie'}), 401
        
        return jsonify({
            'EAAG': TokenEAAG(r, validated),
            'EAAB': TokenEAAB(r, validated),
            'EAAD': TokenEAAD(r, validated),
            'EAAC': TokenEAAC(r, validated),
            'EAAF': TokenEAAF(r, validated),
            'EABB': TokenEABB(r, validated)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
```

---

## 📁 **Ab Tumhari Files Aise Honi Chahiye:**
```
├── app.py              ← NAYA (upar wala code)
├── requirements.txt    ← EDIT KIYA (sirf 3 lines)
├── Login.py            ← Pehle se hai
├── GetToken.py         ← Pehle se hai
├── Tools.py            ← Pehle se hai
└── __init__.py         ← Pehle se hai
