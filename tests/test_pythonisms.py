from pythonisms import __version__


def test_version():
    assert __version__ == '0.1.0'



from pythonisms import __version__

from pythonisms.linkedList import Node,LinkedList

def test_length():
    l = LinkedList(['G', 'H', 'F', 'R', 'I'])
    expected = 5
    actual = len(l)
    assert expected == actual

    
def test_equality():
    one = LinkedList(['q', 'q', 'q', 'q'])
    two = LinkedList(['q', 'q', 'q', 'q', 'q'])

    assert (one == two) == False

    

def test_str():
    l = LinkedList(['t', 'e', 's', 't'])

    assert l.__str__() == '[ t ] -> [ e ] -> [ s ] -> [ t ] -> None'

def test_get_item():

    l = LinkedList(['G', 'H', 'F', 'R', 'I'])
    assert l[0] == 'G'
    assert l[1] == 'H'
    assert l[2] == 'F'
    assert l[3] == 'R'
    assert l[4] == 'I'
