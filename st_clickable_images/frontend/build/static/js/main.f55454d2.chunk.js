(this.webpackJsonpstreamlit_component_template=this.webpackJsonpstreamlit_component_template||[]).push([[0],{4:function(t,e,n){t.exports=n(5)},5:function(t,e,n){"use strict";n.r(e);var a=n(2);a.a.events.addEventListener(a.a.RENDER_EVENT,(function(t){var e=t.detail,n=document.body.lastElementChild;n&&document.body.removeChild(n);var s=document.body.appendChild(document.createElement("div"));for(var o in e.args.div_style)s.style[o]=e.args.div_style[o];for(var i=0,r=function(t){var n=s.appendChild(document.createElement("img"));for(var o in e.args.img_style)n.style[o]=e.args.img_style[o];n.src=e.args.paths[t],e.args.titles.length>t&&(n.title=e.args.titles[t]),n.onclick=function(){a.a.setComponentValue(t)},n.onload=function(){++i===e.args.paths.length&&a.a.setFrameHeight()}},l=0;l<e.args.paths.length;l++)r(l)})),a.a.setComponentReady()}},[[4,1,2]]]);
//# sourceMappingURL=main.f55454d2.chunk.js.map