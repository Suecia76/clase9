## Uso de Git

Crear una rama o branch llamada prueba, que es una breviatura de pruebaelopment, es decir, desarrollo:

    git branch prueba

cambiar a esa rama:

    git checkout prueba

listar las ramas para ver que se este bien parado.

    git branch

hacer los cambios necesarios y enviarlos al staging area.

    git add .

luego, crear un commit con un mensaje:

    git commit -m "mensaje"

una vez que se terminaron de hacer todos los commits necesarios y se los quiere fusionar a la rama principal, tener cuidado de no de jar archivos con cambios sin commit. pararse ne la rama principal:

    git checkout main

fusionar los commits de la rama prueba en main:

    git merge prueba

se puede seguir trabajando en prueba:

    git checkout prueba

o se la puede borrar:

    git branch -D prueba

cuando se quieran subir los cambios a la nube , es decir , a GitHub, cambiarse a la rama principal:

    git checkout main

y luego "empujar" todos los commits nuevos a la rama main de GitHub (se llama origin/main)

    git push
