from cacheService import Class
if __name__ == "__main__":
    print("Lazy Implementation --")
    first = Class.get_instance()
    print("got the instance first time")
    first.put_value(1,"deepak")
    print("value added using first instance return")
    second = Class.get_instance()
    print("got value using second instance return")
    value = second.get_value(1)
    print(value)
