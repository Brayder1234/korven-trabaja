# Genera index.html reutilizando el CSS de la tienda (pasos-urbanos-assets/template.html)
import os,re
T=open(os.path.expanduser('~/Downloads/setup-shopify/pasos-urbanos-assets/template.html'),encoding='utf-8').read().split('\n')
def L(a,b): return '\n'.join(T[a-1:b])
i_filters=next(i for i,l in enumerate(T) if l.startswith('/* ---------- filters'))
css = L(14,i_filters)                      # base, loader, cursor, nav, hero, botones, marquee, títulos
css += '\n'+L(267,269)                     # .rev (sección en papel)
css += '\n'+L(365,365)+'\n'+L(380,390)      # footer
css += '\n'+L(493,498)+'\n'+L(584,587)+'\n'+L(590,591)
css += r'''
.wrap{max-width:1440px;margin:0 auto;padding:0 var(--pad)}
.hero .meta div b{font:800 26px var(--fd);letter-spacing:-.02em;display:block}
.step{border:1px solid var(--line);border-radius:24px;padding:clamp(24px,3vw,38px);background:var(--bg2);position:relative;overflow:hidden;transition:transform .5s var(--ease),border-color .3s}
.step:hover{transform:translateY(-4px);border-color:#555}
.step .num{font:900 clamp(64px,8vw,110px)/.8 var(--fd);letter-spacing:-.04em;color:#2a2a28}
.step h3{font:900 clamp(22px,2.4vw,30px)/1.05 var(--fd);letter-spacing:-.02em;text-transform:uppercase;margin:22px 0 12px}
.step p{color:var(--mute);max-width:34ch}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.ben{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.bc{border:1px solid #d9d6cd;border-radius:24px;padding:clamp(22px,3vw,34px);background:#fbfaf7;transition:transform .5s var(--ease)}
.bc:hover{transform:translateY(-4px)}
.bc .ic{width:48px;height:48px;border-radius:14px;background:var(--ink-d);color:var(--paper);display:grid;place-items:center;margin-bottom:20px}
.bc .ic svg{width:24px;height:24px}
.bc h3{font:900 clamp(20px,2.2vw,28px)/1.05 var(--fd);letter-spacing:-.02em;text-transform:uppercase;margin-bottom:10px}
.bc p{color:var(--mute-d)}
.faq details{border-bottom:1px solid var(--line);padding:24px 0}
.faq summary{cursor:pointer;font:800 clamp(16px,1.6vw,20px) var(--fd);letter-spacing:-.005em;list-style:none;display:flex;justify-content:space-between;gap:20px;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary i{flex:none;width:36px;height:36px;border-radius:50%;border:1px solid var(--line2);display:grid;place-items:center;transition:background .3s,color .3s,transform .5s var(--ease)}
.faq summary i::before{content:"+";font:600 20px/1 var(--fb)}
.faq details[open] summary i{transform:rotate(45deg);background:var(--ink);color:var(--bg)}
.faq details>p{color:var(--mute);margin-top:14px;max-width:62ch}
.ctaband{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px}
@media(max-width:900px){.steps,.ben{grid-template-columns:1fr}.step{min-height:0}.hero .grid{grid-template-columns:1fr}.stage{order:-1}}
@media(max-width:760px){.hero .meta div b{font-size:22px}.btn{height:52px}.ctaband .btn,.hero .ctas .btn{flex:1 1 100%}}
'''
html=r'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Trabaja con Korven · Vende sneakers sin invertir</title>
<meta name="description" content="Tú buscas los clientes, nosotros despachamos. Vende sneakers Korven sin inventario y gana por cada venta.">
<meta name="theme-color" content="#0a0a0a">
<link rel="icon" href="favicon.png">
<meta property="og:title" content="Trabaja con Korven">
<meta property="og:description" content="Tú buscas los clientes, nosotros despachamos.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
'''+css+r'''
</style>
</head>
<body>
<div class="grain" aria-hidden="true"></div>
<div class="prog" id="prog"></div>
<div class="cur" id="cur"><span>VER</span></div><div class="cur-dot" id="curd"></div>

<div id="loader" aria-hidden="true">
  <div class="ld-in"><img class="lk" src="logo.png" alt=""><div class="lw">KORVEN</div></div>
  <div class="pct" id="pct">0%</div>
  <div class="bar"><i id="lbar"></i></div>
