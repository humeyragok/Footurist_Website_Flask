from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def home_tr():
    return render_template('index_tr.html')


from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dil yönlendirme
@app.route('/change-language')
def change_language():
    lang = request.args.get('lang')
    if lang:
        session['lang'] = lang
    return redirect(request.referrer or '/')

# Ana sayfa
@app.route('/')
def home():
    lang = session.get('lang', 'en')  # Varsayılan dil İngilizce
    if lang == 'tr':
        return render_template('index_tr.html')
    return render_template('index.html')

# Hakkımızda sayfası
@app.route('/about.html')
def about():
    lang = session.get('lang', 'en')
    if lang == 'tr':
        return render_template('about_tr.html')
    return render_template('about.html')

# Proje sayfası
@app.route('/projeler.html')
def projeler():
    lang = session.get('lang', 'en')
    if lang == 'tr':
        return render_template('projeler_tr.html')
    return render_template('projeler.html')

# İletişim sayfası
@app.route('/contact.html')
def contact():
    lang = session.get('lang', 'en')
    if lang == 'tr':
        return render_template('contact_tr.html')
    return render_template('contact.html')

# Diğer sayfalar için de benzer şekilde yönlendirme ekleyebilirsiniz.



if __name__ == '__main__':
    app.run(debug=True)



