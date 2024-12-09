# Axmed Catalogue API

## Descripción

API para gestionar el catálogo de SKUs de medicamentos de la plataforma Axmed. Permite a los usuarios realizar operaciones CRUD y cargas masivas de SKUs.

## Requisitos

- Python 3.8+
- pip
- virtualenv (opcional pero recomendado)
- Git

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/tu_usuario/axmed_catalogue.git
   cd axmed_catalogue
   ```

2. **Crear y Activar un Entorno Virtual**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar Migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Crear un Superusuario (Opcional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el Servidor de Desarrollo**

   ```bash
   python manage.py runserver
   ```

   La API estará disponible en `http://localhost:8000/api/`.

## Uso de la API

## Autenticación JWT

La API utiliza **JSON Web Tokens (JWT)** para la autenticación. A continuación, se describen los pasos para registrarse, iniciar sesión y utilizar los tokens para acceder a las rutas protegidas.

### 1. Registrar un Usuario

- **Endpoint:** `/api/register/`
- **Método:** POST
- **Body:**
  ```json
  {
    "username": "testuser",
    "password": "testpassword123",
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User"
  }
  ```

### 2. Obtener Tokens JWT

- **Endpoint:** `/api/token/`
- **Método:** POST
- **Body:**
  ```json
  {
    "username": "testuser",
    "password": "testpassword123"
  }
  ```
- **Respuesta:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

### 3. Refrescar Token de Acceso

- **Endpoint:** `/api/token/refresh/`
- **Método:** POST
- **Body:**
  ```json
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```
- **Respuesta:**
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

### 4. Acceder a Rutas Protegidas

Incluye el token de acceso en el encabezado de autorización de tus peticiones:

### Endpoints

- **Listar SKUs**

  - **Método:** GET
  - **URL:** `/api/skus/`

- **Crear SKU**

  - **Método:** POST
  - **URL:** `/api/skus/`
  - **Body:** JSON
    ```json
    {
      "medication_name": "Amoxicillin",
      "presentation": "Tablet",
      "dose": "50",
      "unit": "mg"
    }
    ```

- **Detalles de SKU**

  - **Método:** GET
  - **URL:** `/api/skus/{id}/`

- **Actualizar SKU**

  - **Método:** PUT
  - **URL:** `/api/skus/{id}/`
  - **Body:** JSON

- **Eliminar SKU**

  - **Método:** DELETE
  - **URL:** `/api/skus/{id}/`

- **Carga Masiva de SKUs**
  - **Método:** POST
  - **URL:** `/api/skus/bulk_create/`
  - **Body:** JSON Array
    ```json
    [
      {
        "medication_name": "Ibuprofen",
        "presentation": "Capsule",
        "dose": "200",
        "unit": "mg"
      },
      {
        "medication_name": "Paracetamol",
        "presentation": "Tablet",
        "dose": "500",
        "unit": "mg"
      }
    ]
    ```

### Ejemplos de Uso con Postman

Importa la colección de Postman incluida en el repositorio para probar los endpoints de manera sencilla.

## Pruebas

Para ejecutar los tests, utiliza el siguiente comando:

```bash
python manage.py test

```
