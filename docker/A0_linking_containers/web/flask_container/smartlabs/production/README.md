### Environment variables

In order to test that flask application will take the configurations at the production_settings.py file, in the development environment create the production environment variables:

```sh
export PG_PORT_5432_TCP_PORT=5432
export PG_PORT_5432_TCP_ADDR=172.17.0.2
export SMARTLABS_SETTINGS=production_settings.py
```