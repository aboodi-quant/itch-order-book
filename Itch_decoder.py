class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}
        self.orders = {}
    def add(self, price, shares, TransType, OrderId):
        if TransType == "B":
            if price not in self.bids:
                self.bids[price] = shares
            else:
                self.bids[price] += shares
        elif TransType == "S":
                if price not in self.asks:
                    self.asks[price] = shares
                else:
                    self.asks[price] += shares
        self.orders[OrderId] = (price, shares, TransType)
    def delete(self, OrderId):
        removed = self.orders.pop(OrderId)
        if removed[-1] == "B":
            self.bids[removed[0]] -= removed[1]
            if self.bids[removed[0]] <= 0:
                del self.bids[removed[0]]
        elif removed[-1] == "S":
            self.asks[removed[0]] -= removed[1]
            if self.asks[removed[0]] <= 0:
                del self.asks[removed[0]]