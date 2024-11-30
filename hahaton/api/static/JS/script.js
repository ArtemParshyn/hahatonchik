document.addEventListener("DOMContentLoaded", function () {
  const BUTTON = document.getElementById("Button");
  BUTTON.onclick = function () {
    const EXPERIENCE = document.getElementById("experience");
    const POST = document.getElementById("Post");
    const DEPARTMENT = document.getElementById("Department");
    const SALARY = document.getElementById("Salary");
    const PROJECT = document.getElementById("project");
    console.log(1);
    //
    console.log(EXPERIENCE);
    //Поиск тут потом будет фетч который отправит данные на json сервак

    // Формируем объект с данными для отправки
    const data = {
      experience: EXPERIENCE.value,
      post: POST.value,
      salary: SALARY.value,
      department: DEPARTMENT.value,
      project: PROJECT.value,
    };
    console.log("data");
    fetch("/search_page", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Успех:", result);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
      });
  };
});
