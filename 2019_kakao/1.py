RECORD_STRS = [
	'Enter uid1234 Muzi', 
	'Enter uid4567 Prodo',
	'Leave uid1234',
	'Enter uid1234 Prodo',
	'Change uid4567 Ryan'
]

RESULT = [
	'Prodo님이 들어왔습니다.', 
	'Ryan님이 들어왔습니다.', 
	'Prodo님이 나갔습니다.', 
	'Prodo님이 들어왔습니다.'
]

UID_NICK_NAME_DICT = dict()

class Record:
	def __init__(self, record_str):
		inputs = record_str.split(' ')
		self.action = inputs[0]
		self.uid = inputs[1]
		self.nick_name = inputs[2] if len(inputs) == 3 else None
		if self.nick_name is not None:
			UID_NICK_NAME_DICT[self.uid] = self.nick_name	

	def build_message(self):
		if self.action == 'Enter':
			return '{}님이 들어왔습니다.'.format(UID_NICK_NAME_DICT[self.uid])
		if self.action == 'Leave':
			return '{}님이 나갔습니다.'.format(UID_NICK_NAME_DICT[self.uid])
		return None

RECORDS = []
RESULT_STRS = []

for record_str in RECORD_STRS:
	RECORDS.append(Record(record_str))

for record in RECORDS:
	processed = record.build_message()
	if processed is not None:
		RESULT_STRS.append(processed)

print(RESULT_STRS)

