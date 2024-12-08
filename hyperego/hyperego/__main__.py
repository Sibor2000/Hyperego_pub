import cherrypy
from ws4py.server.cherrypyserver import WebSocketTool, WebSocketPlugin
from server import WebService, WebSocketHandler
import warnings
import dotenv

# Enable the WebSocket tool in CherryPy
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

def cors_tool():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

def handle_options():
    if cherrypy.request.method == "OPTIONS":
        print("Handling options")
        cherrypy.response.status = 200
        cherrypy.response.body = b""  # Empty body for the response
        return True

cherrypy.tools.cors = cherrypy.Tool("before_handler", cors_tool)
cherrypy.tools.handle_options = cherrypy.Tool("before_handler", handle_options)

if __name__ == '__main__':
    warnings.filterwarnings("ignore", message=".*construct method is deprecated.*")

    # Load environment variables
    dotenv.load_dotenv()

    cherrypy.config.update({
        'server.socket_port': 8080,
        'server.socket_host': '0.0.0.0',
    })

    # Mount websocket handler
    cherrypy.tree.mount(
        WebService(), '/', config={
            '/ws': {
                'tools.websocket.on': True,
                'tools.websocket.handler_cls': WebSocketHandler,
                'tools.cors.on': True
            },
            '/': {
                'tools.cors.on': True,
                'tools.handle_options.on': True
            }
        }
    )

    # Start the app
    cherrypy.engine.start()
    cherrypy.engine.block()