# 🎣 Paradise Bot Auto Fishing Tool (Selfbot Edition)

A Discord selfbot script that automatically plays the fishing minigame for [Paradise Bot](https://top.gg/bot/1272208314163396650) with human-like interaction. It includes fishing automation, stat tracking, anti-captcha voice alerts, and intelligent random behavior to avoid detection.

---

## 📢 Announcement

- **5/26/2025** – This project was discontinued after I got banned from the bot... 💀
- **5/27/2025** – SIKE! I’m back with a full update featuring “**Absolute Human Mimic**” mode for ultra-stealth fishing. See features below!

---

## ⚙️ Features

- 🎣 **Auto Fishing:** Instantly clicks the “Cast Line” button when a fishing embed appears.
- 📊 **Fishing Stats:** Displays streak, earnings, level, and XP with fancy progress bars in the terminal.
- 🧠 **Human Simulation:** Delays, hesitations, random commands, and AFK behavior to mimic real users.
- 🔐 **Captcha Detection:** Alerts you with TTS when a captcha/security check appears.
- 🔧 **Customizable Settings:** All your info (token, channel ID, alert toggle) in a simple `settings.json`.

---

## 🚀 Setup

1. **Clone or download this repo.**
2. **Create a `settings.json` file** in the root directory with this format:

```json
{
  "TOKEN": "your_discord_token_here",
  "CHANNEL_ID": "your_target_channel_id",
  "captcha_alerts": true
}
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🕹️ Usage

```bash
python main.py
```

Once started, run `/fish` in your target Discord channel.

---

## ⚠️ Warnings

> ❗ This is a **selfbot** and violates Discord's [Terms of Service](https://discord.com/terms).  
> ❗ It also violates Paradise Bot’s [TOS](https://github.com/Daniel-191/Paradise/blob/main/TOS.md).  
> ❗ Use responsibly, and at your own risk!

---

## 📦 Dependencies

- `discord.py-self`
- `aiohttp`
- `rich`
- `pyttsx3`
- `requests`

---

## 📝 License

Go wild — edit, fork, remix, or contribute! Just don’t sell it or get anyone banned (including yourself 😉).
