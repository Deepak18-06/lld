from models.user import User
def test_cab_booking():
    user = User("deepak", "deepak@gmail.com")
    print("Testing")
    print(user)

if __name__ == "__main__":
    try:
        test_cab_booking()
    except Exception as e:
        print(e)