import flask
import socket
import os

num_visitas = 0
# Crear el objeto que representa la aplicacion web
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    global num_visitas

    """ Muestra la página inicial asociada al recurso `/`
        y que estará contenida en el archivo index.html
    """
    userinfo = {
        'surname': os.environ['CLIENT_NAME']
    }
    num_visitas = num_visitas + 1 
    hostname = socket.gethostname()
    return flask.render_template('index.html', vis=num_visitas,
            user=userinfo, server_name=hostname)

if __name__ == '__main__':
    PORT=os.environ['PORT']
    APP.debug=True
    APP.run(host='0.0.0.0', port=PORT)

