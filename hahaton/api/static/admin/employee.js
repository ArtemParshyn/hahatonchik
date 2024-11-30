document.addEventListener('DOMContentLoaded', function () {
    const isFounderCheckbox = document.querySelector('#id_is_founder');
    const zevisitField = document.querySelector('.field-zevisit');
    const projectField = document.querySelector('.field-project');


    // Функция для скрытия/показа поля
    function toggleZevisitField() {
        if (isFounderCheckbox.checked) {
            zevisitField.style.display = 'none'; // Скрыть поле
            projectField.style.display = 'none'; // Скрыть поле

        } else {
            zevisitField.style.display = ''; // Показать поле
            projectField.style.display = ''; // Показать поле

        }
    }

    // При загрузке страницы сразу настроить отображение
    toggleZevisitField();

    // Добавить обработчик события для изменения чекбокса
    isFounderCheckbox.addEventListener('change', toggleZevisitField);
});
