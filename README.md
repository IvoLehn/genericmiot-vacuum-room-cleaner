# GenericMiot Vacuum Room Cleaner

Home Assistant integration for Xiaomi GenericMiot vacuum devices. This integration enables room specific cleaning.

**!!! This integration is not fully tested and relies on the python-miio package in beta version 0.6.0.dev0 !!!**

(only testet for Xiaomi Vacuum x20 max)

Specify vacuum ip and token in configuration.yaml like:

```yaml
genericmiot-vacuum-room-cleaner:
  ip: 192.168.1.50
  token: abc123securetoken
```

Install from config directory via:

```bash
git clone https://github.com/IvoLehn/genericmiot-vacuum-room-cleaner.git
cd genericmiot-vacuum-room-cleaner
./install.sh
cd ..
rm -rf genericmiot-vacuum-room-cleaner
```