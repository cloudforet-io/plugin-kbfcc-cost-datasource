import logging

from spaceone.core.error import *
from spaceone.core.manager import BaseManager
from spaceone.cost_analysis.model.data_source_model import PluginMetadata
from spaceone.cost_analysis.connector.aws_hyperbilling_connector import AWSHyperBillingConnector

_LOGGER = logging.getLogger(__name__)


class DataSourceManager(BaseManager):

    def init_response(self, options):
        self._check_options(options)

        plugin_metadata = PluginMetadata()
        plugin_metadata.validate()

        return {
            'metadata': plugin_metadata.to_primitive()
        }

    def verify_plugin(self, options, secret_data, schema):
        aws_hb_connector: AWSHyperBillingConnector = self.locator.get_connector('AWSHyperBillingConnector')
        aws_hb_connector.create_session(options, secret_data, schema)

    @staticmethod
    def _check_options(options):
        if 'accounts' in options:
            if not isinstance(options['accounts'], list):
                raise ERROR_INVALID_PARAMETER_TYPE(key='options.accounts', type='list')
        else:
            raise ERROR_REQUIRED_PARAMETER(key='options.accounts')

        if 'policy' in options:
            if not isinstance(options['policy'], dict):
                raise ERROR_INVALID_PARAMETER_TYPE(key='options.policy', type='dict')
        else:
            raise ERROR_REQUIRED_PARAMETER(key='options.policy')
