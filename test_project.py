from project import loaddiction, addaword, remaword
import json
from unittest.mock import patch, mock_open
import pytest


def main():
    test_addaword()
    test_addaword2()
    test_remaword()
    test_remaword2()

def test_addaword():
    di = {}
    with patch("builtins.input", side_effect=["newword", "newdefinition"]), patch("builtins.open", mock_open(read_data=json.dumps("di"))) as mock_file:
        addaword(di)
        assert di == {"newword" : "newdefinition"}


def test_addaword2():
    di = {"newword" : "newdefinition"}
    with patch("builtins.input", side_effect=["newword", "exitf"]), patch("builtins.print") as mock_print:
        addaword(di)
        mock_print.assert_called_once_with("newword already exists in the dictionary.")

def test_remaword():
    di = {"newword" : "newdefinition"}
    with patch("builtins.input", return_value="newword"), patch("builtins.open", mock_open(read_data=json.dumps("di"))) as mock_file:
        remaword(di)
        assert di == {}

def test_remaword2():
    di = {}
    with patch("builtins.input", side_effect=["newword", "exitf"]), patch("builtins.print") as mock_print:
        remaword(di)
        mock_print.assert_called_once_with("The word has not been found.")

def test_loaddiction():
    mydi = {"word":"definition"}
    with patch("builtins.open", mock_open(read_data=json.dumps(mydi))) as mock_file:
        assert loaddiction() == mydi



if __name__ == "__main__":
    main()

