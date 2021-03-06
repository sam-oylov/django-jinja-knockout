from copy import deepcopy

from .. import tpl

from .base import BaseFilter


class RangeFilter(BaseFilter):
    component_class = 'App.RangeFilter'
    input_type = 'search'
    template = 'bs_range_filter.htm'
    from_field_lookup = 'gte'
    to_field_lookup = 'lte'

    def __init__(self, view, fieldname, vm_filter, request_list_filter=None):
        super().__init__(view, fieldname, vm_filter, request_list_filter)
        data_component_options = {
            'fieldName': self.fieldname,
        }
        if self.view.filter_key != 'list_filter':
            data_component_options['filterKey'] = self.view.filter_key
        if self.from_field_lookup != 'gte':
            data_component_options['fromFieldLookup'] = self.from_field_lookup
        if self.to_field_lookup != 'lte':
            data_component_options['toFieldLookup'] = self.to_field_lookup
        self.component_attrs = {
            'class': 'component',
            'data-component-options': data_component_options,
        }
        self.input_attrs = {
            'class': 'form-control',
            'type': self.input_type,
        }

    def get_template_kwargs(self):
        template_kwargs = super().get_template_kwargs()
        curr_list_filter = self.get_request_list_filter()
        apply_url_query = deepcopy(curr_list_filter)
        self.component_attrs['data-component-class'] = self.get_component_class()
        collapse_class = 'collapse'
        from_input_attrs = deepcopy(self.input_attrs)
        to_input_attrs = deepcopy(self.input_attrs)
        tpl.add_css_classes_to_dict(from_input_attrs, 'input-from')
        tpl.add_css_classes_to_dict(to_input_attrs, 'input-to')
        if self.fieldname in curr_list_filter:
            field_filter = curr_list_filter[self.fieldname]
            if self.from_field_lookup in field_filter:
                from_input_attrs['value'] = field_filter[self.from_field_lookup]
                collapse_class += ' in'
            if self.to_field_lookup in field_filter:
                to_input_attrs['value'] = field_filter[self.to_field_lookup]
                if not collapse_class.endswith(' in'):
                    collapse_class += ' in'
            del curr_list_filter[self.fieldname]
        reset_url_query = deepcopy(curr_list_filter)
        template_kwargs.update({
            'component_attrs': self.component_attrs,
            'collapse_class': collapse_class,
            'from_input_attrs': from_input_attrs,
            'to_input_attrs': to_input_attrs,
            'errors': self.view.get_filter_errors(self.fieldname),
            'apply_url_query': apply_url_query,
            'reset_url_query': reset_url_query,
        })
        return template_kwargs


class DateFilter(RangeFilter):
    input_class = 'date-control'

    def get_template_kwargs(self):
        template_kwargs = super().get_template_kwargs()
        tpl.add_css_classes_to_dict(template_kwargs['from_input_attrs'], self.input_class)
        tpl.add_css_classes_to_dict(template_kwargs['to_input_attrs'], self.input_class)
        return template_kwargs


class DateTimeFilter(DateFilter):
    input_class = 'datetime-control'
