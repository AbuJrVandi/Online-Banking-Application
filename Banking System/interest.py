def calculate_simple_interest(principal, interest_rate, time_years):
    return principal * interest_rate * time_years

def calculate_compound_interest(principal, interest_rate, time_years, compounds_per_year=1):
    return principal * (1 + interest_rate / compounds_per_year) ** (compounds_per_year * time_years) - principal
