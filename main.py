from flask import Flask, render_template, request, redirect, url_for, flash, session
import secrets
app = Flask(__name__)
app.secret_key = 'supersecretkey_used_for_flask_session'

#generating key
Key = secrets.token_hex(16)
ADMIN_KEY = Key

print(Key)

#Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        key = request.form['key']
        if key == ADMIN_KEY:
            session['logged_in'] = True
            return redirect(url_for('admin_page'))
        else:
            flash('Invalid key. Please try again.')
    return render_template('login.html')

# Admin
@app.route('/admin')
def admin_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('admin.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)