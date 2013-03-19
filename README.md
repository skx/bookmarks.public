bookmarks.public
================

This repository contains the single HTML file `index.html`.

The bookmarks file is a _template_ which is designed to be edited by the user,
simply replace the bookmarks in the single unordered-list with your own.

Open the file in a browser and you have a simple to use interface for your
bookmarks.

Online Demo
-----------

You may [try out the interface](http://www.steve.org.uk/Software/bookmarks/bookmarks.public/) which contains a small collection of sample bookmarks.


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

If you wish to use this bookmarks script, and are happy for your boobkmarks
to be public, then just fork the repository and have at it.

If you prefer to keep your bookmarks private, as I do, then you'll need to
clone the repository somewhere private.


Contributing
------------

If you wish to submit improvements to the javascript code then I welcome forks
& pull requests.  The sample bookmarks should probably not be changed too much
though - unless you add any major new feature(s).


Steve
--
