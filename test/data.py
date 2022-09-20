from app.utilities.strings import oo
from app.objects.data import Data

def test_data():
    d = Data("data\\test_file.txt")
    for col in d.cols.y:
        oo(col)
    return True