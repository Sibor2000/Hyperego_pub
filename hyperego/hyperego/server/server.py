import json
import cherrypy
from hyperego.core import HyperegoRunConfig, HyperegoRun
from .shared import ServerState
import uuid
import asyncio
from threading import Thread

class WebService:
    def __init__(self):
        self.runs = {}
        self.state = ServerState()
    
    def create_publisher(self, token):
        def publish(progress):
            if token in self.state.ws_conns:
                self.state.ws_conns[token].send(json.dumps(progress))
        return publish
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def version(self):
        return {"version": "0.1.0"}
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def analyze(self):
        """Starts a hyperego run by allocating a websocket token"""

        if cherrypy.request.method == "OPTIONS":
            return None
        
        if cherrypy.request.method != "POST":
            cherrypy.response.status = 405
            return {"error": "Method not allowed"}

        try:
            data = cherrypy.request.json
            # Deserialize into a dataclass
            config = HyperegoRunConfig(**data)

            # Validate the data
            config.validate()

        except TypeError as e:
            cherrypy.response.status = 400
            return {"success": False, "error": "Invalid data structure", "details": str(e)}
        except ValueError as e:
            cherrypy.response.status = 400
            return {"success": False, "error": "Invalid data", "details": str(e)}
        except Exception as e:
            cherrypy.response.status = 500
            return {"success": False, "error": "Internal server error", "details": str(e)}

        # Create a token (uuid)
        token = str(uuid.uuid4())
        publisher = self.create_publisher(token)
        run = HyperegoRun(config, progress_callback=publisher)
        self.runs[token] = run
        
        # Create a thread to run the hyperego run
        thread = Thread(target=lambda: asyncio.run(run.run()))
        thread.start()  

        return {"success": True, "token": token}
    
    @cherrypy.expose
    def ws(self):        
        # Upgrade the connection to a WebSocket
        handler = cherrypy.request.ws_handler