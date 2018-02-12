from netatmo_client.client import NetatmoClient
import config as cfg

scopes = ('read_station', 'read_thermostat', 'write_thermostat', 'read_camera')

client = NetatmoClient(cfg.credentials[client_id], cfg.credentials[client_secret])

client.request_token_with_client_credentials(cfg.credentials.[username], cfg.credentials[password], *scopes)

# currently just receiving the JSON, not doing anything with it
var result = client.public.get_station_data(cfg.region[lat_ne], cfg.region[lon_ne], cfg.region[lat_sw], cfg.region[lon_sw])
print json.dumps(result)