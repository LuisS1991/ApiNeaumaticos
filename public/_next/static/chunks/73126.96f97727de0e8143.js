(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[73126,58244],{73126:function(e,t,n){"use strict";var a=n(64836);Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var r=a(n(24691)).default;t.default=r},24691:function(e){"use strict";function turtle(e){e.languages.turtle={comment:{pattern:/#.*/,greedy:!0},"multiline-string":{pattern:/"""(?:(?:""?)?(?:[^"\\]|\\.))*"""|'''(?:(?:''?)?(?:[^'\\]|\\.))*'''/,greedy:!0,alias:"string",inside:{comment:/#.*/}},string:{pattern:/"(?:[^\\"\r\n]|\\.)*"|'(?:[^\\'\r\n]|\\.)*'/,greedy:!0},url:{pattern:/<(?:[^\x00-\x20<>"{}|^`\\]|\\(?:u[\da-fA-F]{4}|U[\da-fA-F]{8}))*>/,greedy:!0,inside:{punctuation:/[<>]/}},function:{pattern:/(?:(?![-.\d\xB7])[-.\w\xB7\xC0-\uFFFD]+)?:(?:(?![-.])(?:[-.:\w\xC0-\uFFFD]|%[\da-f]{2}|\\.)+)?/i,inside:{"local-name":{pattern:/([^:]*:)[\s\S]+/,lookbehind:!0},prefix:{pattern:/[\s\S]+/,inside:{punctuation:/:/}}}},number:/[+-]?\b\d+(?:\.\d*)?(?:e[+-]?\d+)?/i,punctuation:/[{}.,;()[\]]|\^\^/,boolean:/\b(?:false|true)\b/,keyword:[/(?:\ba|@prefix|@base)\b|=/,/\b(?:base|graph|prefix)\b/i],tag:{pattern:/@[a-z]+(?:-[a-z\d]+)*/i,inside:{punctuation:/@/}}},e.languages.trig=e.languages.turtle}e.exports=turtle,turtle.displayName="turtle",turtle.aliases=[]},64836:function(e){function _interopRequireDefault(e){return e&&e.__esModule?e:{default:e}}e.exports=_interopRequireDefault,e.exports.__esModule=!0,e.exports.default=e.exports}}]);