import sys
import joblib
import json  # Tambahkan library JSON

# Mengimport model
model = joblib.load('/home/makmalluddin/Documents/projekstupen/Stupen/LastProject/model_rf.pkl')
encoder = joblib.load('/home/makmalluddin/Documents/projekstupen/Stupen/LastProject/label_encoder.pkl')

# Membuat variabel inputpy
type = encoder['Type'].transform([str(sys.argv[1])])
benefit_per_order = float(sys.argv[2])
sales_per_customer = float(sys.argv[3])
latitude = float(sys.argv[4])
longitude = float(sys.argv[5])
shipping_mode = encoder['Shipping Mode'].transform([str(sys.argv[6])])
order_status = int(sys.argv[7])
order_region = encoder['Order Region'].transform([str(sys.argv[8])])
order_country = encoder['Order Country'].transform([str(sys.argv[9])])
order_city = encoder['Order City'].transform([str(sys.argv[10])])
market = encoder['Market'].transform([str(sys.argv[11])])
delivery_status = encoder['Delivery Status'].transform([str(sys.argv[12])])
order_day = int(sys.argv[13])
order_month = int(sys.argv[14])
order_year = int(sys.argv[15])
shipping_day = int(sys.argv[16])
shipping_month = int(sys.argv[17])
shipping_year = int(sys.argv[18])

# Melakukan prediksi
predict = model.predict([[type[0], benefit_per_order, sales_per_customer, latitude, longitude,
                          shipping_mode[0], order_status, order_region[0], order_country[0], order_city[0],
                          market[0], delivery_status[0], order_day, order_month, order_year,
                          shipping_day, shipping_month, shipping_year]])


# Format hasil prediksi dalam JSON
output = {
    "tercepat": predict[0][0],
    "normal": predict[0][1]
}

# Cetak output dalam format JSON
print(json.dumps(output))