fitzpatrick = {'I': 87.6, 'II': 109.4, 'III': 131.3, 'IV': 197.0, 'V': 262.8, 'VI': 437.8}


def get_time():
    skin_type = fitzpatrick[raw_input('What is your Fitzpatrick skin type (I-VI)?')]
    skin_exposure = float(raw_input('What % of your skin is exposed?'))
    uv_index = float(raw_input('What is the current UV index of your city?'))

    time_needed = int((skin_type/(uv_index/40))/(skin_exposure/25))
    seconds_needed = time_needed % 60
    minutes_needed = (time_needed % 3600)/60
    hours_needed = time_needed/3600
    print 'You need %s hours %s minutes and %s seconds of sunlight every other day to get your recommended Vit D dose.' % (hours_needed, minutes_needed, seconds_needed)

get_time()

