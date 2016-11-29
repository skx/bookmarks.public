bookmarks.public
================

This repository allows you to save your bookmarks under revision control,
via a simple combination of HTML, CSS & Javascript.

* You add your bookmarks to the file `bookmarks.data`.
* Then view them by opening `index.html` in your browser.
    * The file `bookmarks.css` is used to style the presentation.
    * The file `bookmarks.js` makes the bookmarks interactive.


Online Demo
-----------

You may try out the interface in this online demo:

* https://www.steve.fi/Software/bookmarks/bookmarks.public/
   * [Github Mirror](http://skx.github.io/bookmarks.public/).



Rationale
---------

I didn't like any of the online bookmark-syncing plugins/addins/tools I tested.

The idea of hosting an online bookmark server is appealing, but using the
power of `git` it seems that having a local bookmark file should be pretty robust:

 * New items are added, generally one per line.
 * Existing items can be edited to add new tags.
 * Merges should be painless.

The included javascript magic is present solely to make the bookmarks
manageable, in my private copy I have 400+ bookmarks and with the
tagging support present here they will continue to work for me easily.


Using
-----

If you wish to use this bookmarks script, and are happy for your bookmarks
to be public, then just fork [this repository](https://github.com/skx/bookmarks.public) and you're done.

If you prefer to keep your bookmarks private, as I do, then you'll need to
clone the repository somewhere private.


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


Importing Bookmarks
-------------------

There are some utilities to ease importing your bookmarks beneath the
top-level `importers` directory:

* `importers/firefox/firefox`
   * Import bookmarks from a saved `bookmarks.html` which Firefox exports.
* `importers/pinboard/pinboard.py`
   * Import bookmarks hosted at http://pinboard.in/


### Adding / Editing / Removing

Other online features are supported:

The **Add Bookmark** form allows you to add new bookmark with name, link and comma-separated tags.

When moving your mouse over an existing bookmark, you can either click *recycle icon* to delete it or *pencil icon* to edit it.  The editing action works just in the same way as adding a new bookmark.

Contributing
------------

If you wish to submit improvements to the javascript, or the CSS, then I welcome forks & pull requests.

>**NOTE**: If you submit a change feel free to add a link to your homepage/blog/whatever as part of that.  The included bookmarks are only examples.

Steve
--
