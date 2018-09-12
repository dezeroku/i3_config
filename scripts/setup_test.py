import setup

def test_parse_apps_list_normal():
    result = setup.parse_apps_list("test_files/normal_apps_list_one_group")
    apps_are = result[0]

    for app in apps_are.applications:
        print("|"+app.name+"|")
        print("|"+str(app.description) + "|")

    assert len(apps_are.applications) == 3
    first_app = setup.App("i3")
    assert apps_are.applications[0] == first_app
    second_app = setup.App("xorg")
    assert apps_are.applications[1] == second_app
    third_app = setup.App("xorg-server", "are you sure?")
    assert apps_are.applications[2] == third_app
