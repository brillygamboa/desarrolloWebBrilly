# BlogWebApp

## Descripci�n

Este proyecto es una aplicaci�n de blog desarrollada con Django. Permite a los usuarios autenticarse, publicar, comentar, dar like y administrar roles con distintos permisos.

## Funcionalidades

- Autenticaci�n de usuarios
- Publicaci�n de posts
- Comentarios en posts
- Sistema de likes
- Administraci�n de roles y permisos:
  - **Administrador**: puede realizar todas las acciones CRUD de blog posts y comentarios de cualquier usuario.
  - **Moderador**: puede eliminar comentarios de otros usuarios, pero no puede borrar posts.
  - **Suscriptor**: puede comentar, borrar �nicamente sus propios comentarios, y dar like/dislike a los posts y comentarios.

## Configuraci�n

### Autenticaci�n de Google

No se logr� implementar el inicio de sesi�n con Google de manera completa. Al registrarse, se produce un error, pero el usuario se registra correctamente.

### Usuarios de prueba con roles

- **Moderador**:
  - Correo: `brilly.gamboa@ucr.ac.cr`
  - Contrase�a: `briYOja-14`
  
- **Admin**:
  - Correo: `yordiga331@gmail.com`
  - Contrase�a: `briYOja-14`
  
- **Suscriptor**:
  - Correo: `rviquezespinoza@gmail.com`
  - Contrase�a: `briYOja-14`

### Acceso a la bit�cora de acciones

Para ver la bit�cora de acciones de los usuarios, ingresa a la siguiente URL:
[http://127.0.0.1:8000/user-action-log/](http://127.0.0.1:8000/user-action-log/)

## Uso

1. Visita `http://127.0.0.1:8000` en tu navegador.
2. Reg�strate o inicia sesi�n utilizando uno de los usuarios de prueba mencionados arriba.
3. Realiza acciones seg�n el rol asignado para interactuar con los posts y comentarios.
