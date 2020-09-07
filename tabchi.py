from pyrogram import Filters, Client
import pyrogram

appid = 1311366
apphash = "55413c0f83d2d0553d059bc33b47ca71"

app = Client("test", api_id=appid, api_hash=apphash)

@app.on_message(Filters.group & Filters.command("ping", prefixes=""))
def ping(c,m):
    m.reply_text("**Pong**")

botlists = []
@app.on_message(Filters.group & Filters.command("add", prefixes=""))
def adder(c,m):
    try:
        botlists.append(m.command[1])
        print(f"\033[93mAdded \033[92m{m.command[1]}")
        if m.command[1] in botlists:
            app.send_message(m.chat.id, f"**|{m.command[1]}| in Bot List!\nBut i Can Invite him/her\nBots:\n"+"\n".join(botlists)+"**")
            botlists.remove(m.command[1])
        elif m.command[1] not in botlists:
            app.send_message(m.chat.id, f"**|{m.command[1]}| Added To Bot Lists!\nBots:\n"+"\n".join(botlists)+"**")
    except:
        app.send_message(m.chat.id, "**Error!**")

@app.on_message(Filters.group & Filters.command("invite",prefixes=""))
def invite(c,m):
    s = app.send_message(m.chat.id, "**Start Adding Bots...**")
    print(f"\033[1;32;40mStart Adding Bots To Group: \033[1;33;40m|{m.chat.title}|")
    app.add_chat_members(m.chat.id, botlists)
    app.delete_messages(s.chat.id, s.message_id)

@app.on_message(Filters.group & Filters.command("list",prefixes=""))
def lists(c,m):
    if botlists == []:
        app.send_message(m.chat.id, "**List Is Empty!**")
    else:
        app.send_message(m.chat.id, "**Bots:\n"+"\n".join(botlists)+"**")

@app.on_message(Filters.group & Filters.command("clear",prefixes=""))
def clears(c,m):
    botlists.clear()
    app.send_message(m.chat.id, "**Bot List Successfuly Cleared!**")



app.run()
