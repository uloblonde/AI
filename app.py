from flask import Flask,request,render_template
from sek import prediksi
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('tester.html')

@app.route("/pred", methods=['POST'])
def prediks():
    if request.method == 'POST':
        sbp = request.form['sbp']
        tobacco = request.form['tobacco']
        ldl = request.form['ldl']
        adiposity = request.form['adiposity']
        typea = request.form['typea']
        obesity = request.form['obesity']
        alcohol = request.form['alcohol']
        umur = request.form['umur']
        hasil = prediksi(sbp,tobacco,ldl,adiposity,typea,obesity,alcohol,umur)
        if (hasil== 1):
            output= "positif penyakit jantung"
            return render_template('tester.html', hasil=output)
        else :
            output= "negatif penyakit jantung"
            return render_template('tester.html', hasil=output)

if __name__ == '__main__':
    app.run(debug=True)



    
    






