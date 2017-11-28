#!/usr/bin/bash
#Dependencies: libreoffice, sxiv, sublime-text, evince, vlc, deadbeef, xarchiver, p7zip
#images
xdg-mime default sxiv.desktop image/png
xdg-mime default sxiv.desktop image/jpg
xdg-mime default sxiv.desktop image/bmp
xdg-mime default sxiv.desktop image/gif
xdg-mime default sxiv.desktop image/jpeg
xdg-mime default sxiv.desktop image/tiff
xdg-mime default sxiv.desktop image/x-portable-pixmap
#text files, codes
xdg-mime default sublime_text.desktop application/sql
xdg-mime default sublime_text.desktop text/plain
xdg-mime default sublime_text.desktop text/x-python
xdg-mime default sublime_text.desktop application/x-shellscript 
xdg-mime default sublime_text.desktop text/css
xdg-mime default sublime_text.desktop text/html
xdg-mime default sublime_text.desktop application/xml
xdg-mime default sublime_text.desktop text/x-c
#documents
xdg-mime default libreoffice-writer.desktop application/rtf
xdg-mime default libreoffice-writer.desktop application/msword
xdg-mime default libreoffice-impress.desktop application/vnd.ms-powerpoint
xdg-mime default libreoffice-calc.desktop application/vnd.ms-excel
xdg-mime default zathura.desktop application/pdf
#video
xdg-mime default vlc.desktop video/msvideo
xdg-mime default vlc.desktop video/avi
xdg-mime default vlc.desktop video/x-msvideo
xdg-mime default vlc.desktop video/quicktime
xdg-mime default vlc.desktop video/mpeg
#audio
xdg-mime default deadbeef.desktop audio/basic
xdg-mime default deadbeef.desktop audio/vorbis
xdg-mime default deadbeef.desktop audio/wav
xdg-mime default deadbeef.desktop audio/x-wav
xdg-mime default deadbeef.desktop application/ogg
xdg-mime default deadbeef.desktop audio/mpeg
#archives
xdg-mime default xarchiver.desktop application/x-bzip2
xdg-mime default xarchiver.desktop application/x-compressed-zip
xdg-mime default xarchiver.desktop application/zip
xdg-mime default xarchiver.desktop application/x-tar
xdg-mime default xarchiver.desktop application/x-gzip
xdg-mime default xarchiver.desktop application/x-rar-compressed
xdg-mime default xarchiver.desktop application/octet-stream
#windows-stuff
xdg-mime default wine.desktop application/octet-stream

#copy urxvt config
cp ~/.config/i3/initial_config/files/urxvt_config ~/.Xdefaults
