from dataclasses import dataclass


@dataclass
class BotState:
    cash: float
    position: int


class AITradingBot:
    def __init__(self, starting_cash: float = 10000.0, max_position: int = 10):
        if starting_cash < 0:
            raise ValueError("starting_cash must be non-negative")
        if max_position <= 0:
            raise ValueError("max_position must be positive")
        self.state = BotState(cash=starting_cash, position=0)
        self.max_position = max_position

    def decide(self, prices: list[float]) -> str:
        if len(prices) < 6:
            return "hold"
        if any(price <= 0 for price in prices):
            raise ValueError("prices must be positive")

        previous_avg = sum(prices[-6:-3]) / 3
        current_avg = sum(prices[-3:]) / 3
        if current_avg > previous_avg:
            return "buy"
        if current_avg < previous_avg:
            return "sell"
        return "hold"

    def execute(self, action: str, price: float, quantity: int = 1) -> None:
        if price <= 0:
            raise ValueError("price must be positive")
        if quantity <= 0:
            raise ValueError("quantity must be positive")

        if action == "buy":
            affordable = int(self.state.cash // price)
            available_capacity = self.max_position - self.state.position
            buy_qty = min(quantity, affordable, available_capacity)
            self.state.cash -= buy_qty * price
            self.state.position += buy_qty
            return

        if action == "sell":
            sell_qty = min(quantity, self.state.position)
            self.state.cash += sell_qty * price
            self.state.position -= sell_qty

    def portfolio_value(self, current_price: float) -> float:
        if current_price <= 0:
            raise ValueError("current_price must be positive")
        return self.state.cash + (self.state.position * current_price)

    def run(self, prices: list[float]) -> list[str]:
        actions: list[str] = []
        for index, price in enumerate(prices, start=1):
            action = self.decide(prices[:index])
            self.execute(action, price)
            actions.append(action)
        return actions


if __name__ == "__main__":
    sample_prices = [100, 101, 102, 103, 105, 106, 104, 102, 101, 99, 98, 100]
    bot = AITradingBot()
    actions = bot.run(sample_prices)
    print("actions:", actions)
    print("cash:", round(bot.state.cash, 2))
    print("position:", bot.state.position)
    print("value:", round(bot.portfolio_value(sample_prices[-1]), 2))
