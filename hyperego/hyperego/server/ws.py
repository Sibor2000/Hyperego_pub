import json
from ws4py.websocket import WebSocket

from .shared import ServerState

class WebSocketHandler(WebSocket):
    def __init__(self, *args, **kwargs):
        super(WebSocketHandler, self).__init__(*args, **kwargs)
        self.token = None
        self.state = ServerState()
        
    def received_message(self, message):
        try:
            data = json.loads(str(message))
            if data.get('token') is not None:
                self.token = data['token']
                self.state.ws_conns[self.token] = self
                print("Token received", self.token)
        except Exception:
            pass
                

    def closed(self, code, reason=""):
        # Handle WebSocket closing
        print(f"WebSocket closed with code {code}, reason: {reason}")