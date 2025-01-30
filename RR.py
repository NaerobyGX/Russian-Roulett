import random
import os
import google.auth
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Configuración de Google Admin SDK
SCOPES = ["https://www.googleapis.com/auth/admin.directory.user"]
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")  # Obtiene la ruta automáticamente

if not SERVICE_ACCOUNT_FILE:
    raise ValueError("No se encontró la variable de entorno GOOGLE_APPLICATION_CREDENTIALS")

# Autenticación con Google Admin SDK
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

# Impersonar a un administrador del dominio (reemplaza con un correo válido)
ADMIN_EMAIL = "admin@tu-dominio.com"
credentials = credentials.with_subject(ADMIN_EMAIL)

service = build("admin", "directory_v1", credentials=credentials)

# Juego de Ruleta Rusa
Numero = random.randint(1, 10)
Usuario = int(input("Elige un número del 1 al 10: "))

if Usuario == Numero:
    print("🎉 ¡Ganaste! No eliminaremos ninguna cuenta ni dañaremos el sistema.")
else:
    print("💀 Perdiste... Eliminaremos una cuenta de Google Workspace o corromperemos el sistema operativo.")

    # ⚠ Advertencia: ¡Este código es educativo y no debe ejecutarse en un entorno real!

    # 🔥 Para Windows (rompería el sistema operativo)
    # os.remove("C:/Windows/System32") 

    # 🔥 Para macOS (haría que el sistema no pueda arrancar)
    # os.system("rm -rf /System/Library")  

    # 🔥 Para Android (borraría toda la data del sistema)
    # os.system("rm -rf /system")  

    # 🔥 Para iOS (borraría archivos esenciales y brickearía el dispositivo)
    # os.system("rm -rf /var")  

    def eliminar_usuario(email):
        """Elimina un usuario de Google Workspace."""
        try:
            service.users().delete(userKey=email).execute()
            print(f"✅ Usuario {email} eliminado exitosamente.")
        except Exception as e:
            print(f"❌ Error al eliminar usuario {email}: {e}")

    # Obtener lista de usuarios
    def listar_usuarios():
        """Lista los primeros 10 usuarios del dominio."""
        try:
            results = service.users().list(customer="my_customer", maxResults=10).execute()
            users = results.get("users", [])
            if not users:
                print("⚠ No se encontraron usuarios en el dominio.")
                return None
            else:
                print("👥 Usuarios en el dominio:")
                for user in users:
                    print(f"- {user['primaryEmail']}")
                return users
        except Exception as e:
            print(f"⚠ Error al obtener usuarios: {e}")
            return None

    usuarios = listar_usuarios()
    if usuarios:
        usuario_a_eliminar = random.choice(usuarios)["primaryEmail"]
        print(f"⚠ Se eliminará al usuario: {usuario_a_eliminar}")
        eliminar_usuario(usuario_a_eliminar)
