from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    new_group = Group(name="New group")
    new_group.id = group.id
    app.group.edit_group_by_id(new_group.id, new_group)
    new_groups = db.get_group_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups[0:2], key=Group.id_or_max) == sorted(app.group.get_group_list()[0:2], key=Group.id_or_max)

#def test_edit_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create_group(Group(header="test"))
   # old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
