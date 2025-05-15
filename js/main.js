// ملف main.js

function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("active");
}

// إغلاق القائمة عند الضغط على رابط داخلها (اختياري لتحسين UX)
document.addEventListener("DOMContentLoaded", function () {
  const sidebarLinks = document.querySelectorAll(".sidebar a");
  sidebarLinks.forEach(link => {
    link.addEventListener("click", () => {
      document.getElementById("sidebar").classList.remove("active");
    });
  });
});
