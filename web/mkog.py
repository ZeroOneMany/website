import sys
sys.path.insert(0,'../logo')
import importlib.util, os
spec=importlib.util.spec_from_file_location('ml','../logo/make_logos.py')
ml=importlib.util.module_from_spec(spec); spec.loader.exec_module(ml)
t=190; gap=50
word_w=max(ml.text_path("inter_semi",w,58*t/200,0,0,tracking=0.12)[1] for w in ["ZERO","ONE","MANY"])
block=t+gap+word_w
bx=(1200-block)/2; by=(630-t)/2
body=ml.tile(bx,by,t,ink=ml.PAPER,fg=ml.INK,text_col=ml.INK)+ml.stacked(bx+t+gap,by,t,ml.PAPER)
open('og.svg','w').write(ml.svg(1200,630,body,bg=ml.INK))
