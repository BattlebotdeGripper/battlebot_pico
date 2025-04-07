# 🛠️ Project Battlebot - Raspberry Pi Pico 2

## 📄 Overzicht
Deze setup maakt het mogelijk om:
- Een servo aan te sturen.
- CAN-berichten van de **Raspberry Pi 5** te ontvangen via de **CAN-bus** op de **Raspberry Pi Pico 2**.

---

## 🔧 Benodigdheden

- Raspberry Pi 5  
- MCP2515 CAN-module  
- Raspberry Pi Pico 2  
- Jumper wires  
- Servo  
- Grijparm  
- Twee motorwielen en ESC

---

## 🔌 Hardware Aansluiten

### 🟡 CAN-bus Bedrading

#### 📥 Voor de MCP2515 module
Zie de instructies in deze repository:  
🔗 [https://github.com/Znooptokkie/mcp2515/](https://github.com/Znooptokkie/mcp2515/)

#### 📤 Voor de Raspberry Pi 5
Zie deze repository voor aansluitingen op de Pi 5:  
🔗 [https://github.com/BattlebotdeGripper/battlebot_pi/](https://github.com/BattlebotdeGripper/battlebot_pi/)

---

### 🦾 Motoren & Grijparm

| **Onderdeel**     | **GPIO op Pico 2** |
|-------------------|--------------------|
| Grijparm PWM      | GPIO 10            |
| Linker Wiel PWM   | GPIO 11            |
| Rechter Wiel PWM  | GPIO 12            |
| VCC (allen)       | 5V                 |
| GND (allen)       | GND                |
