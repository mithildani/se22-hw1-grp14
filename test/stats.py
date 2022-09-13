from app.utilities.lists import csv
from app.utilities.strings import oo

def test_stats():
    
    def div(column):
        return column.div()
    def mid(column):
        return column.mid()

    data = Data("data\\test_file.txt")
    
    print("xmid", o(data.stats(2,data.cols.x, mid)))
    print("xdiv", o(data.stats(3,data.cols.x, div)))
    print("ymid", o(data.stats(2,data.cols.y, mid)))
    print("ydiv", o(data.stats(3,data.cols.y, div)))
     
    return True


