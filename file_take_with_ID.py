from flask import Flask, request, render_template_string
import os
import time

UPLOAD_FOLDER = r"C:\Users\UIU\Desktop\UploadedZIP"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 200 * 1024 * 1024  # 200MB

HTML = """
<!DOCTYPE html>
<html>
<body>
    <h2>Student ZIP Upload Portal</h2>

    <form method="POST" enctype="multipart/form-data">
        <label>Student ID:</label><br>
        <input type="text" name="sid" required><br><br>

        <label>Choose ZIP File:</label><br>
        <input type="file" name="file" accept=".zip" required><br><br>

        <button type="submit">Upload</button>
    </form>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        sid = request.form.get("sid")

        if not sid:
            return "Student ID required!"

        file = request.files["file"]
        if file.filename == "":
            return "No file selected!"

        if not file.filename.lower().endswith(".zip"):
            return "Only .zip file allowed!"

        # Student folder auto create
        student_folder = os.path.join(app.config["UPLOAD_FOLDER"], sid)
        os.makedirs(student_folder, exist_ok=True)

        # Unique filename
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        final_name = f"{timestamp}_{file.filename}"

        save_path = os.path.join(student_folder, final_name)
        file.save(save_path)

        return f"Upload Successful! Saved in folder: {sid}"

    return render_template_string(HTML)


if __name__ == "__main__":
    print("Server running at: http://0.0.0.0:5000/")
    app.run(host="0.0.0.0", port=5000)
