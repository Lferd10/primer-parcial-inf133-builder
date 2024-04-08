from http.server import HTTPServer, BaseHTTPRequestHandler

import json

class Personaje:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.level = None
        self.role = None
        self.charisma = None
        self.strength = None
        self.dexterity = None
    
    def __str__(self):
        return f"id: {self.id}, Name: {self.name}, Level: {self.level}, Role: {self.role}, Charisma: {self.charisma}, Strength: {self.strenght}, Dexterity: {self.dexterity}"

class PersonajeBuilder:
    def __init__(self):
        self.personaje = Personaje
    
    def set_id(self, id):
        self.personaje.id = id
    
    def set_name(self, name):
        self.personaje.name = name
    
    def set_level(self, level):
        self.personaje.level = level
        
    def set_role(self, role):
        self.personaje.role = role
    
    def set_charisma(self, charisma):
        self.personaje.charisma = charisma
    
    def set_strength(self, strength):
        self.personaje.strength = strength
    
    def set_dexterity(self, dexterity):
        self.personaje.dexterity = dexterity
    
    def get_personaje(self):
        return self.personaje
    
class Personajes:
    def __init__(self, builder):
        self.builder = builder

    def create_personaje(self, id, name, level, role, charisma, strength, dexterity):
        self.builder.set_id = id
        self.builder.set_name = name
        self.builder.set_level = level
        self.builder.set_role = role
        self.builder.set_charisma = charisma
        self.builder.set_strength = strength
        self.builder.set_dexterity = dexterity
        return self.builder.get_personaje



class PersonajeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/characters':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
    
    def do_POST(self):
        if self.path == '/characters':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
    def do_PUT(self):
        pass
    
    def do_DELETE(self):
        pass






def run(server_class=HTTPServer, handler_class=PersonajeHandler, port=8000):
    server_dir = ('', port)
    httpd = server_class(server_dir, handler_class)
    print(f"Iniciando servidor HTTP en puerto {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()