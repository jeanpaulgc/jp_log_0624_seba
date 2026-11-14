import re, hashlib, os, glob, sys
REPO='/home/claude/jp_log_0624_seba'
SRC=f'{REPO}/app.bf0a90d6ac.js'
s=open(SRC,encoding='utf-8').read()
css=open('/home/claude/work/duo.css',encoding='utf-8').read()
assert '`' not in css and '${' not in css

def rep(old,new,count=1):
    global s
    n=s.count(old)
    assert n==count, (n, old[:90])
    s=s.replace(old,new)

# 1. CSS at the end of the main stylesheet
m=re.search(r'[,;]iy=`',s); a=m.end(); b=s.find('`',a)
s=s[:b]+css+s[b:]

# 2. layout hook
i=s.find('function fy(){'); j=s.find('function hy(',i); k=s.find('function py(',j)
assert 0<i<j<k
FY='''function fy(){let rd=(x,d)=>{try{let y=localStorage.getItem(x);return y==null?d:y}catch{return d}},wr=(x,y)=>{try{localStorage.setItem(x,y)}catch{}},[e,t]=(0,T.useState)(()=>{let x=rd("cr-layout","auto");return["auto","phone","wide","split"].includes(x)?x:"auto"}),[a,n]=(0,T.useState)(()=>{let x=rd("cr-pin","brief");return["brief","days","trends","plan"].includes(x)?x:"brief"}),[l,i]=(0,T.useState)(()=>rd("cr-lg","0")==="1"),[s,r]=(0,T.useState)(()=>window.innerWidth);(0,T.useEffect)(()=>{let f=()=>r(window.innerWidth),vv=window.visualViewport;window.addEventListener("resize",f);window.addEventListener("orientationchange",f);vv&&vv.addEventListener("resize",f);return()=>{window.removeEventListener("resize",f);window.removeEventListener("orientationchange",f);vv&&vv.removeEventListener("resize",f)}},[]);(0,T.useEffect)(()=>{wr("cr-layout",e)},[e]);(0,T.useEffect)(()=>{wr("cr-pin",a)},[a]);(0,T.useEffect)(()=>{wr("cr-lg",l?"1":"0")},[l]);let u=e==="phone"?"phone":e==="wide"?"wide":s<561?"phone":e==="split"?"split":s>=740?"split":"wide";return{pref:e,setPref:t,pin:a,setPin:n,lg:l,setLg:i,mode:u}}'''
HY='''function hy({L:e,tab:t,go:a}){let[n,l]=(0,T.useState)(!1),s=[["auto","Auto"],["phone","Phone"],["wide","Wide"],["split","2 pages"]],r={auto:"Phone layout when folded. Two pages side by side when open.",phone:"Always the phone layout.",wide:"One wide page with the cards in columns.",split:"Two pages side by side whenever the screen is wide enough."},u=f=>{let d=e.pin;e.setPin(f);f===t&&d!==f&&a(d)},ic={fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",viewBox:"0 0 24 24",width:"15",height:"15"};return(0,o.jsxs)(o.Fragment,{children:[e.mode==="split"&&t!==e.pin&&(0,o.jsx)("button",{className:"chip lz-chip",onClick:()=>u(t),"aria-label":"Pin this page to the left",children:(0,o.jsxs)("svg",{...ic,children:[(0,o.jsx)("path",{d:"M9 4h6l-1 6 3 3H7l3-3z"}),(0,o.jsx)("path",{d:"M12 13v7"})]})}),(0,o.jsx)("button",{className:"chip lz-chip"+(n?" on":""),onClick:()=>l(!n),"aria-label":"Layout and appearance","aria-expanded":n,children:(0,o.jsxs)("svg",{...ic,children:[(0,o.jsx)("rect",{x:"2.5",y:"4.5",width:"19",height:"15",rx:"3"}),(0,o.jsx)("path",{d:"M12 4.5v15"})]})}),n&&(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)("div",{className:"lz-back",onClick:()=>l(!1)}),(0,o.jsxs)("div",{className:"lz-menu",role:"dialog","aria-label":"Layout and appearance","data-noswipe":"",children:[(0,o.jsx)("div",{className:"lz-h",children:"Layout"}),(0,o.jsx)("div",{className:"lz-seg",role:"radiogroup","aria-label":"Layout",children:s.map(([f,d])=>(0,o.jsx)("button",{role:"radio","aria-checked":e.pref===f,className:"lz-opt"+(e.pref===f?" on":""),onClick:()=>e.setPref(f),children:d},f))}),(0,o.jsx)("div",{className:"lz-note",children:r[e.pref]+(e.pref==="split"&&e.mode!=="split"?" This screen is too narrow for it right now.":"")}),(0,o.jsx)("div",{className:"lz-h",children:"Pinned page"}),(0,o.jsx)("div",{className:"lz-seg",role:"radiogroup","aria-label":"Pinned page",children:Ps.map(([f,d])=>(0,o.jsx)("button",{role:"radio","aria-checked":e.pin===f,className:"lz-opt"+(e.pin===f?" on":""),onClick:()=>u(f),children:d},f))}),(0,o.jsx)("div",{className:"lz-note",children:"Stays on the left in two-page layout. Tap its tab to see it full width."}),(0,o.jsxs)("button",{className:"lz-row",role:"switch","aria-checked":e.lg,onClick:()=>e.setLg(!e.lg),children:[(0,o.jsxs)("span",{children:[(0,o.jsx)("b",{children:"Liquid Glass"}),(0,o.jsx)("small",{children:"Clear glass surfaces, same colors"})]}),(0,o.jsx)("span",{className:"lz-sw"+(e.lg?" on":""),children:(0,o.jsx)("i",{})})]})]})]})]})}'''
s=s[:i]+FY+HY+s[k:]

