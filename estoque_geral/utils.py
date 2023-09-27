from datetime import date, datetime, timedelta, timezone


def default_message_request(status_code=None, msg=None):
	default_message = {
		200: 'OK',
		201: 'Criado com sucesso.',
		202: 'Aceito',
		204: 'Deletado.',
		400: 'Ops, ocorreu um problema. Revise seus dados!',
		401: 'Ops, não autorizado.',
		403: 'Ops, negação no acesso.',
		404: 'Informação não encontrada.',
		405: 'Operação desconhecida.',
		409: 'Ops, conflito das informações.',
		412: 'Ops, pré-condições não atendidas.',
		500: 'Ops, ocorreu um problema na operação.'
	}

	if msg:
		return {'message': msg}

	return {'message': default_message.get(status_code)}

def check_list_len(list_field=None):
	if len(list_field) > 0:
		return True
	return False

def convert_str_upper_or_low(type_convert=None, value=None):
	str_formatted = ''
	if value:
		if type_convert == 'up':
			str_formatted = str(value).upper()
		elif type_convert == 'low':
			str_formatted = str(value).lower()
	return str_formatted

def show_message_errors(description_field=None, max_length_field=None, max_digit_field=None, max_decimal_place=None):
	dict_messages = {
		'error_messages': {
			'required': 'O campo {} é obrigatório.'.format(description_field),
			'null': 'O campo {} não pode ser nulo.'.format(description_field),
			'blank': 'O campo {} não pode estar em branco.'.format(description_field),
			'does_not_exist': 'O campo {} possui um valor inválido.'.format(description_field),
			'incorrect_type': 'O campo {} possui um tipo incorreto de dado.'.format(description_field),
			'invalid': 'O campo {} possui um valor inválido.'.format(description_field)
		}
	}

	if max_length_field:
		dict_messages['error_messages']['max_length'] = 'O campo {} não pode ter mais que {} caracteres.'.format(description_field, max_length_field)

	if max_digit_field:
		dict_messages['error_messages']['max_digits'] = 'O campo {} não pode ter mais que {} dígitos.'.format(description_field, max_digit_field)

	if max_decimal_place:
		dict_messages['error_messages']['max_decimal_places'] = 'O campo {} não pode ter mais que {} casas decimais.'.format(description_field, max_decimal_place)

	return dict_messages

def show_message_to_unique_error(description_field=None):
	return {'unique': 'O campo {} é único e já existe no banco de dados.'.format(description_field)}

def get_label_to_boolean_field(value_field=None):
	str_formatted = {
		True: 'SIM',
		False: 'NÃO',
		'true': 'SIM',
		'false': 'NÃO',
		None: None
	}
	return str_formatted.get(value_field)

def check_filtered_params_exists(params=None, filters=None, filtered=None):
	if is_empty_dict_params(params) or len([i for i in list(params.keys()) if i in filters]) == 0:
		return []
	return filtered

def is_empty_dict_params(dict_params=None):
	if not dict_params:
		return True
	else:
		for value in dict_params.values():
			if not value:
				return True
		return False

def mount_list_ids(array_obj=None):
	lst_ids = []
	for item in array_obj:
		lst_ids.append(item.get('id'))
	return lst_ids

def remove_elements_equals_in_list(list_to_change=None):
	if list_to_change:
		return list(set(list_to_change))
	return list_to_change

def data_mapping_to_serializer(pkey=None, validated_data=None):
	return {item[pkey]: item for item in validated_data}

def data_perform_update(self=None, instance=None, data_mapping=None):
	ret = []
	for obj_id, data in data_mapping.items():
		obj = instance.get(obj_id, None)
		if obj is not None:
			ret.append(self.child.update(obj, data))
	return ret

def get_type_date(type_datetime=None):
	types_datetime = {
		'datetime': datetime.now(),
		'date': datetime.now().date(),
		'time': datetime.now().time(),
		'datetime-utc': datetime.now(timezone.utc)
	}

	return types_datetime.get(type_datetime)

def convert_date(value_date=None, format_date=None, convert_twice=None):
	new_value = None
	if value_date:
		if type(value_date) is str:
			if format_date and not convert_twice:
				new_value = datetime.strptime(value_date, format_date)
			else:
				new_value = datetime.strptime(value_date, '%Y-%m-%d')
			if convert_twice:
				new_value = new_value.strftime(format_date)

		else:
			new_value = value_date.strftime(format_date)

	return new_value