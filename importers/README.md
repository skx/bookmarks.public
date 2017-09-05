# Importers

This directory contains a couple of simple importers, which will take
bookmark data from "elsewhere" and massage it into the format this
repository prefers.


## Firefox

The firefox importer allows you to export your bookmarks from Firefox,
or Iceweasel, into this system.  The process requires a couple of steps:

* Open firefox, choose "Bookmarks | Show All bookmarks".
* Then choose "Import & Backup | Export Bookmarks to HTML"
* Save to `~/bookmarks.html`

Once you've done that you should be able to run this, via your
favourite terminal:

     perl importers/firefox/firefox ~/bookmarks.html

## Pinboard

Please read the script, and follow the instructions, for importing bookmarks
from http://pinboard.in/
