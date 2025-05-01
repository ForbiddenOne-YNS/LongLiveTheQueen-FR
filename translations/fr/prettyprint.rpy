init python:
    # Change these functions to apply your own language's rules as appropriate.

    def readable_number_small_translation(i):
        ret = ''
        if i!=int(i):
            rem = i-int(i)
            if i>=0 and i<=19 and rem>=.96:
                ret = 'presque '
                i = int(i+1)
            else:
                i = int(i)
        if i>=0 and i<=20:
            ret += ('aucun','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf','vingt')[int(i)]
        else:
            ret = str(i)
        if rem>=.88 and rem<.96:
            ret += ' et neuf dixièmes'
        elif rem>=.73:
            ret += ' et trois quarts'
        elif rem>=.6:
            ret += ' et plus de la moitié'
        elif rem>=.47:
            ret += ' et une moitié'
        elif rem>=.4:
            ret += ' et presque une moitié'
        elif rem>=.2:
            ret += ' et un quart'
        elif rem>=.07:
            ret += ' et un dixième'
        elif rem>.03:
            ret = 'un rien de plus que '+ret
        if ret.startswith('aucun et '):
            ret = ret[7:]
        return ret

    # and change 'raw' to the directory name the translation files are in.
    # If you don't want to use a function, comment it and the lines pertaining
    # to it out and the game will fall back to simple stringification for most
    # functions.  You will need to include barracks_report_translation,
    # however.

    readable_number_small_translations['fr'] = readable_number_small_translation
    def land_military_desc_translation(soldiers):
        if int(soldiers/1200.0):
            return readable_number_small(soldiers/1200.0)+' battalions'
        elif soldiers/1200.0<=.03:
            return 'une poignée de soldats'
        elif soldiers/1200.0<.07:
            return "plus ou moins un peloton"
        return readable_number_small(soldiers/1200.0)+" d'un batallion'"
    land_military_desc_translations['fr'] = land_military_desc_translation

    def barracks_report_translation(amt):
        battalions = int(amt/1200)
        amt -= battalions*1200
        companies = 0
        platoons = 0
        if amt>0:
            companies = int(amt/300)
            amt -= companies*300
        if amt>0:
            platoons = max(int(amt/100),1)
        ret = ''
        if battalions:
            ret = readable_number(battalions)+' '
            if battalions>1:
                ret += 'batallions'
            else:
                ret += 'batallion'
        if companies:
            if battalions and platoons:
                ret += ', '
            else:
                ret += ' et '
            ret += readable_number(companies)
            if companies>1:
                ret += ' compagnies'
            else:
                ret += ' compagnie'
        if platoons:
            if companies and battalions:
                ret += ', et '
            elif companies or battalions:
                ret += ' et '
            ret += readable_number(platoons)+' '
            if platoons>1:
                ret += 'pelotons'
            else:
                ret += 'peloton'
        return ret

    barracks_report_translations['fr'] = barracks_report_translation

    def readable_number_translation(i):
        num_words = ('aucun', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze', 'treize','quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf', 'vingt')
        tens = ('zérante', 'dix', 'vingt', 'trente', 'quarante', 'cinquante', 'soixante', 'septante', 'octante', 'nonante')
        if i != int(i):
            i = int(i)
        if not i:
            return 'aucun'
        ret = ''
        if i > 1000:
            ret = num_words[int(i / 1000)] + ' mille'
            i = i % 1000
        if i >= 100:
            if ret:
                ret += ' '
            ret += num_words[int(i / 100)] + ' cent'
        i = i % 100
        if i:
            if ret:
                ret += ' '
            if i < 20:
                return ret + num_words[i]
            else:
                ret += tens[int(i / 10)]
                if i % 10 == 1:
                    ret += ' et un'
                else:
                    if i % 10:
                        ret += '-'
                        ret += num_words[i%10]
        return ret
    readable_number_translations['fr'] = readable_number_translation
