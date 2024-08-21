from models.Auction import Auction
from repository.AuctionRepository import AuctionRepository

class AuctionService:
    @classmethod
    def create_auction(cls, auction_id, seller_id, min_bid, max_bid):
        auction = Auction(auction_id, seller_id, min_bid, max_bid)
        AuctionRepository.add_auction(auction)
