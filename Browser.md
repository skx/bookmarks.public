Adding bookmarks via the browser
--------------------------------

The bookmarks are all stored in the standalone file `bookmarks.data`, and
the expected use-case is that you edit that with your favourite editor.

However you may also add bookmarks dynamically, via your browser.  Just
complete the form on the right-side of the interface.  Newly added bookmarks
will be available for you to view immediately, however they will not be
saved by default.

To make your new additions permanent you must click `Save` and overwrite
your local `bookmarks.data` file with the updated version.

Other online features are also supported:


### Adding / Editing / Removing


The **Add Bookmark** form allows you to add new bookmark with name, link and comma-separated tags.

When moving your mouse over an existing bookmark, you can either click *recycle icon* to delete it or *pencil icon* to edit it.  The editing action works just in the same way as adding a new bookmark.

### Browser Integration

For the most of popular web browsers you can install a [userscript](https://en.wikipedia.org/wiki/Greasemonkey)
from [here](add-bookmark.user.js) by clicking **Raw** link.

The intention is that when you use **Bmks.pub.: Add This Page** userscript menu item, browser displays your bookmarks page
having *Link* and *Name* areas populated with the appropriate link and title, such that new bookmark can be added quickly and easily.
Userscript works properly regardless to your bookmarks location, as it is allowed to open the both `file://` and
`http(s)://` URLs. Before bookmarking, please also specify correct `index.html` location using **Bmks.pub.: Settings** menu item.

If you access your bookmarks via `http(s)://`, you may prefer to use following bookmarklet instead of userscript installation:

    window.open("https://myserver/bookmarks.public/index.html" +
        "?op=bookmark" +
        "&title=" + encodeURIComponent(document.title) +
        "&url="   + encodeURIComponent(window.location.href),
        "_blank"
    );

To get it working, please correct your bookmarks URL in the first line, [convert it to bookmarklet](http://mrcoles.com/bookmarklet/),
add browser bookmark with this bookmarklet URL and assign it a shortcut (say, `bl`). Then, when you type `bl` in URL edit box,
browser should suggest using this bookmarklet. The result will be similar: new tab with your bookmarks and your new bookmark
with *Link* and *Name* populated.
