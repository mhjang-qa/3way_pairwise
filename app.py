from flask import Flask, render_template, request, redirect, url_for, session, abort, send_from_directory

app = Flask(__name__)
app.secret_key = 'QA-team-is-best-team'

# ✅ 허용된 IP 목록
ALLOWED_IPS = {
    "219.240.45.245",
    "175.120.219.199",
    "218.237.59.80",
    "121.141.180.210"
}

# ✅ 요청 전에 IP 검사
@app.before_request
def limit_remote_addr():
    client_ip = request.remote_addr
    if client_ip not in ALLOWED_IPS:
        return "접근이 허용되지 않은 IP입니다.", 403

# ✅ 관리자 계정
VALID_USERS = {
    'mino': 'mino',
    'khs06': 'plateerkhs06',
    'jekim': 'admin0218?',
    'sen9088': 'xptmxm123!'
    
}

@app.route('/')
def home():
    if 'user' in session:
        return render_template('index.html', username=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if VALID_USERS.get(username) == password:
            session['user'] = username
            return redirect(url_for('home'))
        else:
            error = '아이디 또는 비밀번호가 올바르지 않습니다.'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True, port=10000)