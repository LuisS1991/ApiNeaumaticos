"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[57176,63047],{20791:function(e,a,n){var t=n(93205);function ejs(e){e.register(t),e.languages.ejs={delimiter:{pattern:/^<%[-_=]?|[-_]?%>$/,alias:"punctuation"},comment:/^#[\s\S]*/,"language-javascript":{pattern:/[\s\S]+/,inside:e.languages.javascript}},e.hooks.add("before-tokenize",function(a){e.languages["markup-templating"].buildPlaceholders(a,"ejs",/<%(?!%)[\s\S]+?%>/g)}),e.hooks.add("after-tokenize",function(a){e.languages["markup-templating"].tokenizePlaceholders(a,"ejs")}),e.languages.eta=e.languages.ejs}e.exports=ejs,ejs.displayName="ejs",ejs.aliases=["eta"]},93205:function(e){function markupTemplating(e){!function(e){function getPlaceholder(e,a){return"___"+e.toUpperCase()+a+"___"}Object.defineProperties(e.languages["markup-templating"]={},{buildPlaceholders:{value:function(a,n,t,s){if(a.language===n){var o=a.tokenStack=[];a.code=a.code.replace(t,function(e){if("function"==typeof s&&!s(e))return e;for(var t,l=o.length;-1!==a.code.indexOf(t=getPlaceholder(n,l));)++l;return o[l]=e,t}),a.grammar=e.languages.markup}}},tokenizePlaceholders:{value:function(a,n){if(a.language===n&&a.tokenStack){a.grammar=e.languages[n];var t=0,s=Object.keys(a.tokenStack);walkTokens(a.tokens)}function walkTokens(o){for(var l=0;l<o.length&&!(t>=s.length);l++){var r=o[l];if("string"==typeof r||r.content&&"string"==typeof r.content){var i=s[t],u=a.tokenStack[i],g="string"==typeof r?r:r.content,p=getPlaceholder(n,i),c=g.indexOf(p);if(c>-1){++t;var k=g.substring(0,c),f=new e.Token(n,e.tokenize(u,a.grammar),"language-"+n,u),m=g.substring(c+p.length),d=[];k&&d.push.apply(d,walkTokens([k])),d.push(f),m&&d.push.apply(d,walkTokens([m])),"string"==typeof r?o.splice.apply(o,[l,1].concat(d)):r.content=d}}else r.content&&walkTokens(r.content)}return o}}}})}(e)}e.exports=markupTemplating,markupTemplating.displayName="markupTemplating",markupTemplating.aliases=[]}}]);