import timeit
from OnlineBankingApp import BankingSystem

def performance_test():
    bank = BankingSystem()
    for i in range(10000):
        bank.register_user(f"team@user{i}", "team@123")

    start_time = timeit.default_timer()
    bank.deposit(1000)
    elapsed = timeit.default_timer() - start_time
    print(f"Time to deposit: {elapsed:.5f} seconds")

if __name__ == "__main__":
    performance_test()
