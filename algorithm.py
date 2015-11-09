fitzpatrick = {'I': 87.6, 'II': 109.4, 'III': 131.3, 'IV': 197.0, 'V': 262.8, 'VI': 437.8}
skin_area = {'Face': 4, 'Neck': 2, 'Chest': 26, 'Hands': 6, 'Arms': 14, 'Legs': 14, 'Thighs': 18}
answers = ['Y', 'YES', 'N', 'NO']


class Skin(object):
    def __init__(self, skin_type, skin_exposure, uv_index):
        self.skin_type = skin_type
        self.skin_exposure = skin_exposure
        self.uv_index = uv_index

    def get_time(self):  # used to calculate time in sunlight needed to get SDD (Standard Vit D Dose)
        if self.skin_exposure == 0:
            print 'You need some skin exposure to get Vit D from the sun.'
        else:
            time = int((self.skin_type / (self.uv_index / 40)) / (self.skin_exposure / 25))
            seconds_needed = time % 60
            minutes_needed = (time % 3600) / 60
            hours_needed = time / 3600
            print 'You need %s hours %s minutes and %s seconds of sunlight every other day to get your recommended Vit D dose.' % (hours_needed, minutes_needed, seconds_needed)

    def get_burn(self):  # used to calculate MED (minimal erythema dose)
        if self.skin_exposure == 0:
            print 'You need to have skin exposed to be burnt'
        else:
            time = int(2 * (self.skin_type / (self.uv_index / 40)))
            seconds_needed = time % 60
            minutes_needed = (time % 3600) / 60
            hours_needed = time / 3600
            print 'You need a minimum %s hours %s minutes and %s seconds of sunlight to burn.' % (hours_needed, minutes_needed, seconds_needed)


def calculate_uv():
    raw_type = raw_input('What is your Fitzpatrick skin type (I-VI)? ').upper()
    while raw_type not in fitzpatrick:
        raw_type = raw_input('Answer not valid. What is your Fitzpatrick skin type (I-VI)? ').upper()
    skin_type = fitzpatrick[raw_type]

    skin_exposure = 0  # asks about each individual skin area and adds all the percentages from skin_area dictionary
    for i in skin_area:
        area = raw_input(i + ' exposed?(Y/N) ').upper()
        while area not in answers:
            area = raw_input('Answer not valid. ' + i + ' exposed?(Y/N) ').upper()
        if area == 'Y' or area == 'YES':
            skin_exposure += skin_area[i]

    uv = False
    while not uv:
        try:
            uv_index = float(raw_input('What is the current UV index of your city? '))
            uv = True
        except ValueError:
            print 'Answer not valid. Please retry.'

    user = Skin(skin_type, skin_exposure, uv_index)

    user.get_time()
    user.get_burn()


calculate_uv()
