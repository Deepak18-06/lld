class WinningBidStrategy:
    @classmethod
    def get_winning_bid(cls, bids):
        unique_bids = [bid.amount for bid in bids if bids.count(bid.amount) == 1]
        if unique_bids:
            return max(unique_bids)
        else:
            return None
