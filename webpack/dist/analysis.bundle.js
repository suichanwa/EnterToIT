/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/analytics.js":
/*!**************************!*\
  !*** ./src/analytics.js ***!
  \**************************/
/***/ (() => {

eval("function createAnalytics(){\n    let counter = 0;\n\n    const listener = () => counter++;\n\n    document.addEventListener('click', listener);\n\n    return { \n        destroy(){\n            document.removeEventListener('click', listener);\n            isDestroyes = true;\n        },\n\n        getClick(){\n            if(isDestroyes){\n                console.log(\"testing\");\n            }\n            return counter;\n        }\n    }\n}\n\nwindow.analytics = createAnalytics();\n\n//# sourceURL=webpack://webpack/./src/analytics.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/analytics.js"]();
/******/ 	
/******/ })()
;