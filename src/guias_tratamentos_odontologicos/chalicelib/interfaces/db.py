import abc
import builtins
import sqlite3
from typing import (
    AbstractSet,
    Collection,
    Iterable,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union
)


class SqliteInterface(abc.ABC):

    @abc.abstractmethod
    def insert(
            self,
            *,
            table: builtins.str,
            fields_values: Mapping[
                builtins.str,
                Union[builtins.str, builtins.int]
            ]
    ) -> None:

        pass

    @staticmethod
    @abc.abstractmethod
    def _flat_dict_items(
            items: AbstractSet[
                Tuple[
                    builtins.str,
                    Union[
                        builtins.str, builtins.int]
                ]
            ]
    ) -> Tuple[
        Tuple[builtins.str, ...],
        Tuple[Union[builtins.str, builtins.int], ...]
    ]:

        pass

    @abc.abstractmethod
    def retrieve(
            self,
            *,
            table: builtins.str,
            all_: builtins.bool = False,
            field_condition: Mapping[builtins.str, Union[builtins.str, builtins.int]]
    ) -> Optional[Collection[Collection[builtins.str]]]:

        pass

    @abc.abstractmethod
    def _map_values_to_fields(
            self,
            table: builtins.str,
            *,
            values: Iterable[builtins.str]
    ) -> Collection[Collection[builtins.str]]:

        pass

    @abc.abstractmethod
    def _get_table_columns(
            self,
            table: builtins.str
    ) -> Sequence[builtins.str]:

        pass

    def close_connection(self) -> None:

        pass


class SqliteOps(SqliteInterface):

    def __init__(self, *, db: builtins.str):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def insert(
            self,
            *,
            table: builtins.str,
            fields_values: Mapping[
                builtins.str,
                Union[builtins.str, builtins.int]
            ]
    ) -> None:

        fields, values = self._flat_dict_items(fields_values.items())
        self.cursor.execute(
            f'INSERT INTO {table} {fields} VALUES {values}'
        )
        self.conn.commit()

    @staticmethod
    def _flat_dict_items(
            items: AbstractSet[
                Tuple[
                    builtins.str,
                    Union[builtins.str, builtins.int]
                ]
            ]
    ) -> Tuple[
        Tuple[builtins.str, ...],
        Tuple[Union[builtins.str, builtins.int], ...]
    ]:

        fields = []
        values = []
        for f, v in items:
            fields.append(f)
            values.append(v)

        return tuple(fields), tuple(values)

    def retrieve(
            self,
            *,
            table: builtins.str,
            all_: builtins.bool = False,
            field_condition: Mapping[builtins.str, Union[builtins.str, builtins.int]]
    ) -> Optional[Collection[Collection[builtins.str]]]:

        values = self.cursor.execute(f'SELECT * FROM {table}').fetchall()
        if values:
            if all_:
                return self._map_values_to_fields(
                    table,
                    values=values
                )

            field, value = next(iter(field_condition.items()))
            values = self.cursor.execute(
                    f'SELECT * FROM {table} WHERE {field} = "{value}"'
                ).fetchall()
            if values:
                return self._map_values_to_fields(table, values=values)

        return None

    def _map_values_to_fields(
            self,
            table: builtins.str,
            *,
            values: Iterable[builtins.str]
    ) -> Collection[Collection[builtins.str]]:

        table_columns = self._get_table_columns(table)
        mapping = []
        for value in values:
            mapping.append(dict(zip(table_columns, value)))

        self.close_connection()
        return mapping if len(mapping) > 1 else mapping.pop()

    def _get_table_columns(
            self,
            table: builtins.str
    ) -> Sequence[builtins.str]:

        return [
            fields[1] for fields in
            self.cursor.execute(f'PRAGMA table_info({table})')
        ]

    def close_connection(self) -> None:
        self.conn.close()
