#MADE BY "AMAN PANDEY"
#FIXED BY @MADBOY482
#MODIFIED BY @GODBOYX
import asyncio
import os
import random
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Extre.utils import extremepro_cmd, edit_or_reply, amanpandey_cmd
from Extre import ALIVE_NAME, CMD_HELP


# Google Drive ()
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
    
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Extre USER"

CARBONLANG = "auto"
LANG = "en"

@client.on(extremepro_cmd(outgoing=True, pattern="carbon(?: |$)(.*)"))
@client.on(amanpandey_cmd(pattern="carbon(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("`Processing..`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)  # Converting to urlencoded
    godboy = await edit_or_reply(e, "`Carbonizing...\n25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by godboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await godboy.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await godboy.edit("`Processing..\n75%`")
    # Waiting for downloading
    await asyncio.sleep(2)
    await godboy.edit("`Done Dana Done...\n100%`")
    file = "./carbon.png"
    await godboy.edit("`Uploading..`")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption="Here we go with ur Karbon.\nCarbonised by Extre USERBOT",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()
    # Removing carbon.png after uploading
    await godboy.delete()


@client.on(extremepro_cmd(outgoing=True, pattern="krb"))
@client.on(amanpandey_cmd(pattern="krb", allow_sudo=True))
async def carbon_api(e):
    godboy = await edit_or_reply(e, "`Processing....`")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[5:]:
        pcodee = str(pcode[5:])
        if "|" in pcodee:
            pcode, skeme = pcodee.split("|")
        else:
            pcode = pcodee
            skeme = None
    elif textx:
        pcode = str(textx.message)
        skeme = None  # Importing message to module
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)  # Converting to urlencoded
    await godboy.edit("`Meking Carbon...`\n`25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await godboy.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]"
    ).click()
    if skeme is not None:
        k_skeme = driver.find_element_by_xpath(
            "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input"
        )
        k_skeme.send_keys(skeme)
        k_skeme.send_keys(Keys.DOWN)
        k_skeme.send_keys(Keys.ENTER)
    else:
        color_scheme = str(random.randint(1, 29))
        driver.find_element_by_id(("downshift-0-item-" + color_scheme)).click()
    driver.find_element_by_id("export-menu").click()
    driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await godboy.edit("`Processing..\n75%`")
    # Waiting for downloading
    await asyncio.sleep(2.5)
    color_name = driver.find_element_by_xpath(
        "/html/body/div[1]/main/div[3]/div[2]/div[1]/div[1]/div/span[2]/input"
    ).get_attribute("value")
    await godboy.edit("`Done Dana Done...\n100%`")
    file = "./carbon.png"
    await godboy.edit("`Uploading..`")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption="`Here's your carbon!` \n**Colour Scheme: **`{}`".format(color_name),
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()
    await godboy.delete()


@client.on(extremepro_cmd(pattern=f"kar1(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="kar1(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    godboy = await edit_or_reply(e, "🔲🔲🔲🔲🔲")
    CARBON = "https://carbon.now.sh/?bg=rgba(249%2C237%2C212%2C0)&t=synthwave-84&wt=none&l=application%2Fjson&ds=true&dsyoff=20px&dsblur=0px&wc=true&wa=true&pv=56px&ph=0px&ln=false&fl=1&fm=IBM%20Plex%20Mono&fs=14.5px&lh=153%25&si=false&es=4x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[6:]:
        pcode = str(pcode[6:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # MODIFIED BY @GODBOYX
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("🔳🔳🔲🔲🔲")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)
    await godboy.edit("🔳🔳🔳🔲🔲")
    await asyncio.sleep(2)
    await godboy.edit("🔳🔳🔳🔳🔳")
    file = "./carbon.png"
    await godboy.edit("☣️Karbon1 Completed, Uploading Karbon☣️")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await godboy.delete()  # Deleting msg


@client.on(extremepro_cmd(pattern=f"kar2(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="kar2(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    godboy = await edit_or_reply(e, "📛📛📛📛📛")
    CARBON = "https://carbon.now.sh/?bg=rgba(239%2C40%2C44%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[6:]:
        pcode = str(pcode[6:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # MODIFIED BY @GODBOYX
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("🔘🔘📛📛📛")
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)
    await godboy.edit("🔘🔘🔘📛📛")
    await asyncio.sleep(2)  # Waiting for downloading
    await godboy.edit("🔘🔘🔘🔘🔘")
    file = "./carbon.png"
    await godboy.edit("☣️Karbon2 Completed, Uploading Karbon☣️")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption=f"Here's your Karbon2",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await godboy.delete()  # Deleting msg


@client.on(extremepro_cmd(pattern=f"kar3(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="kar3(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    godboy = await edit_or_reply(e, "🎛🎛🎛🎛🎛")
    CARBON = "https://carbon.now.sh/?bg=rgba(74%2C144%2C226%2C1)&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[6:]:
        pcode = str(pcode[6:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # MODIFIED BY @GODBOYX
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("🔵🔵🎛🎛🎛")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)
    await godboy.edit("🔵🔵🔵🎛🎛")
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await asyncio.sleep(2)  # Waiting for downloading

    await godboy.edit("🔵🔵🔵🔵🔵")
    file = "./carbon.png"
    await godboy.edit("☣️Karbon3 Completed, Uploading Karbon⬆️")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption=f"Here's your Karbon3",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await godboy.delete()  # Deleting msg


@client.on(extremepro_cmd(pattern=f"kar4(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="kar4(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    godboy = await edit_or_reply(e, "🌚🌚🌚🌚🌚")
    CARBON = "https://carbon.now.sh/?bg=rgba(29%2C40%2C104%2C1)&t=one-light&wt=none&l=application%2Ftypescript&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[6:]:
        pcode = str(pcode[6:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by godboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("🌝🌝🌚🌚🌚")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)
    await godboy.edit("🌝🌝🌝🌚🌚")
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await asyncio.sleep(2)  # Waiting for downloading

    await godboy.edit("🌝🌝🌝🌝🌝")
    file = "./carbon.png"
    await godboy.edit("✅Karbon4 Completed, Uploading Karbon✅")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption=f"Here's your Karbon4 ",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )

    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await godboy.delete()  # Deleting msg


@client.on(extremepro_cmd(pattern=f"rgbk2(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="rgbk2(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    RED = random.randint(0, 256)
    GREEN = random.randint(0, 256)
    BLUE = random.randint(0, 256)
    OPC = random.random()
    godboy = await edit_or_reply(e, "⬜⬜⬜⬜⬜")
    CARBON = "https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C{O})&t=material&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[7:]:
        pcode = str(pcode[7:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, O=OPC, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("⬛⬛⬜⬜⬜")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)

    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)  # this might take a bit.
    # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # await asyncio.sleep(5)
    await godboy.edit("⬛⬛⬛⬜⬜")
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await asyncio.sleep(2)  # Waiting for downloading

    await godboy.edit("⬛⬛⬛⬛⬛")
    file = "./carbon.png"
    await godboy.edit("✅RGB Karbon 2.0 Completed, Uploading Karbon✅")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption=f"Here's your karbonrgb",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    # Removing carbon.png after uploading
    await godboy.delete()  # Deleting msg


@client.on(extremepro_cmd(pattern=f"kargb(?: |$)(.*)", outgoing=True))
@client.on(amanpandey_cmd(pattern="kargb(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    RED = random.randint(0, 256)
    GREEN = random.randint(0, 256)
    BLUE = random.randint(0, 256)
    THEME = [
        "3024-night",
        "a11y-dark",
        "blackboard",
        "base16-dark",
        "base16-light",
        "cobalt",
        "dracula",
        "duotone-dark",
        "hopscotch",
        "lucario",
        "material",
        "monokai",
        "night-owl",
        "nord",
        "oceanic-next",
        "one-light",
        "one-dark",
        "panda-syntax",
        "paraiso-dark",
        "seti",
        "shades-of-purple",
        "solarized",
        "solarized%20light",
        "synthwave-84",
        "twilight",
        "verminal",
        "vscode",
        "yeti",
        "zenburn",
    ]
    CUNTHE = random.randint(0, len(THEME) - 1)
    The = THEME[CUNTHE]
    godboy = await edit_or_reply(e, "⬜⬜⬜⬜⬜")
    CARBON = "https://carbon.now.sh/?bg=rgba({R}%2C{G}%2C{B}%2C1)&t={T}&wt=none&l=auto&ds=false&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Fira%20Code&fs=14px&lh=152%25&si=false&es=2x&wm=false&code={code}"
    CARBONLANG = "en"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[7:]:
        pcode = str(pcode[7:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    code = quote_plus(pcode)  # Converting to urlencoded
    url = CARBON.format(code=code, R=RED, G=GREEN, B=BLUE, T=The, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = CHROME_BIN
    # fixed by madboy482
    # SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    await godboy.edit("⬛⬛⬜⬜⬜")

    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await asyncio.sleep(2)  # this might take a bit.
    #  driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # await asyncio.sleep(5)
    await godboy.edit("⬛⬛⬛⬜⬜")
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await asyncio.sleep(2)  # Waiting for downloading
    await godboy.edit("⬛⬛⬛⬛⬛")
    file = "./carbon.png"
    await godboy.edit("✅RGB Karbon Completed, Uploading Karbon✅")
    await e.Andencento.send_file(
        e.chat_id,
        file,
        caption=f"Here's your karbonrgb",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    await godboy.delete()  # Deleting msg


CMD_HELP.update(
    {
        "carbon": "**Plugin : **`carbon`\
    \n\n**Commands are :** \
    \n  •  `.carbon <reply to code>`\
    \n  •  `.krb <reply to code>`\
    \n  •  `.kar1 <reply to code>`\
    \n  •  `.kar2 <reply to code>`\
    \n  •  `.kar3 <reply to code>`\
    \n  •  `.kar4 <reply to code>`\
    \n  •  `.rgbk2 <reply to code>`\
    \n  •  `.kargb <reply to code>`\
    \n\n**Function : **\
    \n__Carbon generators, each command has one style of carbon (krb, & kargb shows random carbons, remaining all are fixed)__\
    "
    }
)


# fixed by madboy482  
# MODIFIED BY @GODBOYX
# fixed by madboy482

# SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI
# SAY NO TO KANGS, ELSE GEND FAD DI JAYEGI

# chalo ab acche bache ki trah pura plugin copy kro with credits
# ek bhi credit mat htana

# Extre
