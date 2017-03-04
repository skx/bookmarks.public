// ==UserScript==
// @name          bookmarks.public bookmarker
// @description   Opens bookmark management page to bookmark current page
// @author        dluciv
// @license       WTFPLv2 (http://wtfpl.net/)
// @version       0.1.1
// @namespace     https://github.com/skx/bookmarks.public/
//
// @grant         GM_getValue
// @grant         GM_setValue
// @grant         GM_log
// @grant         GM_xmlhttpRequest
// @grant         GM_info
// @grant         GM_getMetadata
// @grant         GM_registerMenuCommand
// @grant         GM_unregisterMenuCommand
// @grant         GM_openInTab
//
// @require       http://raw.github.com/sizzlemctwizzle/GM_config/master/gm_config.js
//
//
// @include       *
// ==/UserScript==

(function() {
  GM_config.init({
    id: 'bookmarks_public_options',
    fields: {
      path_to_bmk_html: {
        label: 'Path to index.html with bookmarks',
        type: 'text',
        'default': 'file:///home/me/bookmarks.public/index.html'
      }
    }
  });

  GM_config.onSave = function() {
    return GM_config.close();
  };

  GM_registerMenuCommand("Bmks.pub.: Add This Page", function() {
    var href = GM_config.get('path_to_bmk_html') +
        "?op=bookmark" +
        "&title=" + encodeURIComponent(document.title) +
        "&url="   + encodeURIComponent(window.location.href)
    ;
    GM_openInTab(href);
  });

  GM_registerMenuCommand("Bmks.pub.: Settings", function() {
    return GM_config.open();
  });

})();
