import asyncio, os
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
html="""<html><body style="margin:0;background:#fff;font-family:Inter,sans-serif">
<div style="width:1200px">
%s
<div style="display:flex;align-items:center;gap:40px;padding:24px 40px;border-top:1px solid #ddd">
<img src="mark_A_only.svg" width="128"><img src="mark_A_only.svg" width="48"><img src="mark_A_only.svg" width="32"><img src="mark_A_only.svg" width="16">
<span style="font-size:14px;color:#666">mark A at 128, 48, 32 and 16 px</span></div>
<img src="logo_A_sequence_dark.svg" width="1200"></div></body></html>"""
imgs="".join(f'<div style="border-top:1px solid #ddd;position:relative"><span style="position:absolute;left:40px;top:14px;font-size:20px;color:#888">{k}</span><img src="{f}" width="1200"></div>' for k,f in [("A",'logo_A_sequence.svg'),("B",'logo_B_serif.svg'),("C",'logo_C_monogram.svg')])
open(D+"/sheet.html","w").write(html%imgs)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1200,'height':800})
        await pg.goto("file://"+D+"/sheet.html"); await pg.wait_for_timeout(500)
        await pg.screenshot(path=D+"/sheet.png",full_page=True); await b.close()
asyncio.run(main())
