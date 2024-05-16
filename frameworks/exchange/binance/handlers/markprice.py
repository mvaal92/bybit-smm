from typing import Dict

from frameworks.exchange.base.ws_handlers.ticker import TickerHandler


class BinanceTickerHandler(TickerHandler):
    def __init__(self, data: Dict) -> None:
        self.data = data
        super().__init__(self.data["ticker"])

    def refresh(self, recv: Dict) -> None:
        pass

    def process(self, recv: Dict) -> None:
        self.format["markPrice"] = float(recv["p"])
        self.format["indexPrice"] = float(recv["i"])
        self.format["fundingTime"] = float(recv["T"])
        self.format["fundingRate"] = float(recv["r"])
        self.ticker.update(self.format)
