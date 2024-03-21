from models.User import User
from services.UserService import UserService
from services.AuctionService import AuctionService
from services.BidService import BidService
from strategy.WinningBidStrategy import WinningBidStrategy
from strategy.LowestUniqueBidStrategy import LowestUniqueBidStrategy
from repository.BidRepository import BidRepository

def add_buyer(user):
    UserService.add_user(user)

def add_seller(user):
    UserService.add_user(user)

def create_auction(auction_id, min_bid, max_bid, seller):
    AuctionService.create_auction(auction_id, seller.user_id, min_bid, max_bid)

def create_bid(buyer, auction_id, amount):
    BidService.create_bid(buyer.user_id, auction_id, amount)

def update_bid(buyer, auction_id, amount):
    BidService.update_bid(buyer.user_id, auction_id, amount)

def close_auction(auction_id):
    winner = AuctionService.close_auction(auction_id)
    return winner

def main():
    buyer1 = User(1, "buyer1", "buyer1@example.com")
    buyer2 = User(2, "buyer2", "buyer2@example.com")
    buyer3 = User(3, "buyer3", "buyer3@example.com")
    seller1 = User(4, "seller1", "seller1@example.com")

    add_buyer(buyer1)
    add_buyer(buyer2)
    add_buyer(buyer3)
    add_seller(seller1)
    create_auction("A1", 10, 50, seller1)
    create_bid(buyer1, "A1", 17)
    create_bid(buyer2, "A1", 15)
    update_bid(buyer2, "A1", 19)
    create_bid(buyer3, "A1", 19)
    winner = close_auction("A1")

    print("Winner of auction A1:", winner)

if __name__ == "__main__":
    main()

# # Example usage
# if __name__ == "__main__":
#     # Add users
#     user1 = User(1, "Alice", "alice@example.com")
#     user2 = User(2, "Bob", "bob@example.com")

#     # Create auctions
#     AuctionService.create_auction(1, 1, 50, 100)

#     # Place bids
#     BidService.create_bid(1, 1, 1, 50)
#     BidService.create_bid(2, 1, 2, 90)
#     BidService.create_bid(3, 1, 1, 100)
#     BidService.create_bid(4, 1, 2, 90)
#     BidService.create_bid(5, 1, 1, 70)
#     BidService.create_bid(6, 1, 2, 100)

#     # Close auction and determine winning bid
#     bids = BidRepository.get_bids_by_auction_id(1)
#     winning_bid = WinningBidStrategy.get_winning_bid(bids)
#     print("Winning bid:", winning_bid)

#     # Determine lowest unique bid
#     lowest_unique_bid = LowestUniqueBidStrategy.get_lowest_unique_bid(bids)
#     print("Lowest unique bid:", lowest_unique_bid)
