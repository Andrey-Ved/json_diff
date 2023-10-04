from typing import TypedDict
from random import shuffle

from src.data import TelegramMessage


class FlatJsonItemWithId(TypedDict):
    parent_vertex_id: int | None
    child_id: list[int] | None
    name: str | None
    value: int | str | bool | None


def random_data_cut(
        json_: TelegramMessage,
        deleted_item_percentage=25,
) -> TelegramMessage:

    flat_json: dict[int, FlatJsonItemWithId] = _make_flat_with_id(json_)
    leaf_ids: list[int] = []

    for vertex in flat_json:
        if flat_json[vertex]['child_id'] is None:
            leaf_ids.append(vertex)

    shuffle(leaf_ids)
    deletions_number = len(leaf_ids) * deleted_item_percentage // 100 + 1
    deletions_ids = leaf_ids[0: deletions_number]

    for vertex in deletions_ids:
        del flat_json[vertex]

    return _make_tree(flat_json)


def _make_flat_with_id(
        json_: TelegramMessage
) -> dict[int, FlatJsonItemWithId]:

    item_counter: int = 0
    start_vertex_id: int = 0

    flat_json_with_id: dict[int, FlatJsonItemWithId] = {
        0: {
            'parent_vertex_id': None,
            'child_id': [],
            'name': None,
            'value': None,
        }
    }

    def _add_level_with_id(
            item_json: TelegramMessage,
            parent_vertex_id: int,
    ) -> None:

        nonlocal flat_json_with_id
        nonlocal item_counter

        for key in item_json:
            item_counter = item_counter + 1
            flat_json_with_id[parent_vertex_id]['child_id'].append(item_counter)

            if isinstance(item_json[key], dict):
                flat_json_with_id[item_counter] = {
                    'parent_vertex_id': parent_vertex_id,
                    'child_id': [],
                    'name': key,
                    'value': None,
                }
                _add_level_with_id(item_json[key], item_counter)
            else:
                flat_json_with_id[item_counter] = {
                    'parent_vertex_id': parent_vertex_id,
                    'child_id': None,
                    'name': key,
                    'value': item_json[key],
                }

    _add_level_with_id(json_, start_vertex_id)

    return flat_json_with_id


def _make_tree(
        flat_json_with_id: dict[int, FlatJsonItemWithId],
) -> TelegramMessage:

    prepared_json: TelegramMessage = {}
    processed_elements: set[int] = set()

    def _put_item_with_id(
            tree: TelegramMessage,
            item_id: int,
    ) -> None:

        nonlocal flat_json_with_id
        nonlocal processed_elements

        processed_elements.add(item_id)

        if item_id in flat_json_with_id:
            if flat_json_with_id[item_id]['child_id'] is None:
                tree[flat_json_with_id[item_id]['name']] = flat_json_with_id[item_id]['value']
            else:
                branch: TelegramMessage = {}

                for child_id in flat_json_with_id[item_id]['child_id']:
                    _put_item_with_id(branch, child_id)

                tree[flat_json_with_id[item_id]['name']] = branch

    for vertex_id in sorted(flat_json_with_id):
        if vertex_id not in processed_elements:
            if flat_json_with_id[vertex_id]['parent_vertex_id'] == 0:
                _put_item_with_id(prepared_json, vertex_id)

    return prepared_json