</div>

<nav class="top" id="nav">
  <div class="wrap row">
    <a href="#top" class="brand" aria-label="Korven"><img class="k" src="logo.png" alt=""><span class="w">KORVEN</span></a>
    <div class="links"><a href="#como">Cómo funciona</a><a href="#ganas">Lo que ganas</a><a href="#preguntas">Preguntas</a><a href="https://korvenoficial.store">Tienda</a></div>
    <a class="bagbtn" data-wa="join">Unirme</a>
  </div>
</nav>

<header class="hero" id="top">
  <div class="spot"></div>
  <div class="giant" id="giant">TRABAJA · KORVEN</div>
  <div class="wrap grid">
    <div>
      <span class="eyebrow fade-up" style="--d:.3s">Trabaja con nosotros · Vendedores</span>
      <h1><span class="ln"><span>Tú buscas</span></span><span class="ln"><span>los clientes.</span></span><span class="ln"><span class="o">Nosotros</span></span><span class="ln"><span class="o">despachamos.</span></span></h1>
      <p class="lead fade-up" style="--d:.55s">Vende sneakers Korven sin comprar inventario, sin empacar y sin hacer envíos. Tú consigues a quien quiera un par; de lo demás nos encargamos nosotros.</p>
      <div class="ctas fade-up" style="--d:.7s">
        <a class="btn btn-w mag" data-wa="join">Quiero trabajar con Korven <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
        <a href="#como" class="btn btn-o mag">Cómo funciona</a>
      </div>
      <p class="fade-up" style="--d:.78s;margin-top:14px;color:var(--mute);font-size:13.5px">Te llevamos a nuestro grupo de WhatsApp, donde te explicamos todo.</p>
      <div class="meta fade-up" style="--d:.85s">
        <div><b>$0</b><small>Inversión</small></div>
        <div><b>100%</b><small>Despacho nuestro</small></div>
        <div><b>36–44</b><small>Tallas</small></div>
      </div>
    </div>
    <div class="stage" id="stage"><div class="card3d" id="card3d">
      <div class="shot enter" data-p="0" style="transition-delay:.4s"><img src="img/j3-fragment-01.webp" alt="Jordan 3 Fragment"><div class="lbl"><span>Jordan<br><b>3 Fragment</b></span></div></div>
      <div class="shot enter" data-p="1" style="transition-delay:.52s"><img src="img/lv-skate-black-01.webp" alt="Louis Vuitton Skate"><div class="lbl"><span>Louis Vuitton<br><b>Skate</b></span></div></div>
      <div class="shot enter" data-p="2" style="transition-delay:.64s"><img src="img/amiri-01.webp" alt="Amiri"><div class="lbl"><span>Amiri</span></div></div>
    </div></div>
  </div>
  <div class="scrollcue">SCROLL<i></i></div>
</header>

<div class="marq" aria-hidden="true"><div class="tr" id="marq"></div></div>

<section class="sec" id="como">
  <div class="wrap">
    <div class="sh">
      <div><span class="eyebrow">Paso a paso</span><h2 class="split">Así de <span class="o">simple.</span></h2></div>
      <p class="rv">Tres pasos y empiezas a vender. Sin experiencia y sin invertir un peso.</p>
    </div>
    <div class="steps">
      <div class="step rv"><div class="num">01</div><h3>Recibes tu enlace</h3><p>Te creamos un código y un enlace personal. Cada cliente que compre desde tu enlace queda a tu nombre.</p></div>
      <div class="step rv" style="--d:.1s"><div class="num">02</div><h3>Buscas clientes</h3><p>Compartes el catálogo por WhatsApp, Instagram, estados o donde tengas contactos. Tú hablas con el cliente.</p></div>
      <div class="step rv" style="--d:.2s"><div class="num">03</div><h3>Nosotros despachamos</h3><p>El cliente hace su pedido en la tienda, nosotros lo empacamos y lo enviamos. Tú ganas por cada venta.</p></div>
    </div>
  </div>
</section>

