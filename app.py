from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"

contacts = []  # In-memory storage for contacts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def show_contacts():
    return render_template('contacts.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')

    if not name:
        flash("Name is required!", "danger")
        return redirect(url_for('index'))

    contacts.append({'name': name, 'phone': phone, 'email': email})
    flash("Contact added successfully!", "success")
    return redirect(url_for('show_contacts'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
