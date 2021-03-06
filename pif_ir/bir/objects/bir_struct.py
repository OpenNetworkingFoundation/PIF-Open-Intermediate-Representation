import logging 
from collections import OrderedDict

from pif_ir.bir.utils.validate import check_attributes

class BIRStruct(object):
    required_attributes = ['fields']

    def __init__(self, name, struct_attrs):
        check_attributes(name, struct_attrs, BIRStruct.required_attributes)
        logging.debug("Adding bir_struct {0}".format(name))

        self.name = name
        self.length = 0
        self.fields = OrderedDict()
        self.field_offsets = OrderedDict()

        for tmp_field in struct_attrs['fields']:
            for name, size in tmp_field.items():
                self.fields[name] = size

            self.field_offsets[name] = self.length
            self.length += size

    def __len__(self):
        return self.length

    def field_offset(self, fld_name):
        return self.field_offsets.get(fld_name, 0)

    def field_size(self, fld_name):
        return self.fields.get(fld_name, 0)

