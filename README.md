bookmarks.public
================

This repository allows you to save your bookmarks under revision control,
via a simple combination of HTML, CSS & Javascript.

* You add your bookmarks to the file `bookmarks.data`.
* Then view them by opening `index.html` in your browser.
    * The file `bookmarks.css` is used to style the presentation.
    * The file `bookmarks.js` makes the bookmarks interactive.

There is a simple online demo hosted at the following location:

* [Online Demo](http://skx.github.io/bookmarks.public/).


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


Usage
-----

If you wish to use this bookmarks script, and are happy for your bookmarks
to be public, then just fork [this repository](https://github.com/skx/bookmarks.public) and you're done.

If you prefer to keep your bookmarks private, as I do, then you'll need to
host your repository somewhere private.

To get started you might wish to examine contributed importers found beneath the [importers directory](importers/), which might be of interest.

For advanced usage you can see:

* [Adding/Editing bookmarks via your browser](Browser.md)


Contributing
------------

If you wish to submit improvements to the javascript, or the CSS, then I welcome forks & pull requests.

>**NOTE**: If you submit a change feel free to add a link to your homepage/blog/whatever as part of that.  The included bookmarks are only examples.


Steve
--
