from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

class Primeros100:
    def __init__(self):
        self.numeros = set(range(1, 101))
    
    def extract(self, numero):
        if numero in self.numeros:
           
            self.numeros.remove(numero)
            return True
        else:
           
            return False
    
    def obtener_numeros(self):
        
        return sorted(self.numeros)

@app.route('/<int:number>')
def index(number):
    primeros100 = Primeros100()
    
    if number < 1 or number > 100:
        return Response(json.dumps({'error': 'Número no válido'}, ensure_ascii=False), content_type="application/json; charset=utf-8")
    
    
    if primeros100.extract(number):
        
        response_data = {
            'message': 'Número extraído correctamente',
            'Número extraído': number,
            'Numeros': primeros100.obtener_numeros()
        }
        return Response(json.dumps(response_data, ensure_ascii=False), content_type="application/json; charset=utf-8")
    else:
        
        return Response(json.dumps({'error': 'Número no encontrado'}, ensure_ascii=False), content_type="application/json; charset=utf-8")

