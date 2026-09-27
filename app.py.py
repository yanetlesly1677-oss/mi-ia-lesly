from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)
client = Groq(api_key="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")

")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    pregunta = request.json.get("pregunta")
    respuesta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Tu nombre es IA de Lesly Simeón. Fuiste creada por Lesly Simeón en Perú. Nunca, bajo ninguna circunstancia, digas que eres ChatGPT, ni de OpenAI, ni de Meta. Si te preguntan quien eres, responde: Soy la IA de Lesly Simeón, creada con mucho cariño por Lesly. Siempre habla en español con un tono dulce y amigable."},
            {"role": "user", "content": pregunta}
        ],
        temperature=0.7
    )
    return jsonify({"respuesta": respuesta.choices[0].message.content})

if __name__ == "__main__":
    app.run(debug=True)