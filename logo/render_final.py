import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
jobs=[("logo_C_monogram.svg",1200,400,2,"logo_C_monogram.png"),("avatar_square.svg",800,800,1,"avatar_square.png"),
("banner_linkedin.svg",1584,396,1,"banner_linkedin.png"),("favicon.svg",64,64,1,"favicon_64.png"),("favicon.svg",32,32,1,"favicon_32.png")]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for f,w,h,s,out in jobs:
            ctx=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=s)
            pg=await ctx.new_page()
            await pg.set_content(f'<body style="margin:0"><img src="file://{D}/{f}" width="{w}" height="{h}" style="display:block"></body>')
            await pg.goto("file://"+D+"/"+f)
            await pg.screenshot(path=D+"/"+out)
            await ctx.close()
        await b.close()
asyncio.run(main())
