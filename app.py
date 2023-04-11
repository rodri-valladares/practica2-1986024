from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home-banking.html', saludo = persona1.nombre )

if __name__ == '__main__':
    from persona import Persona
    persona1 = Persona(36666777, 'Rodrigo')
    
    app.run(debug=True)