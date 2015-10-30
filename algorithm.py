fitzpatrick = {'I': 87.6, 'II': 109.4, 'III': 131.3, 'IV': 197.0, 'V': 262.8, 'VI': 437.8}


class Skin(object):
    def __init__(self, skin_type, skin_exposure, uv_index):
        self.skin_type = skin_type
        self.skin_exposure = skin_exposure
        self.uv_index = uv_index

    def time_needed(self):
        return int((self.skin_type/(self.uv_index/40))/(self.skin_exposure/25))

    def get_time(self):
        time = int((self.skin_type/(self.uv_index/40))/(self.skin_exposure/25))
        seconds_needed = time % 60
        minutes_needed = (time % 3600)/60
        hours_needed = time/3600
        print 'You need %s hours %s minutes and %s seconds of sunlight every other day to get your recommended Vit D dose.' % (hours_needed, minutes_needed, seconds_needed)


def calculate_uv():
    skin_type = fitzpatrick[raw_input('What is your Fitzpatrick skin type (I-VI)?').upper()]
    skin_exposure = float(raw_input('What % of your skin is exposed?'))
    uv_index = float(raw_input('What is the current UV index of your city?'))

    user = Skin(skin_type, skin_exposure, uv_index)

    user.get_time()

calculate_uv()