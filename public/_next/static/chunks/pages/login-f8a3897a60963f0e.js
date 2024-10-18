(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[83459],{45977:function(e,t,r){"use strict";r.d(t,{Z:function(){return o}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,n.Z)("Lock",[["rect",{width:"18",height:"11",x:"3",y:"11",rx:"2",ry:"2",key:"1w4ew1"}],["path",{d:"M7 11V7a5 5 0 0 1 10 0v4",key:"fwvmzm"}]])},56953:function(e,t,r){"use strict";r.d(t,{Z:function(){return o}});var n=r(45711);/**
 * @license lucide-react v0.359.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */let o=(0,n.Z)("Mail",[["rect",{width:"20",height:"16",x:"2",y:"4",rx:"2",key:"18n3k1"}],["path",{d:"m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7",key:"1ocrg3"}]])},36429:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/login",function(){return r(37644)}])},37644:function(e,t,r){"use strict";r.r(t),r.d(t,{Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Label_571070df0f8ead809c11ca78dfcc924c:function(){return Label_571070df0f8ead809c11ca78dfcc924c},Root_545e896022c43a9f6366a180b17cadb3:function(){return Root_545e896022c43a9f6366a180b17cadb3},Toaster_6e90e5e87a1cac8c96c683214079bef3:function(){return Toaster_6e90e5e87a1cac8c96c683214079bef3},default:function(){return Component}});var n=r(82729),o=r(71965),c=r(4511),a=r(67294),i=r(60687),s=r(6608),l=r(56953),d=r(45977),_=r(15637),m=r(70917),f=r(64712),u=r(73954),h=r(21839),p=r(46822),g=r(9008),b=r.n(g);function _templateObject(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Toaster_6e90e5e87a1cac8c96c683214079bef3(){let{resolvedColorMode:e}=(0,a.useContext)(i.kc);s.xL.__toast=f.A;let[t,r]=(0,a.useContext)(i.DR),n={description:"Check if server is reachable at ".concat((0,s.LH)(u.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[c,l]=(0,a.useState)(!1);return(0,a.useEffect)(()=>{r.length>=2?c||f.A.error("Cannot connect to server: ".concat(r.length>0?r[r.length-1].message:"","."),{...n,onDismiss:()=>l(!0)}):(f.A.dismiss("websocket-error"),l(!1))},[r]),(0,o.tZ)(f.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Fallback(e){let{error:t,resetErrorBoundary:r}=e;return(0,o.BX)("div",{children:[(0,o.tZ)("p",{children:"Ooops...Unknown Reflex error has occured:"}),(0,o.tZ)("p",{css:{color:"red"},children:t.message}),(0,o.tZ)("p",{children:"Please contact the support."})]})}function Root_545e896022c43a9f6366a180b17cadb3(){let[e,t]=(0,a.useContext)(i.DR),r=(0,a.useRef)(null);s.xL.ref_email=r;let n=(0,a.useRef)(null);s.xL.ref_password=n;let c=(0,a.useRef)(null);s.xL.ref_remember_me=c;let _=(0,a.useCallback)(t=>{let r=t.target;t.preventDefault();let n={...Object.fromEntries(new FormData(r).entries()),remember_me:(0,s.eA)(s.xL.ref_remember_me),email:(0,s.eA)(s.xL.ref_email),password:(0,s.eA)(s.xL.ref_password)};e([(0,s.ju)("reflex___state____state.api_neaumaticos____auth____local__auth____local_auth_state.api_neaumaticos____auth____login____login_state.on_submit",{form_data:n})])});return(0,o.BX)(p.fC,{className:"Root ",css:{width:"100%"},onSubmit:_,children:[(0,o.BX)(h.xu,{css:{marginBottom:"1.5rem"},children:[(0,o.tZ)("label",{css:{display:"block",fontWeight:"700",marginBottom:"0.5rem",color:"#374151",fontSize:"0.875rem",lineHeight:"1.25rem"},children:"Email Address"}),(0,o.BX)(h.xu,{css:{position:"relative"},children:[(0,o.tZ)(l.Z,{css:{position:"absolute",height:"1.25rem",left:"0.75rem",color:"#9CA3AF",top:"0.75rem",width:"1.25rem"}}),(0,o.tZ)("input",{css:{borderWidth:"2px",borderColor:"#E5E7EB","&:focus":{"border-color":"#3B82F6"},outlineStyle:"none",paddingLeft:"2.5rem",paddingRight:"0.75rem",paddingTop:"0.5rem",paddingBottom:"0.5rem",borderRadius:"0.5rem",width:"100%"},id:"email",placeholder:"you@example.com",ref:r,type:"text"})]})]}),(0,o.BX)(h.xu,{css:{marginBottom:"1.5rem"},children:[(0,o.tZ)("label",{css:{display:"block",fontWeight:"700",marginBottom:"0.5rem",color:"#374151",fontSize:"0.875rem",lineHeight:"1.25rem"},children:"Password"}),(0,o.BX)(h.xu,{css:{position:"relative"},children:[(0,o.tZ)(d.Z,{css:{position:"absolute",height:"1.25rem",left:"0.75rem",color:"#9CA3AF",top:"0.75rem",width:"1.25rem"}}),(0,o.tZ)("input",{css:{borderWidth:"2px",borderColor:"#E5E7EB","&:focus":{"border-color":"#3B82F6"},outlineStyle:"none",paddingLeft:"2.5rem",paddingRight:"0.75rem",paddingTop:"0.5rem",paddingBottom:"0.5rem",borderRadius:"0.5rem",width:"100%"},id:"password",placeholder:"••••••••",ref:n,type:"password"})]})]}),(0,o.BX)(h.kC,{css:{display:"flex",alignItems:"center",justifyContent:"space-between",marginBottom:"1.5rem"},children:[(0,o.BX)(h.kC,{css:{display:"flex",alignItems:"center"},children:[(0,o.tZ)("input",{css:{borderColor:"#D1D5DB","&:focus":{"--ring-color":"#3B82F6"},height:"1rem",borderRadius:"0.25rem",color:"#3B82F6",width:"1rem"},id:"remember-me",ref:c,type:"checkbox"}),(0,o.tZ)("label",{css:{display:"block",marginLeft:"0.5rem",color:"#374151",fontSize:"0.875rem",lineHeight:"1.25rem"},children:"Remember me"})]}),(0,o.tZ)("a",{css:{"&:hover":{color:"#1D4ED8"},color:"#3B82F6",fontSize:"0.875rem",lineHeight:"1.25rem"},href:"#",children:"Forgot password?"})]}),(0,o.tZ)("button",{css:{backgroundColor:"#3B82F6","&:focus":{"outline-style":"none","box-shadow":"0 0 0 3px rgba(59, 130, 246, 0.5)"},fontWeight:"700","&:hover":{"background-color":"#2563EB"},paddingLeft:"1rem",paddingRight:"1rem",paddingTop:"0.75rem",paddingBottom:"0.75rem",borderRadius:"0.5rem",color:"#ffffff",width:"100%"},type:"submit",children:"Log In"})]})}let x=(0,m.F4)(_templateObject());function Label_571070df0f8ead809c11ca78dfcc924c(){let e=(0,a.useContext)(i.M4.reflex___state____state__api_neaumaticos____auth____local__auth____local_auth_state__api_neaumaticos____auth____login____login_state);return(0,o.tZ)("label",{css:{display:"block",fontWeight:"700",marginBottom:"0.5rem",color:"#e74c3c",fontSize:"0.875rem",lineHeight:"1.25rem",textAlign:"center"},children:e.error_message})}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,a.useContext)(i.DR);return(0,o.tZ)(a.Fragment,{children:(0,s.oA)(t.length>0)?(0,o.tZ)(a.Fragment,{children:(0,o.tZ)(_.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(x," 1s infinite")},size:32})}):(0,o.tZ)(a.Fragment,{})})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,a.useContext)(i.DR);return(0,o.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,o.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}function Component(){let[e,t]=(0,a.useContext)(i.DR);return(0,o.BX)(c.SV,{FallbackComponent:Fallback,onError:(t,r)=>{e([(0,s.ju)("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception",{stack:t.stack})])},children:[(0,o.BX)(a.Fragment,{children:[(0,o.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,o.tZ)(Toaster_6e90e5e87a1cac8c96c683214079bef3,{})]}),(0,o.tZ)(a.Fragment,{children:(0,o.tZ)(h.xu,{className:"font-inter",css:{backgroundColor:"#F3F4F6",display:"flex",alignItems:"center",justifyContent:"center",minHeight:"100vh"},children:(0,o.BX)(h.xu,{css:{backgroundColor:"#ffffff",maxWidth:"28rem",padding:"2rem",borderRadius:"0.5rem",boxShadow:"0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",width:"100%"},children:[(0,o.BX)(h.xu,{css:{marginBottom:"2rem",textAlign:"center"},children:[(0,o.tZ)(h.kC,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,o.tZ)("img",{css:{width:"25%"},src:"/Icon.png"})}),(0,o.tZ)(h.X6,{as:"h1",css:{fontWeight:"700",fontSize:"1.875rem",lineHeight:"2.25rem",color:"#1F2937"},children:"TireAPI"}),(0,o.tZ)(h.xv,{as:"p",css:{marginTop:"0.5rem",color:"#4B5563"},children:"Log in to your account"})]}),(0,o.tZ)(Root_545e896022c43a9f6366a180b17cadb3,{}),(0,o.tZ)(h.xu,{css:{marginTop:"2rem",textAlign:"center"},children:(0,o.BX)(h.xv,{as:"p",css:{color:"#4B5563",fontSize:"0.875rem",lineHeight:"1.25rem"},children:["Don't have an account? ",(0,o.tZ)("a",{css:{"&:hover":{color:"#1D4ED8"},color:"#3B82F6"},href:"/register",children:"Sign up"})]})}),(0,o.tZ)(Label_571070df0f8ead809c11ca78dfcc924c,{})]})})}),(0,o.BX)(b(),{children:[(0,o.tZ)("title",{children:"Login Api"}),(0,o.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[43534,84389,49774,92888,40179],function(){return e(e.s=36429)}),_N_E=e.O()}]);