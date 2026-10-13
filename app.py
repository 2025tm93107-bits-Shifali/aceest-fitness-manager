from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

tasks = [{"id": 1, "title": "Morning Gym Workout", "done": True}]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)