from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from ddgs import DDGS

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    mensaje = request.json.get("mensaje", "")
    try:
        with DDGS() as ddgs:
            res = list(ddgs.text(mensaje, max_results=2))
            info = str(res)
    except:
        info = ""
    prompt = f"Eres IA Lesly de Lima Peru. Info: {info}. Pregunta: {mensaje}"
    chat = client.chat.completions.create(model="openai/gpt-oss-20b", messages=[{"role":"user","content":prompt}])
    return jsonify({"respuesta": chat.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
