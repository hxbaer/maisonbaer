import cv2, numpy as np, sys
PAPER=np.array([216,228,235],np.float32)
def noise(h,w,scale,seed):
    r=np.random.default_rng(seed)
    n=r.random((h//scale+2,w//scale+2)).astype(np.float32)
    n=cv2.resize(n,(w,h),interpolation=cv2.INTER_CUBIC)
    return cv2.GaussianBlur(n,(0,0),max(scale/3,0.6))
def paint(path,out,seed,crop):
    im=cv2.imread(path); h,w=im.shape[:2]
    tw=w; th=int(w*5/4)
    if th>h: th=h; tw=int(h*4/5)
    y0=int((h-th)*crop); x0=(w-tw)//2
    im=im[y0:y0+th,x0:x0+tw]
    W,H=880,1100
    small=cv2.resize(im,(704,880),interpolation=cv2.INTER_AREA)
    # simplify into colour washes (hand-painted look)
    ms=cv2.pyrMeanShiftFiltering(small,sp=5,sr=16,maxLevel=1)
    ms=cv2.edgePreservingFilter(ms,flags=1,sigma_s=12,sigma_r=0.18)
    base=cv2.resize(ms,(W,H),interpolation=cv2.INTER_CUBIC)
    base=cv2.bilateralFilter(base,5,20,5)
    full=cv2.resize(im,(W,H),interpolation=cv2.INTER_AREA).astype(np.float32)
    # bring back the fine structure of the photo (windows, leaves, stonework)
    hp=cv2.cvtColor(full.astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)-cv2.GaussianBlur(cv2.cvtColor(full.astype(np.uint8),cv2.COLOR_BGR2GRAY),(0,0),2.2).astype(np.float32)
    base=np.clip(base.astype(np.float32)+hp[...,None]*0.75,0,255).astype(np.uint8)
    # colour: clear, warm, slightly lifted like watercolour on white paper
    hsv=cv2.cvtColor(base,cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[...,1]=np.clip(hsv[...,1]*0.84,0,255)
    hsv[...,2]=hsv[...,2]*0.86+255*0.13
    f=cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR).astype(np.float32)
    f[...,2]*=1.03; f[...,1]*=1.0; f[...,0]*=0.94
    # wash variation: soft low-frequency only (pigment unevenness), no grain
    g=noise(H,W,60,seed)-.5; g2=noise(H,W,16,seed+1)-.5
    f=f*(1+0.05*g[...,None]+0.03*g2[...,None])
    # pigment pooling at the edges of colour areas
    gray_ms=cv2.cvtColor(base,cv2.COLOR_BGR2GRAY).astype(np.float32)
    grad=cv2.morphologyEx(gray_ms,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))
    pool=np.clip(cv2.GaussianBlur(grad,(0,0),1.0)/45,0,1)*0.12
    f=f*(1-pool[...,None])
    # fine pencil/ink drawing, sparse
    gray=cv2.cvtColor(cv2.resize(im,(W,H),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY)
    e=cv2.Canny(cv2.GaussianBlur(gray,(0,0),1.1),45,110).astype(np.float32)/255.
    e=cv2.GaussianBlur(e,(0,0),0.55)*0.30
    ink=np.array([45,60,70],np.float32)
    f=f*(1-e[...,None])+ink*e[...,None]
    # paper shows through in the lightest areas
    lum=cv2.cvtColor(np.clip(f,0,255).astype(np.uint8),cv2.COLOR_BGR2GRAY).astype(np.float32)/255.
    hi=np.clip((lum-0.82)/0.12,0,1)[...,None]*0.6
    f=f*(1-hi)+np.array([238,244,247],np.float32)*hi
    f=np.clip(f,0,255).astype(np.uint8)
    # crisp deckled edge: near-rectangular, dry-brush irregular border
    yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
    d=np.minimum(np.minimum(xx,W-1-xx)/W,np.minimum(yy,H-1-yy)/H)
    rag=noise(H,W,120,seed+2)*0.035+noise(H,W,10,seed+3)*0.016+noise(H,W,3,seed+4)*0.006
    a=np.clip((d-0.012-rag)/0.004,0,1)
    a=cv2.GaussianBlur(a,(0,0),0.7)
    # dry-brush: lighter, broken paint just inside the border
    rim=np.clip(1-(d-0.012-rag)/0.03,0,1)*(noise(H,W,4,seed+5)>0.55)
    f=(f.astype(np.float32)*(1-0.45*rim[...,None])+np.array([238,244,247],np.float32)*0.45*rim[...,None]).astype(np.uint8)
    rgba=cv2.cvtColor(f,cv2.COLOR_BGR2BGRA); rgba[...,3]=(a*255).astype(np.uint8)
    cv2.imwrite(out,rgba)
srcs=sys.argv[1:]
for i,p in enumerate(srcs):
    paint(p,f"/home/claude/seven/img/zh-{i+1}.png",11+i*5,[0.62,0.55,0.25,0.62][i])
print("ok")
