import unittest

from ai_trading_bot import AITradingBot


class AITradingBotTests(unittest.TestCase):
    def test_decide_hold_when_not_enough_history(self):
        bot = AITradingBot()
        self.assertEqual(bot.decide([100, 101, 102]), "hold")

    def test_decide_buy_on_uptrend(self):
        bot = AITradingBot()
        prices = [100, 100, 100, 101, 102, 103]
        self.assertEqual(bot.decide(prices), "buy")

    def test_decide_sell_on_downtrend(self):
        bot = AITradingBot()
        prices = [103, 102, 101, 100, 100, 100]
        self.assertEqual(bot.decide(prices), "sell")

    def test_execute_respects_limits(self):
        bot = AITradingBot(starting_cash=50, max_position=2)
        bot.execute("buy", price=30, quantity=3)
        self.assertEqual(bot.state.position, 1)
        self.assertEqual(bot.state.cash, 20)
        bot.execute("buy", price=10, quantity=3)
        self.assertEqual(bot.state.position, 2)
        self.assertEqual(bot.state.cash, 10)
        bot.execute("sell", price=20, quantity=5)
        self.assertEqual(bot.state.position, 0)
        self.assertEqual(bot.state.cash, 50)

    def test_run_returns_action_per_price(self):
        bot = AITradingBot()
        prices = [100, 101, 102, 103, 104, 105]
        actions = bot.run(prices)
        self.assertEqual(len(actions), len(prices))
        self.assertEqual(actions[-1], "buy")


if __name__ == "__main__":
    unittest.main()
