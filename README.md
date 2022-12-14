# Introduccion

Este es el Backend del Proyecto Final de la asignatura Aplicaciones en la WEB y Redes Inalámbricas

Integrantes:

- Miguel Ángel Rincón Clavijo - 1942985
- Carlos Bermudez Valencia - 1927623
- Daniel Felipe Vélez Cuaical - 1924306
- Juan Esteban Camargo Chacón - 1924984
- Alejandro Satizabal Narvaez - 1726041

### _Requerimientos_

- Python3
- Pipenv
- postgresql

### _Instalacion_

- Clonar el proyecto a tu maquina local `git clone https://github.com/Juanescacha/Back-Proyecto-WWW`
- Crear y activar el entorno virtual de python `python3 -m venv venv`
- Instalar los requerimientos del proyecto los cuales estan en **requirements.txt** esto lo hacemos ejecutando: `pip install -r requirements.txt`
- Ejecutar el comando `python manage.py makemigrations` y luego `python manage.py migrate`

### _Ejecutar la Aplicacion_

Vas a necesitar dos terminales, una para el frontend y otra para el backend para iniciar los servidores de esta aplicacion.

1. Ejecutar este comando para inciar el servidor de backend `python manage.py runserver` (recuerda ejecutar este comando teniendo activo el entorno virtual)

2. Ejecutar este comando para iniciar el servidor del frontend del repositorio `https://github.com/Juanescacha/Front-Proyecto-WWW` `npm start` (esto iniciara el frontend en [localhost:3000](localhost:3000))

### _Construido con_

- [Django](https://www.djangoproject.com/) - un framework de desarrollo web de alto nivel escrito en Python que fomenta el desarrollo rápido y un diseño limpio y pragmático.

- [React](https://es.reactjs.org/) - una biblioteca JavaScript de código abierto con fines de desarrollo de interfaces de usuario en el front-end.

- [Python](https://www.python.org/) - un lenguaje de programación interpretado cuya filosofía hace hincapié en una sintaxis que favorezca un código legible.

- [Postgresql](https://www.postgresql.org/) - un sistema de gestión de bases de datos objeto relacional (ORDBMS) de código abierto.
