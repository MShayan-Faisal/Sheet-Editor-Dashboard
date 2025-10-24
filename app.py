from flask import Flask, render_template, request, redirect, url_for
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

app = Flask(__name__)

SERVICE_ACCOUNT_FILE = 'credentials.json'
SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(creds)
spreadsheet = client.open("Test Project")


# 🏠 Home - View Combined Data
@app.route('/')
def index():
    translator_data = spreadsheet.worksheet("Translator").get_all_records()
    summary_data = spreadsheet.worksheet("data").get_all_records()

    for i, row in enumerate(translator_data, start=2):
        row["App"] = "Translator"
        row["Index"] = i
        # Ensure all expected keys exist
        row.setdefault("Date", "")
        # row.setdefault("Text", "")
        # row.setdefault("Result", "")

    for i, row in enumerate(summary_data, start=2):
        row["App"] = "Data"
        row["Index"] = i
        row.setdefault("Date", "")
        # row.setdefault("Text", "")
        # row.setdefault("Result", "")

    combined = translator_data + summary_data
    return render_template("index.html", data=combined)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        app_type = request.form['app']
        date = datetime.today().strftime('%Y-%m-%d')

        if app_type == 'Translator':
            text = request.form['text']
            result = request.form['result']
            spreadsheet.worksheet(app_type).append_row([date, text, result])
        else:
            impression = request.form['impression']
            vister = request.form['vister']
            spreadsheet.worksheet(app_type).append_row([date, impression, vister])

        return redirect(url_for('index'))

    return render_template('add.html')


# 🛠 Manage Data (Edit/Delete)
@app.route('/manage')
def manage():
   
    data = spreadsheet.worksheet("data").get_all_records()
    translator = spreadsheet.worksheet("Translator").get_all_records()

    for i, row in enumerate(data):
        row["App"] = "data"
        row["Index"] = i + 2
        row.setdefault("Date","")
        row.setdefault("Impression","")
        row.setdefault("Visitor","")

    for i, row in enumerate(translator):
        row["App"] = "Translator"
        row["Index"] = i + 2
        row.setdefault("Date", "")
        row.setdefault("Impression", "")
        row.setdefault("Visitor", "")

    combined = translator + data
    return render_template("manage.html", data=combined)


@app.route('/edit', methods=['POST'])
def edit():
    app_type = request.form['app']
    index = int(request.form['index'])
    date = request.form['date']

    # Normalize sheet name
    sheet_name = "data" if app_type.lower() == "data" else "Translator"
    worksheet = spreadsheet.worksheet(sheet_name)

    impression = request.form['Impression']
    visitors = request.form['Visitor']

    worksheet.update(f'A{index}:C{index}', [[date,  visitors, impression]])

    return redirect(url_for('manage'))


@app.route('/delete', methods=['POST'])
def delete():
    app_type = request.form['app']
    index = int(request.form['index'])

    # Normalize sheet name
    sheet_name = "data" if app_type.lower() == "data" else "Translator"
    worksheet = spreadsheet.worksheet(sheet_name)

    worksheet.delete_rows(index)
    return redirect(url_for('manage'))



if __name__ == '__main__':
    app.run(debug=True)
