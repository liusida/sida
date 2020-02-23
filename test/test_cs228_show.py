import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"src"))
import sida.cs228.show as show
import pickle

def test_show():
    with open("test/test_data/Liu_train2_std.p", "rb") as f:
        data = pickle.load(f)
    show.show_hand(data[:,:,:,0], view_point="front", scale="unit", fname="test/test_data/Liu_train2_std_front.png")
    show.show_hand(data[:,:,:,0], view_point="side", scale="unit", fname="test/test_data/Liu_train2_std_side.png")

if __name__ == "__main__":
    test_show()