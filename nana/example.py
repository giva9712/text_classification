from stemmer import Nana

text = "Андройд төхөөрөмжүүдэд эзнийг нь мэдээгүй байхад нэвтрэн мэдээлэл хулгайлах боломжтой цоорхой илэрснийг судлаачид өчигдөр зарлалаа.\nЭнэ.\nАндройдын өөрийнх нь Stagefright нэртэй медиа санд энэхүү цоорхой байгаа гэнэ.\nZimperium компани ирэх сард болох Black Hat 2015 чуулган дээр өөрсдийн илрүүлсэн алдааны талаар дэлгэрэнгүй мэдээлнэ гэлээ.\nХакерууд энэ цоорхойг ашиглахдаа тухайн хүний утасны дугаарыг мэдэж байхад хангалттай.\nХэрэглэгчийн дугаарт ямар нэг медиа файлыг MMS ашиглан илгээхэд л нэвтрэх боломжтой болдог аж.\nХамгийн аюултай нь ингэж байхад хэрэглэгчид юу ч мэдэгдэхгүй. Нэгэнт нэвтэрсэн хойно хакер тухайн утасны микрофоныг ажиллуулах, файл хулгайлах, имэйлийг нь унших зэрэг үйлдэл хийж чадна.\nЖишээ нь хэрэглэгч унтаж байхад утсанд нь нэвтрээд өөрийн програмыг суулгасны дараа мөрөө баллах боломжтой. Хэрэглэгч энэ бүгдийг огт мэдэхгүй, өглөө нь босоод утсаа үргэлжлүүлэн ашиглаад явах юм.\nҮүний эсрэг авах арга хэмжээ нь хэрэглэгч өөрийн телеком оператор эсвэл гар утас борлуулагчид хандан үйлдлийн системээ шинэчлэх.\nӨчигдөр Google компаниас мэдэгдэл гаргаж энэ цоорхойг нөхөх програмын шинэчлэлтийг гаргаж гар утас үйлдвэрлэгч нартаа хүргэсэн талаар мэдээлжээ.\n \nЭх сурвалж:Venturebeat.com"

nana = Nana()

parsed = nana.parse(text)

print(parsed)