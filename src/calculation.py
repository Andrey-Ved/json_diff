from typing import TypedDict

from src.data import TelegramMessage


AssemblyKey = tuple[str, ...]


class FlatJsonItemWithKey(TypedDict):
    children_key: set[AssemblyKey] | None
    value: int | str | bool | None


FlatJsonWithKey = dict[AssemblyKey, FlatJsonItemWithKey]


def find_diff(
        original_json: TelegramMessage,
        other_json: TelegramMessage
) -> TelegramMessage:

    flat_original_json: FlatJsonWithKey = _make_flat_with_key(original_json)
    flat_other_json: FlatJsonWithKey = _make_flat_with_key(other_json)

    def _diff(
            j1: FlatJsonWithKey,
            j2: FlatJsonWithKey,
            prefix: str
    ) -> None:

        nonlocal flat_diff_json

        for key in j2:
            new_key: AssemblyKey = key[:-1] + (str(prefix + key[-1]),)

            if key not in j1 or j1[key]['value'] != j2[key]['value']:
                flat_diff_json[new_key] = j2[key]['value']

    flat_diff_json: dict[AssemblyKey, int | str | bool | None] = {}

    _diff(flat_other_json, flat_original_json, '- ')
    _diff(flat_original_json, flat_other_json, '+ ')

    return _make_tree(flat_diff_json)


def _make_flat_with_key(
        json_: TelegramMessage
) -> FlatJsonWithKey:

    def _add_level_with_key(
            item_json: TelegramMessage,
            parent_vertex_key: AssemblyKey
    ) -> None:

        nonlocal flat_json_with_key

        for key in item_json:
            current_key: AssemblyKey = parent_vertex_key + (key,)
            flat_json_with_key[parent_vertex_key]['children_key'].add(current_key)

            if isinstance(item_json[key], dict):
                flat_json_with_key[current_key] = {
                    'children_key': set(),
                    'value': None,
                }
                _add_level_with_key(item_json[key], current_key)
            else:
                flat_json_with_key[current_key] = {
                    'children_key': set(),
                    'value': item_json[key],
                }

    start_vertex_key: AssemblyKey = ('0',)

    flat_json_with_key: FlatJsonWithKey = {
        ('0',): {
            'children_key': set(),
            'value': None,
        }
    }

    _add_level_with_key(json_, start_vertex_key)

    return flat_json_with_key


def _make_tree(
        flat_j: dict[AssemblyKey, int | str | bool | None]
) -> TelegramMessage:

    tree_j: TelegramMessage = {}

    for assembly_key in flat_j:
        branch: TelegramMessage = tree_j

        for key in assembly_key[1:-1]:
            if key not in branch:
                branch[key] = {}

            branch = branch[key]

        branch[assembly_key[-1]] = flat_j[assembly_key]

    return tree_j
