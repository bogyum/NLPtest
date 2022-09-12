from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_home():
    return render_template('views/main.html')

@app.route('/analysis/<input_file>/<method>')
def wordcloud():
    wordcloud_from_text(input_file, input_file + '.png', method)                  
    
    
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
