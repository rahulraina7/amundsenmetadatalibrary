from http import HTTPStatus

from metadata_service.exception import NotFoundException
from tests.unit.api.table.table_test_case import TableTestCase

TABLE_URI = 'wizards'
TAG = 'underage_wizards'


class TestTableTagAPI(TableTestCase):

    def test_should_update_tag(self) -> None:
        response = self.app.test_client().put(f'/table/{TABLE_URI}/tag/{TAG}')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.mock_proxy.add_tag.assert_called_with(table_uri=TABLE_URI, tag=TAG)

    def test_should_fail_to_update_tag_when_table_not_found(self) -> None:
        self.mock_proxy.add_tag.side_effect = NotFoundException(message='cannot find table')

        response = self.app.test_client().put(f'/table/{TABLE_URI}/tag/{TAG}')

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_should_delete_tag(self) -> None:
        response = self.app.test_client().delete(f'/table/{TABLE_URI}/tag/{TAG}')

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.mock_proxy.delete_tag.assert_called_with(table_uri=TABLE_URI, tag=TAG)

    def test_should_fail_to_delete_tag_when_table_not_found(self) -> None:
        self.mock_proxy.delete_tag.side_effect = NotFoundException(message='cannot find table')

        response = self.app.test_client().delete(f'/table/{TABLE_URI}/tag/{TAG}')

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
