from sim import sim_heuristic, Game, Card

decklists = {

    'BTL' : [
        (4, 'Sakura-Tribe Elder'),
        (2, 'Snapcaster Mage'),
        (4, 'Cryptic Command'),
        (3, 'Lightning Bolt'),
        (4, 'Remand'),
        (1, 'Electrolyze'),
        (4, 'Bring to Light'),
        (1, 'Anger of the Gods'),
        (2, 'Farseek'),
        (1, 'Kodamas Reach'),
        (1, 'Engineered Explosives'),
        (3, 'Scapeshift'),
        (4, 'Search for Tomorrow'),

        (2, 'Forest'),
        (3, 'Island'),
        (1, 'Mountain'),
        (1, 'Plains'),
        (2, 'Breeding Pool'),
        (1, 'Cinder Glade'),
        (4, 'Misty Rainforest'),
        (1, 'Temple Garden'),
        (4, 'Steam Vents'),
        (4, 'Stomping Ground'),
        (2, 'Valakut, the Molten Pinnacle'),
        (1, 'Hallowed Fountain')
    ],
    }

class Game_btl(Game):

    def __init__(self, deck):
        game.__init__(self, deck)

    def play_spell(self, name):
        self.hand.remove(name)
        self.graveyard += 1

é        if name = 'Search for Tomorrow':
            if (game.available_mana('G')):
                game.play_spell('Search for Tomorrow')
                self.played.append(name)

        self.played.append(name)

def heuristic(game, verbose=False):

    def play_spell(self, name):
        self.hand.remove(name)
        self.graveyard += 1

        if name = 'Search for Tomorrow':
            if (game.available_mana('G')):
                game.play_spell('Search for Tomorrow')
            self.played.append(name)


    def land_drop():
        for fetch in ['Misty Rainforest', 'Windswept Heath', 'Wooded Foothills']:
            if game.in_hand(fetch):
                game.play_spell(fetch)
                if 'Breeding Pool' in game.library:
                    game.play_from_library('Breeding Pool')
                    if verbose:
                        print(fetch + ' -> Breeding Pool')
                    return True
                if 'Forest' in game.library:
                    game.play_from_library('Forest')
                    if verbose:
                        print(fetch + ' -> Forest')
                    return True

        if game.in_hand('Breeding Pool') and not game.can_pay('U'):
            game.play('Breeding Pool')
            if verbose:
                print('Breeding Pool')
            return True

        if game.in_hand('Breeding Pool'):
            game.play('Breeding Pool')
            if verbose:
                print('Breeding Pool')
            return True

        if game.in_hand('Forest'):
            game.play('Forest')
            if verbose:
                print('Forest')
            return True


        return False

    while game.mulligan > 4:
        hand = game.draw_hand()
        green_lands = len([ c for c in hand if Card(c).can_produce_mana('G') ])
        lands = len([ c for c in hand if Card(c).can_produce_mana() ])
        critters = len([ c for c in hand if Card(c).has_infect() ])

        if lands >= 2 and green_lands >= 1 and critters >= 1:
            break

    if verbose:
        print('Start')
        print(game)

    turn = 1

    infect = 0

    while True:
        if verbose:
            print('T' + str(turn))

        game.untap()
        if turn > 1:
            new_card = game.draw()
            if verbose:
                print('Draw : ' + new_card[:3])


        drop = False
        drop = land_drop()

        if verbose:
            print('%sLandfall' % '' if drop else 'No land')

        while game.in_hand('Search for Tomorrow') and game.can_pay(['G']):
            if verbose:
                print('Search for Tomorrow')

            play_spell('Search for Tomorrow')
            game.optimal_pay(['G'])

        turn += 1

        if verbose:
            print(game)

        if turn > 10:
            break

    return None

if __name__ == '__main__':
    for hypothesis in decklists:
        if hypothesis != 'BTL':
            continue
        print(hypothesis)
        decklist = decklists[hypothesis]

        ntries = 1
        d = sim_heuristic(decklist, heuristic,
                heuristic_params={
                    'verbose':True
                }, ntries=ntries)

        for k in range(2,11):
            if k in d:
                print('%.3f' % (d[k]/float(ntries)))
            else:
                print('0.0')
