class LowestUniqueBidStrategy:
    @classmethod
    def get_lowest_unique_bid(cls, bids):
        unique_bids = [bid.amount for bid in bids if bids.count(bid.amount) == 1]
        if unique_bids:
            return min(unique_bids)
        else:
            return None
