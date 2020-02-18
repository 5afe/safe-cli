#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional, Type, Dict
from contract_reader import ContractReader
from web3.contract import Contract
from web3 import Web3
from contract_constants import (
    RE_ADDRESS, RE_UINT_8, RE_UINT_16, RE_UINT_32, RE_UINT_64,
    RE_UINT_128, RE_UINT_160, RE_UINT_256, RE_BYTE32, RE_BYTES,
    METHOD_ATTR_META_PATTERN
)


class ContractOperator:
    """ Contract Operator
    This function will provide dynamic access to the function  contracts using the abi
    """
    def __init__(self):
        self.name = self.__class__.__name__

    def load(self, file_path: str, contract_address: str = None) -> (Type[Contract], Dict):
        """
        :param file_path:
        :param contract_address:
        """
        try:
            web3 = Web3()
            contract_reader = ContractReader()
            contract_abi, _, _ = contract_reader.read_from(file_path=file_path)
            contract_instance = web3.eth.contract(contract_address, abi=contract_abi)
            contract_methods = self.map(contract_instance)
            return contract_instance, contract_methods
        except Exception as err:
            print(err)

    @staticmethod
    def type_pattern(attr_type: str) -> str:
        # https://ethereum.stackexchange.com/questions/49127/how-to-convert-decode-solidity-bytes32-to-python-string-via-web3-py?rq=1
        """
        :param attr_type:
        """
        if attr_type == 'address':
            return RE_ADDRESS
        elif attr_type == 'bytes':
            return RE_BYTES
        elif attr_type == 'byte32':
            return RE_BYTE32
        # from 0 to 255
        elif attr_type == 'uint8':
            return RE_UINT_8
        # from 0 to 65535
        elif attr_type == 'uint16':
            return RE_UINT_16
        # from 0 to 4294967295
        elif attr_type == 'uint32':
            return RE_UINT_32
        # from 0 to 18446744073709551615
        elif attr_type == 'uint64':
            return RE_UINT_64
        # from 0 to 340282366920938463463374607431768211455
        elif attr_type == 'uint128':
            return RE_UINT_128
        # from 0 to 1461501637330902918203684832716283019655932542975
        elif attr_type == 'uint160':
            return RE_UINT_160
        # from 0 to 115792089237316195423570985008687907853269984665640564039457584007913129639935
        elif attr_type == 'uint256':
            return RE_UINT_256

    def call(self, first_command: str, rest_command: List[str], contract: Type[Contract],
             contract_methods: Dict) -> bool:
        """
        :param first_command:
        :param rest_command:
        :param contract:
        :param contract_methods:
        """
        for method in contract_methods:
            if contract_methods[method]['name'].lower() == first_command:
                print('entry')
                try:
                    # Split data for info and sender_info, then the assert, etc etc
                    sender_info = ''
                    input_attr = ''
                    assert len(contract_methods[method]['attr']) == len(rest_command)
                    for attr in input_attr:
                        # Final Type_Validation, here?
                        print('Final Type_Validation, Here?')
                        # Contract it's used here, in the eval(), Change *rest_command for *input_attr
                        # Does not currently work, not filling properly the spots, sender_info it's not being taken
                        # into account.
                    print(contract_methods[method]['call_pattern'].format(*rest_command, sender_info))
                    # eval(contract_methods[method]['call_pattern'].format(*rest_command, sender_info))

                    print(contract_methods[method]['transact_pattern'].format(*rest_command, sender_info))
                    eval(contract_methods[method]['transact_pattern'].format(*rest_command, sender_info))
                    return True
                except AssertionError:
                    print('Not Enough Arguments')
                except Exception as err:
                    print(err)

    def transact(self, first_command: str, rest_command: List[str], contract: Type[Contract], contract_methods: Dict) -> bool:
        """
        :param first_command:
        :param rest_command:
        :param contract:
        :param contract_methods:
        """
        pass

    @staticmethod
    def new_method(method_name: str, method_attr: List[str], method_attr_meta: str,
                   method_attr_input_pattern: str, method_attr_security_pattern: str) -> Dict:
        """ To Struct Method Artifacts
        This function will return a properly structured method artifact for contract_method dictionary

        :param method_name:
        :param method_attr:
        :param method_attr_meta:
        :param method_attr_input_pattern:
        :param method_attr_security_pattern:
        :return:
        """

        # ^contract.functions.swapOwner(0x[aA-zZ,0-9]{40}|0x[aA-zZ,0-9]{62},
        # 0x[aA-zZ,0-9]{40}|0x[aA-zZ,0-9]{62} ,0x[aA-zZ,0-9]{40}|0x[aA-zZ,0-9]{62}).call()$
        # contract.functions.swapOwner(0x0000000000000000000000000000000000000000,
        # 0x0000000000000000000000000000000000000000, 0x0000000000000000000000000000000000000000).call()

        return {
            'name': method_name,
            'attr': method_attr,
            'attr_meta': METHOD_ATTR_META_PATTERN % (method_name, method_attr_meta),
            'attr_input_pattern': method_attr_input_pattern,
            'attr_security_pattern': method_attr_security_pattern,
            'eval_call_pattern': '^contract.functions.{0}('.format(method_name) +
                                 '{0}'.format(method_attr_security_pattern) + ').call({0})$',
            'eval_transact_pattern': '^contract.functions.{0}('.format(method_name) +
                                     '{0}'.format(method_attr_security_pattern) + ').transact({0})$',
            'call_pattern': 'contract.functions.{0}('.format(method_name) +
                            '{0}'.format(method_attr_input_pattern) + ').call({%s})' % len(method_attr),
            'transact_pattern': 'contract.functions.{0}('.format(method_name) +
                                '{0}'.format(method_attr_input_pattern) + ').transact({%s})' % len(method_attr),
        }

    def map(self, contract: Type[Contract]):
        """ Map Contract functions
        This function will try to map function methods, functions can be call using call & transact
        :param contract:
        :return:
        """
        contract_instance_methods = {}
        try:
            # Retrieve methods presents in the provided abi file
            for method_index, method_data in enumerate(contract.functions.__dict__['abi']):
                method_attr = []
                method_attr_meta = []
                # If current method_name, does not trigger, KeyError, try to retrieve method_attr
                # If current length for method_attr it's at least one, build up the new entry
                try:
                    method_name = method_data['name']
                except KeyError:
                    continue
                else:
                    try:
                        method_inputs = method_data['inputs']
                    except KeyError:
                        method_inputs = []

                    if len(method_inputs) >= 1:
                        attr_type = []
                        attr_meta = ''
                        attr_pattern = ''
                        security_pattern = ''
                        for index, method_attr_data in enumerate(method_inputs):
                            # attr_type: ['uint256','bytecode']
                            attr_type.append(str(method_attr_data['type']))
                            # attr_meta: 'uint256 AttrName0, bytecode AttrName1'
                            attr_meta += str(method_attr_data['type']) + ' ' + str(method_attr_data['name']) + ', '
                            attr_pattern += '{%s}, ' % index
                            security_pattern += '%s, ' % self.type_pattern(str(method_attr_data['type']))

                        contract_instance_methods[method_index] = \
                            self.new_method(method_name, attr_type, attr_meta[:-2], attr_pattern[:-2],
                                            security_pattern[:-2])

            return contract_instance_methods
        except Exception as err:
            print(type(err), err)
