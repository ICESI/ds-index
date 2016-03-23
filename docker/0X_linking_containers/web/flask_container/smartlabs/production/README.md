# Environment variables
* In the production server set an environment variable named SMARTLABS_SETTINGS by default it looks at app directory
the environment variables PG_PORT_5432_TCP_ADDR and PG_PORT_5432_TCP_PORT are created when you link containers. If
the environment variables are not set, the ones from default_settings.py are used
export SMARTLABS_SETTINGS=production_settings.py

# For testing you can create the production environment variables
export PG_PORT_5432_TCP_PORT=5432
export PG_PORT_5432_TCP_ADDR=172.17.0.2
export SMARTLABS_SETTINGS=production_settings.py