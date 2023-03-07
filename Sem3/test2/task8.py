ALLOWED_SIGNS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


class Record:
    def __init__(self, record_id, mimoid_id, timestamp, length, width, height_max, height_avg, mounds, color, age):
        self.record_id = record_id
        self.mimoid_id = mimoid_id
        self.timestamp = timestamp
        self.length = length
        self.width = width
        self.height_max = height_max
        self.height_avg = height_avg
        self.mounds = mounds
        self.color = color
        self.age = age


N = int(input())

records = []

for i in range(N):
    i_str = input().split()
    records.append(Record(int(i_str[0]),
                          int(i_str[1]),
                          int(i_str[2]),
                          float(i_str[3]),
                          float(i_str[4]),
                          float(i_str[5]),
                          float(i_str[6]),
                          int(i_str[7]),
                          i_str[8],
                          int(i_str[9])))

records.sort(key=lambda x: x.timestamp)

records = [record for record in records if all(sign in ALLOWED_SIGNS for sign in record.color) and len(record.color) <= 6]

first_records = []

for record in records:
    if next((x for x in first_records if x.mimoid_id == record.mimoid_id), None) is None:
        first_records.append(record)

records = [record for record in records if (record.timestamp - next((x for x in first_records if x.mimoid_id == record.mimoid_id), None).timestamp == record.age - next((x for x in first_records if x.mimoid_id == record.mimoid_id), None).age) and record.length <= next((x for x in first_records if x.mimoid_id == record.mimoid_id), None).length and record.width <= next((x for x in first_records if x.mimoid_id == record.mimoid_id), None).width]

for record in records:
    print(record.record_id, end=' ')
