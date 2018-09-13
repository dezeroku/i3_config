import parser

import pytest

def list_group(group):
    """Used for debug displaying group content."""
    print("GROUP:")
    print("/" + group.name + "/")
    print("APPS:")
    for app in group.applications:
        print("|" + app.name + "|")
        print("|" + str(app.description) + "|")
    print("ACCEPTED")
    for app in group.accepted:
        print("|" + app.name + "|")
        print("|" + str(app.description) + "|")

def test_parse_apps_one_empty_group_incorrect_not_closed_name():
    with pytest.raises(parser.AppsGroupDoesNotExistAppAddedError):
        result = parser.parse_apps_list("test_files/one_empty_group_incorrect_not_closed_name")

def test_parse_apps_one_empty_group_incorrect_not_started_name():
    with pytest.raises(parser.AppsGroupDoesNotExistAppAddedError):
        result = parser.parse_apps_list("test_files/one_empty_group_incorrect_not_started_name")

def test_parse_apps_one_empty_group_incorrect_not_closed_group():
    with pytest.raises(parser.AppsGroupNotClosedError):
        result = parser.parse_apps_list("test_files/one_empty_group_incorrect_not_closed_group")

def test_parse_apps_one_empty_group_incorrect_group_closed_not_started():
    with pytest.raises(parser.AppsGroupClosedNotStartedError):
        result = parser.parse_apps_list("test_files/one_empty_group_incorrect_closed_not_started")

def test_parse_apps_one_empty_group_correct():
    result = parser.parse_apps_list("test_files/one_empty_group_correct")
    assert len(result) == 1
    group = result[0]

    list_group(group)

    assert group.name == "empty"
    assert not group.accepted
    assert not group.applications

def test_parse_apps_two_empty_groups_correct():
    result = parser.parse_apps_list("test_files/two_empty_groups_correct")

    assert len(result) == 2
    group_one = result[0]
    group_two = result[1]

    list_group(group_one)
    list_group(group_two)

    assert group_one.name == "empty"
    assert group_two.name == "empty2"

    assert not group_one.accepted
    assert not group_two.accepted

    assert not group_one.applications
    assert not group_two.applications

# Disabling this test enable next one to pass?
#@pytest.mark.skip()
def test_parse_apps_one_group_one_app():
    result = parser.parse_apps_list("test_files/one_group_correct_one_app")
    assert len(result) == 1
    group = result[0]

    list_group(group)

    assert group.name == "example"

    assert not group.accepted

    app = parser.App("lambda")
    assert app == group.applications[0]

def test_parse_apps_one_group_two_apps_one_description():
    result = parser.parse_apps_list("test_files/normal_apps_list_one_group")
    assert len(result) == 1
    apps_are = result[0]

    list_group(apps_are)

    assert len(apps_are.applications) == 2
    first_app = parser.App("i3")
    assert apps_are.applications[0] == first_app
    second_app = parser.App("xorg-server", "are you sure?")
    assert apps_are.applications[1] == second_app
    assert not apps_are.accepted
