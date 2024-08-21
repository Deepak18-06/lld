from models.Bid import Bid
from repository.BidRepository import BidRepository

class BidService:
    @classmethod
    def create_bid(cls, bid_id, auction_id, bidder_id, amount):
        bid = Bid(bid_id, auction_id, bidder_id, amount)
        BidRepository.add_bid(bid)
