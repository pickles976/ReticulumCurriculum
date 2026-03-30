# Flashing

### Heltec V4

```
esptool --chip esp32s3 --port /dev/ttyACM0 --baud 921600 write-flash 0x0 ./heltec_v4_repeater-v1.14.1-467959c-merged.bin
```