# taller_04

rest api con django y drf que se conecta al firebase realtime database para registrar y consultar actividades academicas.

endpoint: `/actividades/api/index/`

- `GET` devuelve las actividades guardadas
- `POST` registra una actividad con titulo, descripcion y responsable

la clave privada de firebase va en `secrets/actividades-key.json` y no se versiona.
