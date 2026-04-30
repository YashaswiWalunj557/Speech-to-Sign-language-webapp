from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)


def translate_text(text, dest_lang="en"):
    try:
        translator = GoogleTranslator(source="auto", target=dest_lang)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {str(e)}"



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the frontend
        data = request.get_json()
        input_text = data.get("text")
        selected_language = data.get("language")

        # Perform the translation
        translation_result = translate_text(input_text, dest_lang=selected_language)

        # Return the result as JSON
        return translation_result


    # Render the HTML template for GET requests
    return render_template("hushtalk.html")


if __name__ == "__main__":
 app.run(debug=True)


