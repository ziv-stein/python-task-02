"""Calculates the price of a recipe from ingredient prices and amounts."""

GRAMS_PER_PRICE_UNIT = 100


def piece_of_cake(prices: dict, optionals: list | None = None, **amounts) -> float:
    """
    Returns the total price of a recipe.

    :param prices: Price per 100 grams of each ingredient
    :param optionals: Ingredients to skip
    :param amounts: Grams to buy of each ingredient
    :return: Total price of the recipe
    """
    if optionals is None:
        optionals = []

    return sum(
        prices[ingredient] * grams / GRAMS_PER_PRICE_UNIT
        for ingredient, grams in amounts.items()
        if ingredient not in optionals
    )


def main():
    """Prints a few example calls."""
    print(piece_of_cake({"chocolate": 18, "milk": 8}, chocolate=200, milk=100))
    print(piece_of_cake({"chocolate": 18, "milk": 8}, optionals=["milk"], chocolate=300))
    print(piece_of_cake({}))


if __name__ == "__main__":
    main()
