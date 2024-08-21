from enum import Enum

class BidStatus(Enum):
    ACTIVE = 1
    WITHDRAWN = 2
    WINNING = 3

class Bid:
    def __init__(self, bid_id, auction_id, bidder_id, amount):
        self.bid_id = bid_id
        self.auction_id = auction_id
        self.bidder_id = bidder_id
        self.amount = amount
        self.status = BidStatus.ACTIVE
