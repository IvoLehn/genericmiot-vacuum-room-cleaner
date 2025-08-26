from homeassistant.core import HomeAssistant
from homeassistant.helpers.discovery import async_load_platform
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    if DOMAIN not in config:
        return True

    hass.data[DOMAIN] = config[DOMAIN]
    await async_load_platform(hass, "button", DOMAIN, {}, config)
    return True
