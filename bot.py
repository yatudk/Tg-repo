from telethon import TelegramClient, events

api_id = 20891012
api_hash = "caee5c1abea8434a31589d2e2ee31e88"
bot_token = "8270208242:AAFCkSjypbIgQp0FHqVIqv3mbP0elvCDVDw"

client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats="@proudpoojary05"))
async def handler(event):
    if event.fwd_from:
        await event.delete()

print("Bot started...")
client.run_until_disconnected()
