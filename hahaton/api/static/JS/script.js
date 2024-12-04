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
    console.log(data);
    fetch("/search_page", {
      method: "POST",
      headers: { "Content-Type": "application/json",},
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        employees = result.employees;
        const employeesContainer = document.getElementById("employees-container");

        employeesContainer.innerHTML = "";

            // Создаем и добавляем сотрудников в контейнер
        employees.forEach((employee) => {
    const employeeDiv = document.createElement("div");
    employeeDiv.className = "employee-card";

    employeeDiv.innerHTML = `
      <p><strong>ФИО:</strong> ${employee.fio}</p>
      <p><strong>Возраст:</strong> ${employee.age}</p>
      <button class="fetch-details" data-id="${employee.id}">Подробнее</button>
      <div class="details" id="details-${employee.id}" style="display: none;">
        <p>Загрузка данных...</p>
      </div>
    `;

    employeesContainer.appendChild(employeeDiv);
  });
        console.log("Успех:", result);
      })
      .catch((error) => {
        console.error("Ошибка:", error);
      });
  };
});
