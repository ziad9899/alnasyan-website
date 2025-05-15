<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>شركة النصيان القابضة</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <a href="index.html"><img src="img/logo.jpeg" alt="شعار شركة النصيان القابضة" style="height: 50px;"></a>
      </div>
      <nav>
        <button class="menu-toggle" aria-label="القائمة" onclick="toggleSidebar()">
          <span></span><span></span><span></span>
        </button>
        <ul class="nav-menu">
          <li><a href="about.html">عن الشركة</a></li>
          <li><a href="companies.html">شركاتنا</a></li>
          <li><a href="sustainability.html">الاستدامة</a></li>
          <li><a href="media.html">المركز الإعلامي</a></li>
          <li><a href="contact.html">اتصل بنا</a></li>
          <li><a href="careers.html">الوظائف</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <div class="sidebar" id="sidebar">
    <button class="close-sidebar" onclick="toggleSidebar()">×</button>
    <ul>
      <li><a href="index.html">الرئيسية</a></li>
      <li><a href="about.html">عن الشركة</a></li>
      <li><a href="companies.html">شركاتنا</a></li>
      <li><a href="sustainability.html">الاستدامة</a></li>
      <li><a href="media.html">المركز الإعلامي</a></li>
      <li><a href="contact.html">اتصل بنا</a></li>
      <li><a href="careers.html">الوظائف</a></li>
    </ul>
  </div>

  <main>
    <section class="hero">
      <img src="img/banner.jpeg" alt="بانر رئيسي" class="hero-banner">
      <div class="hero-overlay">
        <h1>شركة النصيان القابضة</h1>
      </div>
      <a href="#overview" class="scroll-down-btn">النزول للأسفل</a>
    </section>

    <section id="overview" class="overview-section">
      <div class="container">
        <h2>لمحة سريعة</h2>
        <div class="overview-grid">
          <div class="overview-item"><h3>2015-04-14</h3><p>تاريخ التأسيس</p></div>
          <div class="overview-item"><h3>5 آلاف+</h3><p>موظف مبدع</p></div>
          <div class="overview-item"><h3>27+</h3><p>موقع داخل السعودية</p></div>
          <div class="overview-item"><h3>14+</h3><p>شركة حكومية وخاصة</p></div>
        </div>
        <a href="about.html" class="btn btn-primary">حول شركة النصيان القابضة</a>
      </div>
    </section>
  </main>

  <footer>
    <div class="container">
      <div class="footer-columns">
        <div class="footer-col">
          <h4>اتصل بنا</h4>
          <p>شركة النصيان القابضة<br>طريق الملك سعود<br>ص.ب: 402، الخبر 31952<br>المملكة العربية السعودية</p>
          <p>الهاتف: <a href="tel:+966138145555">+966-13-814-5555</a></p>
          <p>البريد الإلكتروني: <a href="mailto:info@alnasyan.com">info@alnasyan.com</a></p>
        </div>
        <div class="footer-col">
          <h4>روابط سريعة</h4>
          <ul>
            <li><a href="#">الشروط والأحكام</a></li>
            <li><a href="#">إخلاء المسؤولية</a></li>
            <li><a href="#">سياسة الخصوصية</a></li>
            <li><a href="#">خريطة الموقع</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>تابعنا</h4>
          <div class="social-icons">
            <a href="#"><svg>...</svg></a>
            <a href="#"><svg>...</svg></a>
            <a href="#"><svg>...</svg></a>
            <a href="#"><svg>...</svg></a>
          </div>
          <img src="img/vision_2030.png" alt="رؤية السعودية 2030" style="width: 100px; margin-top: 15px;" />
        </div>
      </div>
      <div class="copyright">
        <p>&copy; 2025 شركة النصيان القابضة. جميع الحقوق محفوظة.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>

