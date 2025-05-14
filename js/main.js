document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = document.querySelector(".nav-menu");

    if (menuToggle && navMenu) {
        // فتح / إغلاق القائمة عند الضغط على زر التبديل
        menuToggle.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });

        // إغلاق القائمة تلقائيًا بعد اختيار أي عنصر (مهم للجوال)
        navMenu.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", function () {
                navMenu.classList.remove("active");
            });
        });
    }

    // التمرير السلس عند الضغط على روابط داخلية (anchor links)
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
