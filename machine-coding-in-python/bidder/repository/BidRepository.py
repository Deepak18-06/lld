class BidRepository:
    bids = []

    @classmethod
    def add_bid(cls, bid):
        cls.bids.append(bid)

    @classmethod
    def get_bids_by_auction_id(cls, auction_id):
        return [bid for bid in cls.bids if bid.auction_id == auction_id]
