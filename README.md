
# Pradise bot Auto Fishing Tool

A selfbot designed to automate fishing in a specific game channel for Pradise Bot : [Click me](top.gg/bot/1272208314163396650)

---

## Features

- **Automatic fishing:** Automatically clicks the "Cast line" button on fishing message
- **Fishing stats display:** Shows your current streak, earnings, level, and XP progress in a formatted console table with progress bars.
- **Captcha detection & alert:** Detects captcha/security verification prompts and uses text-to-speech to notify you.
- **Settings management:** Loads token, channel ID, and captcha alert toggle from a `settings.json` file
- **Discord presence:** Sets a custom "Fishing 🎣" status on login

---

## Setup

1. Clone/download this repo.
2. Edit a `settings.json` file in the same directory with the following structure:

```json
{
  "TOKEN": "your_discord_token_here",
  "CHANNEL_ID": "your_target_channel_id",
  "captcha_alerts": true
}
```

- Replace `"your_discord_token_here"` with your Discord user token.
- Replace `"your_target_channel_id"` with the ID of the Discord channel where fishing messages appear.
- Set `"captcha_alerts"` to `true` or `false` to enable or disable captcha voice alerts.

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python main.py
```

- Then run /fish on your discord channel

---

## Important Notes

- This is a **selfbot** (runs on your user account) which **violates Discord's Terms of Service**. Use at your own risk.
- It also violates Paradise Bot's Terms of Service at [Here](https://github.com/Daniel-191/Paradise/blob/main/TOS.md). Use at your own risk.
- Do **not** share your Discord token with anyone.
- Make sure your token and channel ID are correct in the `settings.json` file.
- Run this script responsibly and avoid spamming Discord.

---

## Dependencies

- `discord.py`
- `aiohttp`
- `rich`
- `pyttsx3`

---

## License

Feel free to edit, improve, or expand upon this code to fit your specific needs. Contributions and feedback are welcome—help make this project even better!
