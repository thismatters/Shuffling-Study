
class PileShuffle(object):
    """Performs a bucket shuffle on a list"""
    def __init__(self, cardinality=10, repetitions=1, randomize=False, 
                 *args, **kwargs):
        super(PileShuffle, self).__init__(*args, **kwargs)
        self.cardinality = cardinality
        self.repetitions = repetitions
        self.randomize = randomize
        self.debug = False

    def shuffle(self, deck):
        piles = [[] for _ in range(self.cardinality)]
        
        def current_pile():
            pile = 0
            while True:
                yield piles[pile]
                pile = (pile + 1) % self.cardinality

        for _ in range(self.repetitions):
            piles = [[] for _ in piles]
            cp = current_pile()
            while deck:
                next(cp).append(deck.pop())

            deck = []
            for pile in piles:
                if self.debug:
                    print(pile)
                deck.extend(pile)
            if self.debug:
                print(deck)
        return deck


# class RandomnessMetrics(object):
#     # def __init__(self):
#     def nearness(self)

def print_list(l, digits=2):
    print(','.join(['{:0{}}'.format(x, digits) for x in l]))

def nearness_count(deck):
    lo_nearness_counts = [0 for card in deck]
    hi_nearness_counts = [0 for card in deck]
    for i, card1 in enumerate(deck):
        for j, card2 in enumerate(deck[i+1:], start=i+1):
            nearness = j - i
            if card1 - card2 == 1:
                lo_nearness_counts[i] = nearness
                hi_nearness_counts[j] = nearness
            if card2 - card1 == 1:
                hi_nearness_counts[i] = nearness
                lo_nearness_counts[j] = nearness
                # break
    print_list(lo_nearness_counts)
    print(sum(lo_nearness_counts))
    print_list(hi_nearness_counts)
    print(sum(hi_nearness_counts))
    print(sum(lo_nearness_counts + hi_nearness_counts) - (len(deck) - 1) * 2)


def subsequences_count(deck, increasing=True):
    count = 0
    modifier = -1
    last_card = 0
    if increasing:
        modifier = 1
        last_card = max(deck) + 1
    for card in deck:
        card *= modifier
        if card < last_card:
            # this card breaks the sequence
            count += 1
        last_card = card
    print(count)


if __name__ == '__main__':
    deck = [x for x in range(0,52)]
    # nearness_count(deck)
    # print_list(deck)
    shuffler = PileShuffle(repetitions=3, cardinality=4)
    shuffled = shuffler.shuffle(deck)
    print_list(shuffled)
    nearness_count(shuffled)
    subsequences_count(shuffled)