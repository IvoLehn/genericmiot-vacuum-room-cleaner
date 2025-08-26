from homeassistant.components.button import ButtonEntity
from .const import DOMAIN, CONF_ROOMS, CONF_NAME, CONF_ID, CONF_IP, CONF_TOKEN
from miio import GenericMiot

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    integration_config = hass.data[DOMAIN]
    ip = integration_config.get(CONF_IP)
    token = integration_config.get(CONF_TOKEN)
    rooms = integration_config.get(CONF_ROOMS, [])

    buttons = [
        RoomCleanButton(room[CONF_NAME], room[CONF_ID], ip, token)
        for room in rooms
    ]
    async_add_entities(buttons)

class RoomCleanButton(ButtonEntity):
    def __init__(self, name, room_id, ip, token):
        self._attr_name = f"Clean {name}"
        self._attr_unique_id = f"clean_button_{room_id}"
        self._room_id = room_id
        self._ip = ip
        self._token = token

    async def async_press(self) -> None:
        await self.clean_room()

    async def clean_room(self) -> None:
        print(f"Sending vacuum {self._ip} to room {self._room_id}")
        cleaner = GenericMiot(ip=self._ip, token=self._token)
        siid = 2
        aiid = 16
        piid = 15
        params = [{"piid": piid, "value": f"[{self._room_id}]"}]
        cleaner.call_action_by(siid, aiid, params)
        
        
