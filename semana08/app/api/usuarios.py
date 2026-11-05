from flask_restful import Resource, request
from app.extensions import db
from app.schemas import RegistroUsuarioSchema, LoginUsuarioSchema, UsuarioSchema, ResetPasswordSchema
from pydantic import ValidationError
from app.models import Usuario
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from cryptography import fernet


class RegistroController(Resource):
    def post(self):
        try:
            datavalidada = RegistroUsuarioSchema.model_validate(request.get_json())
            print(datavalidada)

            usuarioExistente = db.session.query(Usuario).with_entities(Usuario.correo == datavalidada.correo).first()

            if usuarioExistente:
                return{
                    'message':'Usuario ya existe'
                }, 400

            #Proceso del hashin de la contrase;a

            #1. texto de ayuda
            salt = gensalt(12)
            
            #2. Convertimos password a bits
            password = datavalidada.password.encode()

            #3. Hasinh de la contraseña
            password_hasheada_bytes = hashpw(password, salt)

            #4. convertimos el hashing del password en bytes a str
            password_hasheada = password_hasheada_bytes.decode()

            print(password_hasheada)

            nuevoUsuario = Usuario(correo = datavalidada.correo, password = password_hasheada, nombre = datavalidada.nombre, apellido = datavalidada.apellido)

            db.session.add(nuevoUsuario)
            db.session.commit()


            return{
                'message': 'Usuario registrado exitosamente'
            }, 201

        except ValidationError as error:
            return{
                'message': 'Error al crear el usuario',
                'content': error.errors(include_context=False)
            }, 400


class LoginController(Resource):
    def post(self):

        try:
            dataValidada = LoginUsuarioSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()

            if not usuarioEncontrado:
                return{
                    'message': 'Usuario no existe'
                }

            password = dataValidada.password.encode()
            hashedPassword = usuarioEncontrado.password.encode()

            EsLaPassword = checkpw(password, hashedPassword)

            if EsLaPassword:
                jwt = create_access_token( identity=usuarioEncontrado.id, 
                                    fresh=False, 
                                    expires_delta=timedelta(hours=8, minutes=5))
                return{
                    'content': jwt
                }
            else:
                return{
                    'message': 'Credenciales incorrectas'
                }, 400

        except ValidationError as error:
            return{
                'message': 'Error al hacer el login',
                'content': error.errors(include_context=False)
            }, 400


class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        id = get_jwt_identity()

        usuarioEncontrado = db.session.query(Usuario).filter(Usuario.id == id).first()

        resultado = UsuarioSchema.model_validate(usuarioEncontrado).model_dump(mode='json')

        return{
            'content': resultado
        }

class ChangePasswordController(Resource):
    @jwt_required()
    def post(self):

        try:
            dataValidada = ResetPasswordSchema.model_validate(request.get_json())

            return

            return{
                'message': 'Password cambiada exitosamente!'
            }
        except ValidationError as error:
            return{
                'message': 'Error al hacer el login',
                'content': error.errors(include_context=False)
            }, 400

class ResetPasswordController(Resource):
    def post(self):
        try:
            dataValidada = ResetPasswordSchema.model_validate(request.get_json())

            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()

            if not usuarioEncontrado:
                return{
                    'message': 'Usuario no existe en el sistema'
                }, 400

            key = fernet.Fernet.generate_key()
            print(key)
            
            return{
                'message': 'Se envio al correo'
            }

        except ValidationError as error:
            return{
                'message': 'Error al resetear la password',
                'content': error.errors(include_context=False)
            },400