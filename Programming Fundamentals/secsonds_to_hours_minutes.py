totalSeconds = float(input("Please enter total seconds: "))
hours = totalSeconds // 3600
minutes = (totalSeconds // 60) % 60
seconds = totalSeconds % 60

print( hours, "h", minutes, "m", seconds, "s" )