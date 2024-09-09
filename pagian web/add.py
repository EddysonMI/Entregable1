from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'mi_llave_secreta'  # Llave para manejar sesiones

# Lista de autos deportivos
sports_cars = [
    {"name": "Ferrari F8 Tributo", "price": "$276,550", "description": "El Ferrari F8 Tributo es un auto V8 que redefine el rendimiento con un motor de 720 CV."},
    {"name": "Lamborghini Aventador", "price": "$393,695", "description": "El Lamborghini Aventador es un superdeportivo con un motor V12 de 770 CV, capaz de alcanzar los 350 km/h."},
    {"name": "Porsche 911 Turbo S", "price": "$207,000", "description": "El Porsche 911 Turbo S combina lujo y velocidad, con un motor de 640 CV y tracción en las cuatro ruedas."},
    {"name": "McLaren 720S", "price": "$299,000", "description": "El McLaren 720S es un superdeportivo británico con un motor V8 biturbo que genera 710 CV."},
    {"name": "Aston Martin Vantage", "price": "$139,000", "description": "El Aston Martin Vantage es un auto de lujo con un motor V8, capaz de generar 503 CV."}
]

# Lista de motos deportivas
sports_bikes = [
    {"name": "Yamaha YZF-R1", "price": "$17,399", "description": "La Yamaha YZF-R1 cuenta con un motor de 998cc y es conocida por su tecnología de MotoGP."},
    {"name": "Kawasaki Ninja H2", "price": "$29,500", "description": "La Kawasaki Ninja H2 es una moto sobrealimentada con 231 CV, capaz de alcanzar velocidades extremas."},
    {"name": "Ducati Panigale V4", "price": "$28,395", "description": "La Ducati Panigale V4 tiene un motor de 1,103cc y ofrece una experiencia de conducción de alto rendimiento."},
    {"name": "BMW S1000RR", "price": "$16,995", "description": "La BMW S1000RR es una superbike con un motor de 999cc y tecnología avanzada para carreras."},
    {"name": "Suzuki GSX-R1000R", "price": "$17,749", "description": "La Suzuki GSX-R1000R es una de las superbikes más ligeras, con un motor de 999cc y 199 CV."}
]

@app.route('/')
def home():
    # Verificar si el usuario ha iniciado sesión
    if 'username' in session:
        return render_template('index.html', cars=sports_cars, bikes=sports_bikes)
    else:
        return redirect(url_for('login'))  # Si no ha iniciado sesión, redirigir al login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario de login
        username = request.form['username']
        password = request.form['password']

        # Validar credenciales (usuario: admin, contraseña: password123)
        if username == 'Masculino' and password == 'password123':
            session['username'] = username  # Guardar usuario en la sesión
            return redirect(url_for('home'))  # Redirigir al home si es exitoso
        else:
            error = 'Credenciales incorrectas, inténtalo de nuevo.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Eliminar el usuario de la sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
