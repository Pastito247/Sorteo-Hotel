# sorteo_valentin/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Establecer el entorno de configuración predeterminado de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sorteo_valentin.settings')

app = Celery('sorteo_valentin')

# Usamos string aquí para evitar el problema de importar la app cuando el worker está en ejecución.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Cargar tareas de todas las aplicaciones Django registradas.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
