import requests, yamlsettings
import libtado.api as api

config_file = "config.yml"
cfg = yamlsettings.load(config_file)

headers = {
    "Authorization": "Bearer %s" % cfg.lifx.token,
}

def turnOffAllLights():
    print("Turn off all lights...")
    payload = {
        "power": "off",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state',
                            data=payload, headers=headers)

if __name__ == '__main__':
    t = api.Tado(cfg.tado.username, cfg.tado.password, cfg.tado.secret)

    isAtHome = False

    for device in t.get_mobile_devices():
        if device['location']['atHome']:
            isAtHome = True

    if not isAtHome:
        print("Nobody's home.")
        turnOffAllLights()
