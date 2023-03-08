# UbicateUC-Backend

Backend del proyecto del semillero de investigación de Software SOLID de la universidad de Caldas.

## Guia de Instalación

Para realizar la instalacion y ejecucion del proyecto siga los siguientes pasos:

- Realice la clonacion del proyecto en su maquina local

```batch
    git clone https://github.com/CristianDavidEC/UbicateUC-Backend.git
```

- Una vez clonado, abra el repositorio en su terminal o con su editor de codigo.
- Inicie un entorno virtual en python en la carpeta raiz del repo con el siguiente comando.

```
    py -m venv venv
```

- Active el entorno virtual del proyecto si esta en la terminal de windows con el siguiente comando.

```
    venv\Scripts\activate
```

Si esta en la terminal de linux o mac con el siguiente comando.

```
    source venv/bin/activate
```

- Una vez activado el entorno virtual, instale las dependencias del proyecto con el siguiente comando.

```
    pip install -r requirements.txt
```

Esto realizara la instalacion de las dependencias del proyecto.

- Solicite el archivo .env al administrador del proyecto y coloque el archivo en la carpeta raiz del proyecto. Este archivo contine las variables de entorno del proyecto y la cadena de conexion a la base de datos.

- Desde la terminal abra la carpeta src, y ejecute el siguiente comado

```
    uvicorn main:app --reload
```

Este iniciara el servidor y los servicios Rest que ya existen.

- Una vez lanzado el servidor correctamente entre a su localhost o la direccion que su equipo definio.

- Con el http://127.0.0.1:8000/docs puede entrar a ver la documentacion de los endpoins.
