playlist_f = 'Ace Of Base - All That She Wants\nNo Doubt - Dont Speak\nBad Boys Blue - You\'re A Woman\nE-Type - Angels Crying\nHaddaway - What is Love'
playlist_f_split = playlist_f.splitlines()
playlist_m = playlist_f_split[::-1]
result = '\n'.join(playlist_m)
print(result)