# 3. main component
rep('let[a,n]=fy(),[l,i]=(0,T.useState)("brief")','let Lz=fy(),a=Lz.mode==="wide",[l,i]=(0,T.useState)("brief")')
rep('Zt=()=>{F>55&&p(),U(0),q.current=null};return(0,o.jsx)(hm.Provider',
    'Zt=()=>{F>55&&p(),U(0),q.current=null},Sd=Lz.mode==="split"&&Lz.pin!==l?Lz.pin:null,Cp=(0,T.useRef)("days");(0,T.useEffect)(()=>{Sd&&k(G=>G.includes(Sd)?G:[...G,Sd])},[Sd]);(0,T.useEffect)(()=>{l!==Lz.pin&&(Cp.current=l)},[l,Lz.pin]);(0,T.useEffect)(()=>{if(Lz.mode==="split"&&l===Lz.pin){let G=Cp.current!==Lz.pin?Cp.current:E.find(O=>O!==Lz.pin);i(G)}},[Lz.mode]);return(0,o.jsx)(hm.Provider')
rep('className:`cr-root ${a?"wide":""}`','className:`cr-root ${a?"wide":""} ${Sd?"split":""} ${Lz.mode==="split"&&!Sd?"solo":""} ${Lz.lg?"lg":""}`')
rep('className:G!==l?"page-off":`page ${y>0?"from-right":y<0?"from-left":"fade-swap"}','className:G===Sd?"page pane-side":G!==l?"page-off":`page ${Sd?"pane-main":""} ${y>0?"from-right":y<0?"from-left":"fade-swap"}')
rep('(0,o.jsx)(hy,{wide:a,onToggle:n})','(0,o.jsx)(hy,{L:Lz,tab:l,go:m})')
rep('.recap,.sheet,.overflow-x-auto")){A.current=null;return}','.recap,.sheet,.overflow-x-auto,.pane-side")){A.current=null;return}')
rep('(0,o.jsx)(Cy,{tab:l,setTab:m,compact:h})','(0,o.jsx)(Cy,{tab:l,setTab:m,compact:h,pin:Lz.mode==="split"?Lz.pin:null})')
rep('function Cy({tab:e,setTab:t,compact:a}){','function Cy({tab:e,setTab:t,compact:a,pin:pn}){')
rep('className:`tab-btn ${e===l?"on":""}`','className:`tab-btn ${e===l?"on":""} ${pn===l?"pinned":""}`')
# 4. preview lives in /next/ and reads the same data file
rep('fetch(`data.json?t=${Date.now()}`','fetch(`../data.json?t=${Date.now()}`')

h=hashlib.sha1(s.encode()).hexdigest()[:10]
out=f'{REPO}/next'; os.makedirs(out,exist_ok=True)
for f in glob.glob(out+'/app.*.js'): os.remove(f)
open(f'{out}/app.{h}.js','w',encoding='utf-8').write(s)
html=open(f'{REPO}/index.html',encoding='utf-8').read()
assert html.count('app.bf0a90d6ac.js')==1 and html.count('href="icon.png"')==2
html=html.replace('app.bf0a90d6ac.js',f'app.{h}.js').replace('href="icon.png"','href="../icon.png"').replace('<title>Cut protocol</title>','<title>Cut protocol · Preview</title>')
open(f'{out}/index.html','w',encoding='utf-8').write(html)
print('built',h,len(s))
