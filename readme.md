# About
Prevu is a plugin for Sublime Text 2 that allows you to quickly open your projects local url for testing.

# Installation 
- Use Package Control to install
- Or you can download or clone directly and drop into your Sublime Text 2 packages directory (plugin folder must be named Prevu)
-- `Preferences > Browse Packages` to get to the package directory

# Usage
Add a comment with the following tag:
```
location: project/
```

And use the key-combo `ctrl + alt + p` to use prevu. This will cause a new tab or window to open in your default browser.

Url will turn into: `http://localhost/project`

# Settings
Settings can be configured and found under `Preferences > Package Settings > Prevu`

Supports `#`, `//`, `*`, `!` comments out of the box.

# Download
https://github.com/Nijikokun/Prevu/zipball/master

# License

Prevu is released under AOL <http://aol.nexua.org> (c) Nijikokun 2012

# Version 0.1
- Initial release