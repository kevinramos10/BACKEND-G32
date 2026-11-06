from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['if_staff', 'is_superuser', 'is_active', 'user_permissions', 'last_login', 'groups']

        #Si queremos condicionar un atributo a que solo sea lectura o solo escritura entonces se recomieda usar extra_kwargs
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class LoginSerializer(Serializer):
    correo = EmailField(required=True)
    password = CharField(required=True)