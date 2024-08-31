import timeit
from onlinebanking_system.banking import BankingSystem

def performance_test():
    bank = BankingSystem()

    # Register 10,000 users
    start_time = timeit.default_timer()
    for i in range(10000):
        bank.register_user(f"user{i}", "1234")
    elapsed = timeit.default_timer() - start_time
    print(f"Time to register 10,000 users: {elapsed:.5f} seconds")

    # Test deposit performance for a logged-in user
    bank.login("user0", "1234")
    start_time = timeit.default_timer()
    bank.deposit(1000)
    elapsed = timeit.default_timer() - start_time
    print(f"Time to deposit for 1 user: {elapsed:.8f} seconds")

    # Test withdraw performance for a logged-in user
    start_time = timeit.default_timer()
    bank.withdraw(500)
    elapsed = timeit.default_timer() - start_time
    print(f"Time to withdraw for 1 user: {elapsed:.8f} seconds")

if __name__ == "__main__":
    performance_test()
