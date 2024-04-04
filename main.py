music.play(music.string_playable("G B A G C5 B A B ", 170),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
