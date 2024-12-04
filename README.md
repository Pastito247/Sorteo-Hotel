# Sorteo-Hotel

Esta es una aplicación full-stack de un sorteo para San Valentín, donde los usuarios pueden registrarse, verificar su correo, y participar en el sorteo de un hotel. La aplicación está dividida en dos partes: el **Backend** (API REST en Django) y el **Frontend** (interfaz de usuario con Vue.js).

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados los siguientes programas en tu máquina:

- Python 3.x
- Node.js (al menos versión 14.x)
- Redis (para las tareas en segundo plano con Celery)
- Git

## Backend (Django + DRF)

### 1. Clonar el Repositorio

Primero, clona el repositorio:

```bash
git clone <url_del_repositorio>
cd sorteo_valentin
```
### 2. Crea un entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate
```
### 3. Instala requirement.txt
```bash
pip install -r requirements.txt
```
### 4. Corre la base de datos
```bash
python manage.py migrate
```
### 5. dentro del entorno virtual ejecuta esto en distintas terminales
```bash
redis-server --port 6380 #Terminal 1
celery -A sorteo_valentin worker --loglevel=info --pool=solo #Terminal 2
python manage.py runserver #Terminal 3
```
### 6. Clona el Front End
```bash
cd frontend
npm install
npm run dev
```
# Credentials Administrator
```bash
correo: admin@example.com
contraseña: ADMIN
```
# Flujo de Trabajo
# Registro de Usuario
Los usuarios pueden registrarse proporcionando su correo electrónico y contraseña.
El sistema enviará un correo de verificación. Los usuarios deberán verificar su correo para completar el registro.
# Participación en el Sorteo
 Una vez autenticados, los usuarios pueden acceder a la página para participar en el sorteo.
 Los usuarios no admin o staff pueden generar un ganador, mientras que los administradores o el personal pueden gestionar el sorteo.
# Verificación de Correo
Un correo será enviado con un enlace de verificación. Al hacer clic, se verificará la cuenta del usuario y se podrá iniciar sesión.
# Notas
Asegúrate de tener CORS habilitado en Django para permitir que el frontend haga solicitudes a la API.
Si estás utilizando Redis para Celery, asegúrate de que esté configurado correctamente.
El proyecto está configurado para correr en un entorno local. Si planeas desplegarlo en producción, necesitarás ajustar la configuración de CORS, el entorno de la base de datos, y la seguridad.


 Este `README.md` cubre todos los pasos para configurar y ejecutar tanto el backend como el frontend en tu entorno local. Asegúrate de seguir cada paso según corresponda.
