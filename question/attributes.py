import sys


class QuestionAttribute(object):
    _attributes = {
        'STATUS_PASS': 1,
        'STATUS_NOT_PASS': 2,
        'KEY_STATUS': 'status',
    }

    def __getattr__(self, item: str):
        if item in self._attributes.keys():
            return self._attributes[item]

        raise TypeError('The attribute[' + item + '] not found')

    @classmethod
    def get_attributes(cls) -> dict:
        return {
            cls._attributes.get('KEY_STATUS'): {
                cls._attributes.get('STATUS_PASS'): '正常',
                cls._attributes.get('STATUS_NOT_PASS'): '未通过',
            }
        }

    @classmethod
    def get_transform(cls, key: str, default=None) -> dict:
        '''

        :param key:
        :param default:
        :return:
        '''
        if key in cls.get_attributes().keys():
            return cls.get_attributes().get(key)

        raise TypeError('The attribute[' + key + '] not found')
