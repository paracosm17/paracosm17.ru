(()=>{"use strict";var e,t={24804:function(e,t,r){var a=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var l=a(r(73609));l.default((function(){l.default('[data-widget="filtered-select"]').each((function(){var e=l.default("#"+this.dataset.filterField),t=l.default(this),r=[];function a(){var a=t.val();t.empty();var o,i=e.val();if(""===i)o=r;else{o=[];for(var n=0;n<r.length;n++)""!==r[n].value&&-1===r[n].filterValue.indexOf(i)||o.push(r[n])}var u=!1;for(n=0;n<o.length;n++){var s=l.default("<option>");s.attr("value",o[n].value),o[n].value===a&&(u=!0),s.text(o[n].label),t.append(s)}u?t.val(a):t.val("")}l.default("option",this).each((function(){var e;e="filterValue"in this.dataset?this.dataset.filterValue.split(","):[],r.push({value:this.value,label:this.label,filterValue:e})})),a(),e.change(a)}))}))},73609:e=>{e.exports=jQuery}},r={};function a(e){var l=r[e];if(void 0!==l)return l.exports;var o=r[e]={id:e,loaded:!1,exports:{}};return t[e].call(o.exports,o,o.exports,a),o.loaded=!0,o.exports}a.m=t,e=[],a.O=(t,r,l,o)=>{if(!r){var i=1/0;for(s=0;s<e.length;s++){for(var[r,l,o]=e[s],n=!0,u=0;u<r.length;u++)(!1&o||i>=o)&&Object.keys(a.O).every((e=>a.O[e](r[u])))?r.splice(u--,1):(n=!1,o<i&&(i=o));n&&(e.splice(s--,1),t=l())}return t}o=o||0;for(var s=e.length;s>0&&e[s-1][2]>o;s--)e[s]=e[s-1];e[s]=[r,l,o]},a.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return a.d(t,{a:t}),t},a.d=(e,t)=>{for(var r in t)a.o(t,r)&&!a.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},a.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),a.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),a.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),a.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.j=4,(()=>{var e={4:0};a.O.j=t=>0===e[t];var t=(t,r)=>{var l,o,[i,n,u]=r,s=0;for(l in n)a.o(n,l)&&(a.m[l]=n[l]);if(u)var d=u(a);for(t&&t(r);s<i.length;s++)o=i[s],a.o(e,o)&&e[o]&&e[o][0](),e[i[s]]=0;return a.O(d)},r=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),a.O(void 0,[751],(()=>a(24804)));var l=a.O(void 0,[751],(()=>a(90971)));l=a.O(l)})();
//# sourceMappingURL=filtered-select.js.3248010da39f.map