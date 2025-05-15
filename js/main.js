document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle"); // زر ☰
    const sidebar = document.querySelector(".sidebar");        // القائمة الجانبية
    const closeBtn = document.querySelector(".close-btn");     // زر الإغلاق ×

    // فتح القائمة الجانبية
    if (menuToggle && sidebar) {
        menuToggle.addEventListener("click", function () {
            sidebar.classList.add("active");
        });
    }

    // إغلاق القائمة عند الضغط على زر ×
    if (closeBtn && sidebar) {
        closeBtn.addEventListener("click", function () {
            sidebar.classList.remove("active");
        });
    }

    // إغلاق القائمة عند الضغط على أي رابط داخل القائمة
    sidebar.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", function () {
            sidebar.classList.remove("active");
        });
    });

    // إغلاق القائمة إذا ضغط خارجها (اختياري)
    document.addEventListener("click", function (e) {
        if (!sidebar.contains(e.target) && !menuToggle.contains(e.target)) {
            sidebar.classList.remove("active");
        }
    });

    // التمرير السلس عند الضغط على روابط داخلية (anchor)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href");
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });
});
