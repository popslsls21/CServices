# CService - نظام إدارة خدمات السيارات

## نظرة عامة
CService هو نظام شامل لإدارة خدمات صيانة السيارات بمميزات متقدمة. يتيح للمستخدمين:
- إدارة بيانات السيارات والمواعيد
- تحديد مراكز الصيانة القريبة
- مراقبة صحة السيارة والتشخيص الذكي
- روبوت محادثة ذكي للمساعدة بالعربية والإنجليزية

## المميزات الرئيسية
- نظام تسجيل وإدارة حسابات المستخدمين
- واجهة مستخدم متجاوبة لأجهزة الموبايل
- خرائط تفاعلية لمراكز الصيانة
- تشخيص أعطال السيارات باستخدام الذكاء الاصطناعي
- إمكانية حجز مواعيد الصيانة إلكترونياً

## متطلبات النظام
- Python 3.11+
- PostgreSQL
- المكتبات المطلوبة (مدرجة في ملف requirements.txt)

## تثبيت وتشغيل المشروع

### 1. استنساخ المشروع
```bash
git clone https://github.com/your-username/cservice.git
cd cservice
```

### 2. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 3. إعداد قاعدة البيانات
```bash
export DATABASE_URL="postgresql://username:password@localhost:5432/cservice"
cd car_service
python init_database.py
python seed_database.py
```

### 4. تشغيل التطبيق
```bash
cd car_service
python app.py
```

ستكون واجهة التطبيق متاحة على الرابط: http://localhost:8080

## تشغيل واجهة لوحة التحكم
```bash
streamlit run app.py
```

## هيكل المشروع
- `car_service/`: التطبيق الرئيسي بتقنية Flask
- `app.py`: واجهة إدارة البيانات بتقنية Streamlit
- `pages/`: صفحات لوحة التحكم

## المساهمة في المشروع
نرحب بمساهماتكم! يمكنكم فتح issue جديد أو إرسال pull request.

## الرخصة
هذا المشروع تحت رخصة MIT.