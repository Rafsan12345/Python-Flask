from flask import Flask, request, render_template_string
import os

UPLOAD_FOLDER = r"C:\Users\UIU\Desktop\UploadedZIP"   # ← আপনার নিজের path দিন
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

HTML = """
<!DOCTYPE html>
<html>
<body>
    <h2>Student ZIP Upload Portal</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" accept=".zip" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        # Check .zip format
        if not file.filename.lower().endswith(".zip"):
            return "Only .zip file allowed!"

        save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(save_path)

        return f"Uploaded Successfully: {file.filename}"

    return render_template_string(HTML)


if __name__ == '__main__':
    print("Server running on: http://0.0.0.0:5000/")
    app.run(host="0.0.0.0", port=5000)
