# Reticulum Beginner Guide

A simple 4-step guide to get your LoRa board running with Reticulum, Meshchat, and Nomadnet.

---

## Prerequisites

Install Reticulum and add yourself to the dialout group:

```bash
pip install rns rnodeconf
sudo usermod -a -G dialout $USER
```

**Log out and back in** for group changes to take effect.

---

## Step 1: Flash Your LoRa Board

**Goal:** Get RNode firmware on your Heltec board.

### 1. Plug in your board and find the port

```bash
ls /dev/ttyUSB* /dev/ttyACM*
```

- Heltec V2/V3: `/dev/ttyUSB0`
- Heltec V4: `/dev/ttyACM0`

### 2. Flash the firmware

```bash
rnodeconf /dev/ttyUSB0 --autoinstall
```

When prompted:
- Select your board type (7 = Heltec V2, 9 = Heltec V4)
- Select your region (2 = 915 MHz North America, 1 = 868 MHz Europe)
- Confirm with `y`

### 3. Verify it worked

```bash
rnodeconf /dev/ttyUSB0 --info
```

You should see your device info with firmware version.

**Done!** Your board now has RNode firmware.

---

## Step 2: Configure and Run Reticulum

**Goal:** Get your LoRa node talking to the Reticulum network.

### 1. Generate default config

```bash
rnsd --exampleconfig > ~/.reticulum/config
```

### 2. Add your LoRa interface

Edit `~/.reticulum/config` and add this to the `[interfaces]` section:

```ini
[[LoRa]]
  type = RNodeInterface
  interface_enabled = True
  port = /dev/ttyUSB0
  frequency = 915000000
  txpower = 14
  bandwidth = 125000
  spreadingfactor = 8
  codingrate = 5
```

### 3. Start Reticulum

```bash
rnsd -v
```

### 4. Check status (in another terminal)

```bash
rnstatus
```

You should see your LoRa interface showing "Up".

**Done!** Your node is now running on the Reticulum network.

---

## Step 3: Set Up Meshchat

**Goal:** Send encrypted messages over LoRa using a web interface.

### 1. Install Meshchat

```bash
git clone https://github.com/liamcottle/reticulum-meshchat
cd reticulum-meshchat
npm install --omit=dev
npm run build-frontend
pip install -r requirements.txt
```

### 2. Start Meshchat

```bash
python meshchat.py
```

### 3. Open the web interface

Go to `http://localhost:8000` in your browser.

### 4. Create your identity and start chatting

- Click "Create Identity"
- Wait for peers to announce (may take a few minutes over LoRa)
- Click on a peer to start a conversation

**Tips:**
- Keep messages short for LoRa (slow bandwidth)
- Peers must be in radio range or connected via TCP

**Done!** You can now send encrypted messages over mesh.

---

## Step 4: Set Up Nomadnet

**Goal:** Run a terminal-based node that can host pages.

### 1. Install Nomadnet

```bash
pip install nomadnet
```

### 2. Run Nomadnet

```bash
nomadnet
```

This launches the terminal UI. Use arrow keys to navigate, `Ctrl+Q` to quit.

### 3. Host a page (optional)

Create `~/.nomadnetwork/storage/pages/index.mu`:

```
#!c=0

`c`!Welcome to My Node`!

This page is served over Reticulum.

> About
I'm running a LoRa mesh node!
```

Restart Nomadnet to serve your page. Other Nomadnet users can browse to your node to view it.

**Done!** You now have a terminal-based mesh communication tool.

---

## Troubleshooting

### Device not found

```bash
# Check if board is plugged in
lsusb | grep -iE "silicon|espressif|ch34"

# Check serial ports
ls /dev/ttyUSB* /dev/ttyACM*
```

### Permission denied on serial port

```bash
# Add yourself to dialout group
sudo usermod -a -G dialout $USER
# Log out and back in
```

### Interface not starting

1. Make sure no other program is using the port (Arduino IDE, etc.)
2. Check your config syntax: `cat ~/.reticulum/config`
3. Try unplugging and replugging the board
4. Restart rnsd: `pkill rnsd && rnsd -v`

### Can't see other peers

- LoRa peers must be in radio range (2-10 km typical)
- Wait for announces (can take several minutes)
- Make sure both nodes use the same frequency, bandwidth, and spreading factor

### Heltec V4 specific issues

- Use the port labeled "USB", not "UART"
- Port is `/dev/ttyACM0` (not ttyUSB0)
- If stuck, hold BOOT while pressing RESET to enter bootloader mode

---

## Quick Commands

| Task | Command |
|------|---------|
| Start Reticulum | `rnsd -v` |
| Check status | `rnstatus` |
| Stop Reticulum | `pkill rnsd` |
| Device info | `rnodeconf /dev/ttyUSB0 --info` |
| Flash firmware | `rnodeconf /dev/ttyUSB0 --autoinstall` |
| Start Meshchat | `python meshchat.py` |
| Start Nomadnet | `nomadnet` |

---

## Files in This Repo

| File | Purpose |
|------|---------|
| `test_node.py` | Run `python test_node.py` to verify your setup |
| `reticulum-config-lora-enabled.ini` | Example config with LoRa enabled |
| `reticulum-config-original.ini` | Backup of default config |

---

## Resources

- [Reticulum Manual](https://markqvist.github.io/Reticulum/manual/)
- [Reticulum GitHub](https://github.com/markqvist/Reticulum)
- [Meshchat GitHub](https://github.com/liamcottle/reticulum-meshchat)
- [Nomadnet GitHub](https://github.com/markqvist/NomadNet)
- [Sideband (Mobile App)](https://github.com/markqvist/Sideband)
- [Reticulum Network Map](https://rmap.world/)
- [Reticulum IP Backbones](https://directory.rns.recipes/)

## Need More Range?
https://lilygo.cc/en-us/products/t-beam?variant=51708943335605  
https://www.etsy.com/listing/1865975766/gizont-915mhz-40cm-whip-antenna-with  
https://github.com/meshtastic/antenna-reports/  
