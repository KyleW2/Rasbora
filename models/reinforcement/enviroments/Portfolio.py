class Portfolio:
    def __init__(self) -> None:
        self.positions = {}

    def buy(self, price: float, volume: int) -> None:
        if price in self.positions.keys():
            self.positions[price] += volume
        else:
            self.positions[price] = volume

    def sell(self, price: float, volume: int) -> bool:
        if price in self.positions.keys():
            if self.positions[price] >= volume:
                self.positions[price] -= volume
                return True
            else:
                return False
        return False
    
    def points(self, current_price: float) -> float:
        sum = 0
        for i in self.positions.values():
            sum += i
        if sum == 0:
            return 0
            
        sum = 0
        change = 0
        for i in self.positions.keys():
            sum += self.positions[i]
            change += ((current_price - i) / i)
        
        return 10 * (change / sum)
    
    def value(self) -> float:
        v = 0
        for i in self.positions.keys():
            v += self.positions[i] * i
        
        return v
    
    def holding(self) -> int:
        holding = 0

        for h in self.positions.values():
            holding += h

        return holding

    def dump(self) -> float:
        v = 0
        for i in self.positions.keys():
            v += self.positions[i] * i
            self.positions[i] = 0
        
        return v

if __name__ == "__main__":
    p = Portfolio()
    p.buy(10, 1)
    p.buy(11, 1)
    print(p.positions)
    print(p.points(15))