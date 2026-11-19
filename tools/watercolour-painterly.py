import cv2, numpy as np
from wc2 import noise
PAPER=np.array([238,244,247],np.float32)
def paint4(path,out,seed,crop,cx=0.5):
    im=cv2.imread(path); h,w=im.shape[:2]
    tw=w; th=int(w*5/4)
    if th>h: th=h; tw=int(h*4/5)
    y0=int((h-th)*crop); x0=int((w-tw)*cx)
    im=im[y0:y0+th,x0:x0+tw]
    W,H=880,1100
    src=cv2.resize(im,(W,H),interpolation=cv2.INTER_AREA)
    # 1. loose colour washes: strong simplification at low resolution
    sm=cv2.resize(src,(528,660),interpolation=cv2.INTER_AREA)
    ms=cv2.pyrMeanShiftFiltering(sm,sp=6,sr=22,maxLevel=1)
    ms=cv2.xphoto.oilPainting(ms,2,1)
    base=cv2.resize(ms,(W,H),interpolation=cv2.INTER_CUBIC)
    base=cv2.GaussianBlur(base,(0,0),1.0)
    f=base.astype(np.float32)
    # 2. a little structure back, but painterly (not photographic)
    g=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp=g-cv2.GaussianBlur(g,(0,0),3.0)
    f+=hp[...,None]*0.6
    # 3. rich, saturated pigment with deeper shadows
    hsv=cv2.cvtColor(np.clip(f,0,255).astype(np.uint8),cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[...,1]=np.clip(hsv[...,1]*1.10,0,255)
    v=hsv[...,2]/255.; v=np.clip(v*0.92+0.10,0,1)
    hsv[...,2]=v*255
    f=cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR).astype(np.float32)
    f[...,2]*=1.03; f[...,0]*=0.96
    # 4. wet-in-wet blooms and blotchy brush marks
    b1=noise(H,W,90,seed)-.5; b2=noise(H,W,28,seed+1)-.5; b3=noise(H,W,9,seed+2)-.5
    f*=(1+0.10*b1+0.08*b2+0.035*b3)[...,None]
    # 5. wet edges: pigment collects where washes meet
    gm=cv2.cvtColor(base,cv2.COLOR_BGR2GRAY).astype(np.float32)
    grad=cv2.morphologyEx(gm,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))
    edge=np.clip(cv2.GaussianBlur(grad,(0,0),1.3)/30,0,1)
    f*=(1-0.16*edge)[...,None]
    # 6. granulation in the darker pigment
    lum=cv2.cvtColor(np.clip(f,0,255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255.
    gr=(np.random.default_rng(seed+3).random((H,W)).astype(np.float32)-.5)
    gr=cv2.GaussianBlur(gr,(0,0),0.8)
    f*=(1+gr*0.10*(1-lum))[...,None]
    # 7. loose ink drawing
    e=cv2.Canny(cv2.GaussianBlur(g.astype(np.uint8),(0,0),1.2),45,110).astype(np.float32)/255.
    e=cv2.GaussianBlur(e,(0,0),0.6)*0.30*(noise(H,W,20,seed+4)>0.3)
    ink=np.array([30,38,45],np.float32)
    f=f*(1-e[...,None])+ink*e[...,None]
    # 8. white paper left in the highlights
    lum=cv2.cvtColor(np.clip(f,0,255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255.
    hi=np.clip((lum-0.80)/0.10,0,1)[...,None]*0.75
    f=f*(1-hi)+PAPER*hi
    f=np.clip(f,0,255).astype(np.uint8)
    # 9. painted, blotchy border (like a brushed watercolour sheet)
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    d=np.minimum(np.minimum(xx,W-1-xx)/W,np.minimum(yy,H-1-yy)/H)
    rag=noise(H,W,140,seed+5)*0.05+noise(H,W,26,seed+6)*0.03+noise(H,W,6,seed+7)*0.012
    a=np.clip((d-0.01-rag)/0.006,0,1)
    a=cv2.GaussianBlur(a,(0,0),0.8)
    rgba=cv2.cvtColor(f,cv2.COLOR_BGR2BGRA); rgba[...,3]=(a*255).astype(np.uint8)
    cv2.imwrite(out,rgba)
