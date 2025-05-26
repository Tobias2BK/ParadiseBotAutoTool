import discord
from discord.ext import commands
import os
import json
import re
import aiohttp
import asyncio
import random
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.box import ROUNDED
import pyttsx3

# ===================== GLOBAL INIT =====================
engine = pyttsx3.init()
bot = commands.Bot(command_prefix="!", self_bot=True)
console = Console()
session = None
settings_file = "settings.json"

# ===================== SETTINGS =====================
def load_settings():
    if not os.path.exists(settings_file):
        with open(settings_file, "w") as f:
            json.dump({"captcha_alerts": True, "TOKEN": "","CHANNEL_ID": ''}, f)
    with open(settings_file, "r") as f:
        return json.load(f)
    
settings = load_settings()
_token = settings.get("TOKEN")
_channel_id = int(settings.get("CHANNEL_ID"))
_captcha = settings.get("captcha_alerts",True)
if _token == "your_discord_token_here":
    print("Please put your token in .json file")
    input()
    os._exit()
if _channel_id == 'your_target_channel_id':
    print("Please put your channel id in .json file")
    input()
    os._exit()

# ===================== UTILITY FUNCS =====================
def log(msg: str) -> None:
    console.print(f"[bold green][{datetime.now().strftime('%H:%M:%S')}][/bold green] {msg}")

def human_format(num: float) -> str:
    units = ['', 'K', 'M', 'B', 'T']
    for unit in units:
        if abs(num) < 1000:
            formatted = f"{num:.1f}"
            return f"{formatted.rstrip('.0')}{unit}"
        num /= 1000
    return f"{num:.1f}P"

def print_stats(streak: int, earnings: float, level: int, xp: tuple[int, int]) -> None:
    os.system('cls')
    console.rule("[bold blue]> Fishing Stats [/bold blue]", style="grey37")
    progress_ratio = min(xp[0]/xp[1], 1.0)
    filled = round(20 * progress_ratio)
    bar = "█" * filled + "░" * (20 - filled)
    table = Table(box=ROUNDED, show_header=False, padding=(0, 2))
    table.add_row("🔥 Streak", f"{streak}")
    table.add_row("💰 Earnings", f"${human_format(earnings)}")
    table.add_row("⭐ Level", f"{level}")
    table.add_row("✨ XP", f"[{bar}] {xp[0]}/{xp[1]}")
    console.print(table)
    console.rule("", style="grey23")

# ===================== EVENTS =====================
@bot.event
async def on_ready():
    global session
    await bot.wait_until_ready()
    session = aiohttp.ClientSession()  # now created inside event loop
    os.system('cls')
    log(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Fishing 🎣"))

@bot.event
async def on_raw_message_edit(payload: discord.RawMessageUpdateEvent) -> None:
    if payload.channel_id != _channel_id:
        return
    channel = bot.get_channel(payload.channel_id)
    if not channel or not (message := await channel.fetch_message(payload.message_id)):
        return
    if message.author.id != 1272208314163396650 or not message.embeds:
        return

    embed = message.embeds[0]
    title = embed.title or ""

    if not re.match(r'^.+\*\*Fishing at ', title):
        return

    if components := message.components:
        for btn in (b for row in components for b in row.children):
            if btn.label.lower() == "cast line":
                await session.post(
                    "https://discord.com/api/v9/interactions",
                    json={
                        "type": 3,
                        "nonce": str(random.randint(10**18, 10**19)),
                        "guild_id": str(message.guild.id),
                        "channel_id": str(channel.id),
                        "message_id": str(message.id),
                        "application_id": "1272208314163396650",
                        "session_id": bot._connection.session_id,
                        "data": {"component_type": 2, "custom_id": btn.custom_id}
                    },
                    headers={"Authorization": _token}
                )
                break
    # parse stats
    if text := "\n".join(f.value for f in embed.fields if f.value):
        streak_match = re.search(r"Streak:\s*\*\*(\d+)", text)
        earnings_match = re.search(r"Earnings:\s*\*\*\$([\d,.]+(?:\.\d+)?)([KMBT]?)", text)
        level_match = re.search(r"Level:\s*\*\*(\d+)", text)
        xp_match = re.search(r"XP:.*\*\*(\d+)/(\d+)", text)

        if streak_match and earnings_match and level_match and xp_match:
            streak = int(streak_match.group(1))

            earnings_str = earnings_match.group(1).replace(",", "")
            unit = earnings_match.group(2).upper()
            earnings = float(earnings_str)
            multiplier = {"":1, "K":1_000, "M":1_000_000, "B":1_000_000_000, "T":1_000_000_000_000}
            earnings *= multiplier.get(unit, 1)

            level = int(level_match.group(1))
            xp = (int(xp_match.group(1)), int(xp_match.group(2)))

            print_stats(streak, earnings, level, xp)
    await asyncio.sleep(random.uniform(2.5, 4.5))  

@bot.event
async def on_message(message: discord.Message):
    if (
        message.channel.id != _channel_id or
        message.author.id != 1272208314163396650 or
        not message.embeds
    ):
        return

    embed = message.embeds[0]

    if embed.title == "🔒 Security Verification Required":
        log("[bold red][CAPTCHA DETECTED][/bold red]")
        if _captcha:
            engine.say("Captcha detected. Attention required.")
            engine.runAndWait()

    elif "Verification successful! Continue fishing!" in embed.description:
        if _captcha:
            log("[bold yellow][CAPTCHA SOLVED] Press 'Cast line' again to start[/bold yellow]")
            engine.say("Captcha solved. Press 'Cast line' again to start.")
            engine.runAndWait()

# ===================== RUN BOT =====================
try:
    bot.run(_token)
finally:
    if session:
        asyncio.get_event_loop().run_until_complete(session.close())
