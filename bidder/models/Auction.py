from enum import Enum

class AuctionStatus(Enum):
    OPEN = 1
    CLOSED = 2

class Auction:
    def __init__(self, auction_id, seller_id, min_bid, max_bid):
        self.auction_id = auction_id
        self.seller_id = seller_id
        self.min_bid = min_bid
        self.max_bid = max_bid
        self.status = AuctionStatus.OPEN
