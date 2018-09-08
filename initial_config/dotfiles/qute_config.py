# Max 360p.
config.bind('<z>', 'spawn mpv --ytdl-format=best[height<=?360] {url}')

# Max 360p (ASCII).
config.bind('<Shift-z>', 'spawn mpv --ytdl-format=best[height<=?360] {url} -vo caca')

# Max 720p.
config.bind('<x>', 'spawn mpv --ytdl-format=best[height<=?720] {url}')

# Max 1080p.
config.bind('<c>', 'spawn mpv --ytdl-format=best[height<=?1080] {url}')

# Max available.
config.bind('<Shift-c>', 'spawn mpv {url}')
