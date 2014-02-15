from django import template

register = template.Library()

@register.inclusion_tag('bootstrap_field.html')
def bootstrap_field(field):
    return { 'label_id': field.id_for_label,
             'label': field.label,
             'errors': field.errors,
             'name': field.html_name,
             'type': field.field.widget.input_type,
             'value': field.value }

@register.inclusion_tag('bootstrap_form.html')
def bootstrap_form(form, submit_label):
    return { 'form': form,
             'submit_label': submit_label }

@register.inclusion_tag('bootstrap_multipart_form.html')
def bootstrap_multipart_form(form, submit_label):
    return { 'form': form,
             'submit_label': submit_label }