<section class="sec rev" id="ganas">
  <div class="wrap">
    <div class="sh">
      <div><span class="eyebrow">Beneficios</span><h2 class="split">Lo que <span class="o">ganas.</span></h2></div>
      <p class="rv">Todo lo pesado lo hacemos nosotros. Tú solo te dedicas a vender.</p>
    </div>
    <div class="ben">
      <div class="bc rv"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18M17 7.5c0-1.9-2.2-3-5-3s-5 1.1-5 3 2.2 2.6 5 3.5 5 1.6 5 3.5-2.2 3-5 3-5-1.1-5-3"/></svg></div><h3>Cero inversión</h3><p>No compras mercancía ni pagas nada para empezar.</p></div>
      <div class="bc rv" style="--d:.08s"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 7l9-4 9 4-9 4-9-4Z"/><path d="M3 7v10l9 4 9-4V7M12 11v10"/></svg></div><h3>Sin logística</h3><p>No empacas ni envías: nosotros despachamos cada pedido.</p></div>
      <div class="bc rv" style="--d:.16s"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/></svg></div><h3>Tu ganancia es tuya</h3><p>Ganas la diferencia entre el precio mayorista y el precio al que vendes.</p></div>
      <div class="bc rv" style="--d:.24s"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 15l5-4 4 3 3-2 6 4M8 20h8"/></svg></div><h3>Catálogo listo</h3><p>Fotos, tallas y precios ya están en la tienda. Solo compartes tu enlace.</p></div>
    </div>
  </div>
</section>

<section class="sec faq" id="preguntas">
  <div class="wrap">
    <div class="sh">
      <div><span class="eyebrow">Dudas</span><h2 class="split">Preguntas <span class="o">frecuentes.</span></h2></div>
    </div>
    <div>
      <details class="rv"><summary>¿Necesito experiencia o dinero para empezar?<i></i></summary><p>No. Solo necesitas un celular y ganas de vender. No hay inversión inicial.</p></details>
      <details class="rv"><summary>¿Cómo sé cuáles ventas son mías?<i></i></summary><p>Cada cliente que entra por tu enlace personal queda asociado a tu código, y tus ventas aparecen registradas a tu nombre.</p></details>
      <details class="rv"><summary>¿Quién envía los pedidos?<i></i></summary><p>Nosotros. Tú no tocas el producto: confirmamos con el cliente, empacamos y despachamos.</p></details>
      <details class="rv"><summary>¿Cómo empiezo?<i></i></summary><p>Únete a nuestro grupo de WhatsApp. Ahí te explicamos todo paso a paso y te creamos tu código y tu enlace de ventas.</p></details>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="fcta">
      <h2 class="split">¿Listo para <span class="o">vender?</span></h2>
      <a class="btn btn-w mag" data-wa="join">Unirme al grupo de WhatsApp <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
    </div>
    <div class="fgrid">
      <div><a href="#top" class="brand" style="margin-bottom:18px"><img class="k" src="logo.png" alt="" style="height:40px"><span class="w" style="font-size:18px">KORVEN</span></a><p style="max-width:300px;color:var(--mute)">Sneakers seleccionados para quienes no pasan desapercibidos.</p></div>
      <div><h5>Trabaja</h5><a href="#como">Cómo funciona</a><a href="#ganas">Lo que ganas</a><a href="#preguntas">Preguntas</a></div>
      <div><h5>Tienda</h5><a href="https://korvenoficial.store">Ver colección</a><a href="https://korvenoficial.store/#resenas">Reseñas</a></div>
      <div><h5>Síguenos</h5><a href="https://www.instagram.com/korvenstore_/" target="_blank" rel="noopener">Instagram</a><a data-wa="join" target="_blank" rel="noopener">Grupo de WhatsApp</a></div>
    </div>
    <div class="fbig">KORVEN</div>
    <div class="fbot"><span>© <span id="yr"></span> Korven. Todos los derechos reservados.</span><span>korvenoficial.store</span></div>
  </div>
</footer>

<a class="wa-float" data-wa="join" id="waFloat" aria-label="Grupo de WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3Z"/></svg></a>

