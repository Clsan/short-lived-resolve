# N = 5
# STAGES = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
STAGES = [4, 4, 4, 4, 4]

STAGE_COUNT_DICT = dict()

for stage in STAGES:
	if stage in STAGE_COUNT_DICT:
		STAGE_COUNT_DICT[stage] += 1
	else:
		STAGE_COUNT_DICT[stage] = 1

TEMP_SUM = 0
P_DICT = dict()
for i in range(N + 1, 0, -1):
	if i in STAGE_COUNT_DICT:
		TEMP_SUM += STAGE_COUNT_DICT[i]
	else:
		STAGE_COUNT_DICT[i] = 0
	if TEMP_SUM == 0:
		P_DICT[i] = 0
	else:	
		P_DICT[i] = STAGE_COUNT_DICT[i] / TEMP_SUM
#	print('{} {} {}'.format(
#		str(STAGE_COUNT_DICT[i]), 
#		str(TEMP_SUM), 
#		str(P_DICT[i])
#	))

# print(P_DICT.items())
SORTED = sorted(sorted(P_DICT.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
# print(SORTED)

RESULTS = []
for i in range(0, N + 1):
	if SORTED[i][0] != N + 1:
		RESULTS.append(SORTED[i][0])

print(RESULTS)

