from dotenv import load_dotenv
load_dotenv()

# Importacions espcificaas
from app import create_app

#Importaciones totales (toda la inforamcion del arcivo)
#import app

app = create_app()

if __name__ == "__main__":
    app.run()