class AuctionRepository:
    auctions = []

    @classmethod
    def add_auction(cls, auction):
        cls.auctions.append(auction)

    @classmethod
    def get_auction_by_id(cls, auction_id):
        for auction in cls.auctions:
            if auction.auction_id == auction_id:
                return auction
        return None
