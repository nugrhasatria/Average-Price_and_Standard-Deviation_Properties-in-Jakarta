# (Property Price) Type list data: 
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
 
 # (Average Price) Fungsi hitung_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
 
 # (Average Price - Count) Hitung nilai rata-rata dari kedua data yang dimiliki
print('Rata-rata data1:')
print(hitung_rata_rata(data1))
print('Rata-rata data2:')
print(hitung_rata_rata(data2))

 # (Property Price) Type list data: 
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
 
 # (Average Price) Fungsi hitung_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
 
 # (Standard Deviation) Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
    varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi

 # (Standard Deviation - Count) Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))

 # Data properti
tabel_properti = {
 'luas_tanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
 'luas_bangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
 'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
 'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
 }
 
 # (Average Price) Fungsi hitung_rata_rata
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
         jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
 
 # (Standard Deviation) Fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
         varians += (item - rata_rata_data) ** 2
         varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi
 
 # (Standard Deviation) & (Average Price)
 # Fungsi untuk menghitung rata-rata dan standar deviasi
 # setiap kolom pada tabel_properti yang diberikan oleh key dict.
def deskripsi_properti(tabel):
    for key in tabel.keys():
        print('Rata-rata ' + key + ':')
        print(hitung_rata_rata(tabel[key]))
        print('Standar deviasi ' + key + ':')
        print(hitung_standar_deviasi(tabel[key]))
        print('')
 
 # (Complete Data Desciption)
 # Fungsi deskripsi_properti untuk menghitung rata-rata
 # dan standar deviasi setiap kolom pada tabel_properti
deskripsi_properti(tabel_properti)


# 1: 
# Read File: "harga_rumah.txt"
file_harga_rumah = open("harga_rumah.txt", "r")
data_harga_rumah = file_harga_rumah.readlines()
file_harga_rumah.close()
# list of dict: harga_rumah
key_harga_rumah = data_harga_rumah[0].replace("\n","").split(",")
harga_rumah = []
for baris in data_harga_rumah[1:]:
	baris_harga_rumah = baris.replace("\n","").split(",")
	dict_harga_rumah = dict()
	for i in range(len(baris_harga_rumah)):
		dict_harga_rumah[key_harga_rumah[i]] = baris_harga_rumah[i]
	harga_rumah.append(dict_harga_rumah)
print(harga_rumah)

# 2:
# def get_all_specified_attribute: menerima parameter list_of_dictionary 
# (tipe data list yang berisikan sekumpulan tipe data dictionary) dan specified_key 
# (tipe data string). Fungsi akan mengembalikan sebuah list yang berisikan seluruh 
# atribut dengan kunci (key) specified_key. 
def get_all_specified_attributes(list_of_dictionary, specified_key):
	list_attributes = []
	for data in list_of_dictionary:
		attribute = data[specified_key]
		list_attributes.append(attribute)
	return list_attributes

# 3: 
# def min_value: menerima parameter list_attributes:
# (tipe data list) dan mengembalikan nilai terkecil dalam list_attributes 
def min_value(list_attributes):
	min_attribute = 9999
	for attr in list_attributes:
		if int(attr) < min_attribute:
			min_attribute = int(attr)
	return min_attribute
# def fungsi dan max_value yang menerima parameter list_attribute dan 
# mengembalikan nilai terbesar dalam list_attributes.	
def max_value(list_attributes):
	max_attribute = -9999
	for attr in list_attributes:
		if int(attr) > max_attribute:
			max_attribute = int(attr)
	return max_attribute

# 4: 
# def transform_attribute yang menerima parameter attr (sebuah 
# bilangan), max_attr (sebuah bilangan) dan min_attr (sebuah bilangan) 
# yang mengembalikan nilai transformasi dari sebuah attribute.
def transform_attribute(attr, min_attr, max_attr):
	nilai_transformasi = (attr - min_attr) / (max_attr - min_attr)
	return nilai_transformasi

# 5:
# def data_transformation yang menerima parameter list_of_dictionary 
# (sebuah list yang berisikan tipe data dictionary) dan list_attribute_names 
# (sebuah list yang berisikan tipe data string) mengembalikan hasil 
# transformasi data dari list_of_dictionary berdasarkan list_attribute_names 
# dan attr_info telah dispesifikasikan.
def data_transformation(list_of_dictionary, list_attribute_names):
	attr_info = {}
	for attr_name in list_attribute_names:
		specified_attributes = get_all_specified_attributes(list_of_dictionary, attr_name)
		max_attr = max_value(specified_attributes)
		min_attr = min_value(specified_attributes)
		attr_info[attr_name] = {'max': max_attr, 'min': min_attr}
		data_idx = 0
		while(data_idx < len(list_of_dictionary)):
			list_of_dictionary[data_idx][attr_name] = transform_attribute(int(list_of_dictionary[data_idx][attr_name]), max_attr, min_attr)
			data_idx += 1
	return list_of_dictionary, attr_info

# 6:
# (Berdasarkan data baru dan attr_info), deffungsi transform_data yang
# menerima parameter data dan attr_info dan mengembalikan nilai atribut 
# dari data baru yang telah ditransformasikan.
def transform_data(data, attr_info):
	for key_name in data.keys():
		data[key_name] = (data[key_name] - attr_info[key_name]['min']) / (
		                  attr_info[key_name]['max'] - attr_info[key_name]['min'])
	return data

# 7:
# def sistem prediksi harga berdasarkan 
# nilai kemiripan atribut, yaitu argument input data dan list_of_data!
def abs_value(value):
	if value < 0:
		return -value
	else:
		return value
def price_based_on_similarity(data, list_of_data):
	prediksi_harga = 0
	perbedaan_terkecil = 999
	for data_point in list_of_data:
		perbedaan= abs_value(data['tanah'] - data_point['tanah'])
		perbedaan+= abs_value(data['bangunan'] - data_point['bangunan'])
		perbedaan+= abs_value(data['jarak_ke_pusat'] - data_point['jarak_ke_pusat'])
		if perbedaan < perbedaan_terkecil:
			prediksi_harga = data_point['harga']
			perbedaan_terkecil = perbedaan
	return prediksi_harga

# 8:
# Hitung harga rumah yang telah ditransformasikan ke dalam variabel 
# harga_rumah berikut dengan atributnya attr_info
harga_rumah, attr_info = data_transformation(harga_rumah,
                                             ['tanah','bangunan','jarak_ke_pusat'])
# Gunakan variabel data untuk memprediksi harga rumah
data = {'tanah': 110, 'bangunan': 80, 'jarak_ke_pusat': 35}
# Transformasi data tersebut dengan dengan menggunakan attr_info yang telah 
# diperoleh yang kembali disimpan ke variabel data.
data = transform_data(data, attr_info)
# Hitung prediksi harga dari variabel data:
harga = price_based_on_similarity(data, harga_rumah)
print("Prediksi harga rumah: ", harga)