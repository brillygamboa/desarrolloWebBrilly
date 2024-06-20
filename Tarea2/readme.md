# BlogWebApp

## Descripción

Este proyecto es una aplicación de blog desarrollada con Django. Permite a los usuarios autenticarse, publicar, comentar, dar like y administrar roles con distintos permisos.

## Funcionalidades

- Autenticación de usuarios
- Publicación de posts
- Comentarios en posts
- Sistema de likes
- Administración de roles y permisos:
  - **Administrador**: puede realizar todas las acciones CRUD de blog posts y comentarios de cualquier usuario.
  - **Moderador**: puede eliminar comentarios de otros usuarios, pero no puede borrar posts.
  - **Suscriptor**: puede comentar, borrar únicamente sus propios comentarios, y dar like/dislike a los posts y comentarios.

## Configuración

### Autenticación de Google

No se logró implementar el inicio de sesión con Google de manera completa. Al registrarse, se produce un error, pero el usuario se registra correctamente.

### Usuarios de prueba con roles

- **Moderador**:
  - Correo: `brilly.gamboa@ucr.ac.cr`
  - Contraseña: `briYOja-14`
  
- **Admin**:
  - Correo: `yordiga331@gmail.com`
  - Contraseña: `briYOja-14`
  
- **Suscriptor**:
  - Correo: `rviquezespinoza@gmail.com`
  - Contraseña: `briYOja-14`

### Acceso a la bitácora de acciones

Para ver la bitácora de acciones de los usuarios, ingresa a la siguiente URL:
[http://127.0.0.1:8000/user-action-log/](http://127.0.0.1:8000/user-action-log/)

## Uso

1. Visita `http://127.0.0.1:8000` en tu navegador.
2. Regístrate o inicia sesión utilizando uno de los usuarios de prueba mencionados arriba.
3. Realiza acciones según el rol asignado para interactuar con los posts y comentarios.
