bookmarks.public
================

This repository contains the single HTML file `index.html`.

The bookmarks file is a template which is designed to be edited by the user,
replacing the bookmarks in the single unordered-list with their own.

The bookmarks file contains some simple javascript which should allow simple
navigtation and interactive use of the bookmarks, when opened via a browser.


Online Demo
-----------

You may [try out the interface](http://www.steve.org.uk/Software/bookmarks/bookmarks.public/) as the sample page contains a small number of (tagged) bookmarks.


Rationale
---------

I didn't like any of the online bookmark-syncing plugins/addins/tools I tested.

The idea of hosting an online bookmark server is appealing, but using the
power of Git it seems that having a local bookmark file should be pretty robust:

 * New items are added, generally one per line.
 * Existing items can be edited to add new tags.
 * Merges should be painless.

The included javascript magic is present solely to make the bookmarks manageable,
in my private copy I have 400+ bookmarks and with the tagging support present here
they will continue to work for me easily.


Using
-----

If you wish to use this bookmarks script, and are happy for your bookmarks
to be public, then just fork [this repository](https://github.com/skx/bookmarks.public) and you're done.

If you prefer to keep your bookmarks private, as I do, then you'll need to
clone the repository somewhere private.


Contributing
------------

If you wish to submit improvements to the javascript code, or layout, then I welcome forks & pull requests.

(If you submit a change feel free to add a link to your homepage/blog/whatever as part of that.  The sample bookmarks are only samples.)

Steve
--
