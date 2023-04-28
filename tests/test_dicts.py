from utils import dicts

def test_val():
    collection = {"specie": "Beluga", "water": "fresh"}
    assert dicts.get_val(collection, "specie") == 'Beluga'
    assert dicts.get_val(collection, "water", "git") == 'fresh'
    assert dicts.get_val(collection, "wat", "git") == 'git'
    assert dicts.get_val({}, "specie", "git") == 'git'
    assert dicts.get_val({}, "water", "specie") == 'specie'
