from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None

    if request.method == "POST":
        file = request.files.get("audio")

        if file:
            save_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(save_path)

            # for now – dummy output
            prediction = "Uploaded successfully (model not connected yet)"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)