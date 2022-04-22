"""
Reused parsing class, probably will be replaced
"""

class CSVParser:
    def __init__(self, file: str) -> None:
        self.file = file
        self.table = self.parse()

    def parse(self) -> list:
        table = []

        f = open(self.file, "r")
        rows = f.read().splitlines()
        f.close()

        for i in range(0, len(rows)):
            table.append(rows[i].split(","))
        
        return table
    
    def getTable(self) -> list:
        return self.table
    
    def getColumnTitles(self) -> list:
        return self.table[0]
    
    def getColumn(self, title: str) -> list:
        column = []

        for i in range(0, len(self.table[0])):
            if self.table[0][i] == title:
                for j in range(1, len(self.table)):
                    column.append(self.table[j][i])
                
                return column
        
        return None
    
    def getColumnAsFloats(self, title: str) -> list:
        column = []

        for i in range(0, len(self.table[0])):
            if self.table[0][i] == title:
                for j in range(1, len(self.table)):
                    column.append(float(self.table[j][i]))
                
                return column
        
        return None