<script>
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches,FINE=matchMedia('(pointer:fine)').matches;
/* pantalla de carga */
(function(){const bar=$('#lbar'),pct=$('#pct');let p=0,ended=false;const t0=performance.now();
  const end=()=>{if(ended)return;ended=true;bar.style.transform='scaleX(1)';pct.textContent='100%';
    setTimeout(()=>{const l=$('#loader');l.classList.add('out');document.body.classList.add('ready');setTimeout(()=>l.remove(),1200)},250)};
  const step=()=>{if(ended)return;const el=performance.now()-t0;p+=((el>1300?100:Math.min(88,el/14))-p)*.18;if(p>99)p=100;
    bar.style.transform=`scaleX(${p/100})`;pct.textContent=Math.round(p)+'%';if(p>=100)end();else requestAnimationFrame(step)};
  RM?end():requestAnimationFrame(step);setTimeout(end,4000)})();
/* todos los botones llevan al grupo de WhatsApp de vendedores, donde se explica todo */
const GRUPO='https://chat.whatsapp.com/HqqXs7UPL6r11v4TAcZApq';
$$('[data-wa]').forEach(a=>{a.href=GRUPO;a.target='_blank';a.rel='noopener'});
/* marquee */
(function(){const w=['Cero inversión','Sin inventario','Nosotros despachamos','Tú vendes','Tu enlace, tus ventas'];
  const one=w.map((b,i)=>`<span class="${i%2?'o':''}">${b}</span><img src="logo.png" alt="">`).join('');
  $('#marq').innerHTML=`<div class="it">${one}</div><div class="it">${one}</div>`})();
/* cursor */
if(FINE&&!RM){const cur=$('#cur'),curd=$('#curd');let tx=0,ty=0,cx=0,cy=0;
  addEventListener('mousemove',e=>{tx=e.clientX;ty=e.clientY;curd.style.transform=`translate(${tx}px,${ty}px)`});
  (function loop(){cx+=(tx-cx)*.18;cy+=(ty-cy)*.18;cur.style.transform=`translate(${cx}px,${cy}px)`;requestAnimationFrame(loop)})();
  document.addEventListener('mouseover',e=>{cur.classList.toggle('hov',!!e.target.closest('a,button,summary'))});
  $$('.mag').forEach(b=>{b.addEventListener('mousemove',e=>{const r=b.getBoundingClientRect();b.style.transform=`translate(${(e.clientX-r.left-r.width/2)*.25}px,${(e.clientY-r.top-r.height/2)*.35}px)`});b.addEventListener('mouseleave',()=>b.style.transform='')})}
/* aparición */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px',threshold:.1});
function splitWords(el){const walk=(node)=>{[...node.childNodes].forEach(n=>{if(n.nodeType===3){const frag=document.createDocumentFragment();
  n.textContent.split(/(\s+)/).forEach(t=>{if(!t)return;if(/^\s+$/.test(t)){frag.append(t);return}const w=document.createElement('span');w.className='w';const s=document.createElement('span');s.textContent=t;s.style.setProperty('--i',splitWords.i++);w.append(s);frag.append(w)});n.replaceWith(frag)}else walk(n)})};
  splitWords.i=0;walk(el)}
$$('.split').forEach(el=>{splitWords(el);io.observe(el)});$$('.rv').forEach(el=>io.observe(el));
/* spot del hero, scroll */
$('.hero').addEventListener('mousemove',e=>{const r=e.currentTarget.getBoundingClientRect();e.currentTarget.style.setProperty('--mx',(e.clientX-r.left)+'px');e.currentTarget.style.setProperty('--my',(e.clientY-r.top)+'px')});
const nav=$('#nav'),giant=$('#giant'),prog=$('#prog');let lastY=0;
function onScroll(){const y=scrollY;nav.classList.toggle('solid',y>40);nav.classList.toggle('hide',y>lastY&&y>600);lastY=y;
  prog.style.transform=`scaleX(${y/(document.documentElement.scrollHeight-innerHeight||1)})`;
  if(!RM&&y<innerHeight*1.2)giant.style.transform=`translate3d(${-y*.35}px,0,0)`;
  $('#waFloat').classList.toggle('on',y>innerHeight*.8)}
addEventListener('scroll',()=>requestAnimationFrame(onScroll),{passive:true});onScroll();
$('#yr').textContent=new Date().getFullYear();
</script>
</body>
</html>
'''
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'index.html'),'w',encoding='utf-8').write(html)
print(len(html))
