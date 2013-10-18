import csv
import json
business=[]
b_data=open('Data/yelp_training_set_business.json','rw')

for line in b_data:
	
	uline = unicode(line, 'latin-1')
	business.append(json.loads(uline))

#full_data=json.loads(b_data.readlines())
csv_file=csv.writer(open('business_train.csv','w+'))
csv_file.writerow(["business_id",'full_address','open','categories','review_count','name','neighborhoods','longitude','state','stars','latitude','type'])

for item in business:
	csv_file.writerow([item['business_id'],item['full_address'].encode('utf-8'),item['open'],item['categories'],item['review_count'],(item['name']).encode('utf-8'),item['neighborhoods'],item['longitude'],item['state'],item['stars'],item['latitude'],item['type']])
