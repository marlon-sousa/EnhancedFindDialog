# NVDA için Gelişmiş Ara İletişim Kutusu ${addon_version}
NVDA için arama işlevini geliştiren gelişmiş ara iletişim kutusu eklentisi:  

* arama geçmişi.  
* arama kaydırma, profil başına yapılandırılmış.  
* büyük/küçük harf duyarlılığı, profil başına yapılandırılmış.  
* aramalarla ilgili bağlamsal bilgiler.  

## İndirme:  
[Gelişmiş Ara İletişim Kutusu ${addon_version} eklentisini indirin](https://github.com/marlon-sousa/EnhancedFindDialog/releases/download/${addon_version}/EnhancedFindDialog-${addon_version}.nvda-addon)

## Özellikler:  

### Arama geçmişi:  
Birçok web sitesinde ve web uygulamasında, belirli yerlere erişmenin en hızlı yolu, genellikle ctrl + nvda + f tuşlarına bağlı olan arama komutunu kullanmaktır.  

Arama iletişim kutusu, bir metin yazmamıza ve bulunursa o metnin sonraki örneğine erişmemize olanak tanır.

Çoğu durumda, tek NVDA oturumu sırasında aynı web sitelerini birkaç kez ziyaret ettiğinizi göreceksiniz. Bu web sitelerinin birçoğunda, özellikle o web sitesinin bir bağlantısına veya bölümüne hızlı bir şekilde ulaşmanın tek yolu buysa, aynı terimleri aramanız gerekecektir.  

Bu, özellikle işlerinin bir gereği olarak web tabanlı sistemlerle günlük olarak çalışan kişiler için geçerlidir.  

Ancak NVDA, daha önce aradığınız terimleri bir listede tutmaz. Bu, üretkenliğinizi yavaşlatır, çünkü son aramanızın tam olarak aynı terimini aramadığınız sürece, tekrar yazmanız gerekir.  

Bu eklenti, NVDA çalıştığı sürece devam eden bir arama geçmişi tutar. Bu nedenle, aktivasyonda, yeni bir arama yapmak için aşağı oka basmanız ve daha önce aranan terimleri seçmeniz yeterlidir.  

Elbette yeni terimler yazabilirsiniz. Ayrıca, arama iletişim kutusunu bir sonraki etkinleştirdiğinizde listeye eklenecektir.  

#### Nasıl çalışır?  

Eklentiyi kurmanız yeterlidir. Etkinleştirildiğinde, arama iletişim kutusundaki düzenleme alanında aşağı ve yukarı oklara basmak, daha önce aranan terimler listesinde gezinmenizi sağlar.  

Her zaman olduğu gibi istediğiniz zaman yeni bir terim yazabilirsiniz.  

### Arama Kaydırma:  

Arama kaydırma yapılandırılmışsa, arama yaparken bir metin üzerinde bulunduğunuz geçerli konumu dikkate almayan bir özelliktir.  

Bu, mevcut konumunuzun altında olmayan bir şey ararsanız, bu terimin tüm metinde bir yerde olup olmadığını kontrol etmek için metnin başından itibaren arama yapılacağı anlamına gelir.  

Bu, web tabanlı sistemlerle çalışan ve sayfanın neresinde olurlarsa olsunlar belirli bir düğmeyi veya metin parçasını bulması gereken kişiler için özellikle önemlidir.  

Bu seçenek profile özeldir, yani etkin olduğu yerde bir profiliniz olabilir ve olmadığı yerde başka bir profiliniz olabilir.  

#### Nasıl çalışır?  

Eklentiyi kurmanız yeterlidir. Etkinleştirildiğinde, bul iletişim kutusu arama kaydır adı verilen bir onay kutusu sunacaktır.  

Kontrol edilirse:  

1. Bir terim ararsanız ve mevcut konumun altında bulunursa, o metnin üzerine odaklanırsınız.  
2. Bu terim mevcut pozisyonun altında bulunamazsa, metnin üstünden aranacaktır.  
3. Terim bulunursa, bulunan metnin mevcut konumunuzun üzerinde olduğunu ve yerine yerleştirildiğinizi bildirmek için kısa bir bip sesi duyulur.  
4. Bu terim hiç bulunamazsa, metin bulunamadı mesajı görüntülenir.  

Bu onay kutusunu değiştirmek ve bir arama yapmak, aktif profil için yeni durumu (işaretli veya işaretsiz) kaydeder. Aramayı iptal etmeden önce değiştirmiş olsanız bile, aramayı iptal etmek etkin profildeki durumunu değiştirmez.  

### büyük küçük harf duyarlılığı:  

NVDA, büyük/küçük harfe duyarlı aramalara izin vermek için büyük/küçük harf duyarlılığı onay kutusunu zaten sunuyor. Bu eklenti, bu onay kutusunun durumunu etkin profilde kaydederek bu işlevi genişletir, böylece farklı şekilde yapılandırılmış profillere sahip olabilirsiniz.  

#### Nasıl çalışır?  

Eklentiyi kurmanız yeterlidir. Büyük/küçük harf duyarlılığı onay kutusunun değiştirilmesi ve bir arama yapılması, etkin profil için yeni durumu (işaretli veya işaretsiz) kaydeder. Aramayı iptal etmeden önce değiştirmiş olsanız bile, aramayı iptal etmek etkin profildeki durumunu değiştirmez.  

### aramalarla ilgili bağlamsal bilgiler:  

Bir arama terimi bulunduğunda NVDA'nın davranış şekli şu şekildedir: aranan terimin konumuna yerleştirilirsiniz ve satır, aranan terimden itibaren okunur.  

Bir şey için birkaç kez (NVDA + f3 kullanarak) arama yapmanız gerektiğinde bu her zaman sorunlu olmuştur, çünkü dinlediğiniz ilk şey aranan terimin kendisidir, o terimi sadece aradığınız için bildiğiniz zaman.  

Bu eklenti, imleci terimin konumuna yerleştirir, ancak üzerindeki terimden okumak yerine tam satırı okur ve size o terimin bulunduğu bağlamı gösterir.  

Örneğin, "Marlon" kelimesini aradığınızı, çünkü Marlon'u bir yerde hedefle adlı bir düğme olduğunu bildiğinizi varsayalım. Hedef aramak istemiyorsunuz çünkü "target x y z" adında başka butonlar var ve Marlon Button hedefi bulmak istiyorsunuz.

İşte metin:  

Marlon yorumlarını sil  

doğrudan Marlon'a cevap ver  

Marlon'u spam gönderici olarak bildir  

Bir yanıtta Marlon'u hedefle  

Bu bloktan önce Marlon'u ararsanız, şunu duyardınız:
Marlon Yorumları  

NVDA + f3'e basmaya devam ederseniz şunu duyarsınız:  

marlon  

Marlon as spammer

Marlon on a response

Bu, üretkenliğinizi azaltır çünkü ilk önce bu oluşum hakkında hiçbir şey bilmeden sadece marlon duyarsınız.  

Bir dahaki sefere, Marlon'u duyacaksınız ve spam gönderici olarak konuşulmasını beklemek zorunda kalacaksınız, çünkü bu metinde Marlon hakkında ne olduğunu da bilemezsiniz.  

Benzer şekilde, bir dahaki sefere söylenecek bir yanıtı beklemeniz gerekecekti çünkü Marlon'la ilgili bu şeyin ne olduğundan da emin olmayacaktınız.  

Üstelik NVDA + f3'e hızlı basarsanız, Marlon, Marlon, Marlon, Marlon'u duyardınız... Çok üretken olmayan cinse Marlon aradığınızı bilirsiniz.  

#### Nasıl çalışır?  

Eklentiyi kurmanız yeterlidir.

Kurulduktan sonra, bulunan arama teriminin mevcut satırı okunur ve üzerindeki terime yerleştirilirsiniz.  

Yukarıdaki örneğimizde, aramayı ilk yaptığınızda duyacağınız.  

Marlon yorumlarını sil  

NVDA + f3'e basmaya devam ederseniz şunu duyarsınız:  

doğrudan Marlon'a cevap ver  

Marlon'u spam gönderici olarak bildir  

Bir yanıtta Marlon'u hedefle  

Ayrıca, NVDA + f3'e hızlı bir şekilde basarsanız, her satırın başlangıcını duyarsınız, bu da hedef satırda hızlı bir şekilde enter'a basmanıza olanak tanır çünkü Marlon'un aynı satırda daha sonraki bir konumda bulunduğunu bilirsiniz.  

## Katkıda bulunmak ve tercüme etmek:  

Bu eklentiye katkıda bulunmak veya bu eklentiyi çevirmek istiyorsanız, lütfen [proje deposuna](https://github.com/marlon-sousa/EnhancedFindDialog) erişin ve İngilizce dokümantasyon dizininde Contribute.md ile ilgili talimatları bulun.  

## Katkıda Bulunanlar.  

Özel teşekkür:  


* Angelo Miguel Abrantes - Portekizce çeviri  
* Rémy Ruiz - Fransızca çeviri
* Rémy Ruiz - İspanyolca çeviri  
* Tarik Hadžirović - Hırvatça çeviri
*  Thiago Seus - Brezilya Portekizcesi çeviri  
* Umut KORKMAZ - Türkçe Çeviri  
* Valentin Kupriyanov - Rusça çeviri  
