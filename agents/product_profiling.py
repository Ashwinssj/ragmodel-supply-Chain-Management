def profile_product(product_name):
    if "ceramic" in product_name.lower():
        return {"category": "fragile", "turnover": "medium", "perishability": "none"}
    else:
        return {"category": "general", "turnover": "low", "perishability": "none"}
