from flask import Flask, render_template, request, redirect
import json
import recite

app = Flask(__name__)

@app.route('/new', methods=['GET', 'POST'])
def new_schedule():
    if request.method == 'GET':
        return render_template('make_schedule.html')
    else:
        list_name = request.form['wordlist']
        r = [int(i) for i in request.form['range'].split('-')]
        daily_count = int(request.form['daily'])
        random = request.form.get('random', '0')
        if random == '1':
            random = True
        else:
            random = False
        wordlist = recite.load_word_list(list_name)[r[0]:r[1]]
        s = recite.make_schedule(wordlist, daily_count, random)
        return 'DONE'

@app.route('/')
def index():
    return redirect('/new')

if __name__ == '__main__':
    app.debug = True
    app.run()
