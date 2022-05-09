from usuario_dao import UsuarioDao
from logger_base import log
from usuario import Usuario

opcion = None
while opcion != 5:
    print('Opciones: ')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el nombre de usuario: ')
        password_var = input('Escribe el password del usuario: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuario insertado: {usuarios_insertados}')
    elif opcion == 3:
        id_user_var = int(input('Escribe el id usuario a modificar: '))
        username_act_var = input('Escribe el nuevo nombre de usuario: ')
        password_act_var = input('Escribe el nuevo password de usuario: ')
        usuario = Usuario(username=username_act_var, password=password_act_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuarios_actualizados}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'Usuario eliminado : {usuario_eliminados}')


else:
    log.info("Salimos de nuestra aplicacion .......")




